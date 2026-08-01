"""Look up archived snapshots of X/Twitter pages via the Internet Archive's
Wayback Machine CDX API (https://web.archive.org/cdx/search/cdx) — no API key
required. Useful for OSINT recovery of deleted tweets/profiles: a bare
username is expanded into a prefix search across both x.com and twitter.com
so every archived page the crawler ever saw under that profile comes back,
including individual tweet permalinks.

Each snapshot is additionally enriched by fetching the archived HTML itself
(via the Wayback "id_" identity flag, which returns the original bytes with
no toolbar/rewriting) and pulling the og:/twitter: meta tags out of it — that
is how X serves post text to link-preview crawlers, so it works even though
the live site is a JS shell.
"""

import html
import re
from concurrent.futures import ThreadPoolExecutor

import requests

WAYBACK_CDX_URL  = "https://web.archive.org/cdx/search/cdx"
REQUEST_TIMEOUT  = 30
SNAPSHOT_TIMEOUT = 10   # per-snapshot content fetch, run in parallel
ENRICH_WORKERS   = 8
META_PARSE_CAP   = 300_000   # bytes of HTML scanned for meta tags


class WaybackError(Exception):
    pass


_DATE8_RE   = re.compile(r"^\d{8}$")
_SAFE_URL_RE = re.compile(r"^https?://", re.IGNORECASE)


def _validate_date(label: str, value: str) -> None:
    if value and not _DATE8_RE.match(value):
        raise WaybackError(f"{label} must be an 8-digit date (YYYYMMDD)")


def _normalize_target(raw: str) -> str:
    target = (raw or "").strip()
    if not target:
        raise WaybackError("Target username or URL is required")
    if target.startswith("http://") or target.startswith("https://"):
        target = target.split("://", 1)[1]
    target = target.lstrip("@")
    if "/" not in target and "." not in target:
        target = f"x.com/{target}"
    return target


def _fetch_cdx(url: str, limit: int, from_date: str = "", to_date: str = "",
                match_type: str | None = None) -> list[dict]:
    params = {
        "url":      url,
        "output":   "json",
        "fl":       "timestamp,original,statuscode,mimetype,length",
        "collapse": "digest",
        "limit":    str(limit),
    }
    if match_type:
        params["matchType"] = match_type
    if from_date:
        params["from"] = from_date
    if to_date:
        params["to"] = to_date

    try:
        r = requests.get(
            WAYBACK_CDX_URL, params=params, timeout=REQUEST_TIMEOUT,
            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240"},
        )
        r.raise_for_status()
    except requests.RequestException as e:
        raise WaybackError(f"Wayback CDX request failed: {e}") from e

    try:
        rows = r.json()
    except ValueError:
        return []
    if not rows or len(rows) < 2:
        return []

    header, *data_rows = rows
    return [dict(zip(header, row)) for row in data_rows]


def _row_to_record(row: dict) -> dict:
    ts       = row.get("timestamp", "") or ""
    original = row.get("original", "") or ""
    iso_date = None
    if len(ts) >= 14:
        iso_date = f"{ts[0:4]}-{ts[4:6]}-{ts[6:8]} {ts[8:10]}:{ts[10:12]}:{ts[12:14]}"
    return {
        "timestamp":   ts,   # internal only — stripped before returning to caller
        "iso_date":    iso_date,
        "original":    original,
        "statuscode":  row.get("statuscode"),
        "mimetype":    row.get("mimetype"),
        "length":      row.get("length"),
        "archive_url": f"https://web.archive.org/web/{ts}/{original}" if ts and original else None,
    }


# ── Content enrichment ──────────────────────────────────────────────────────

_META_TAG_RE  = re.compile(r"<meta\b[^>]*>", re.IGNORECASE)
_ATTR_RE      = re.compile(r'''([\w:-]+)\s*=\s*"([^"]*)"|([\w:-]+)\s*=\s*'([^']*)\'''')
_TITLE_TAG_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.IGNORECASE | re.DOTALL)


def _parse_meta_tags(text: str) -> dict:
    tags = {}
    for tag in _META_TAG_RE.findall(text):
        attrs = {}
        for m in _ATTR_RE.finditer(tag):
            if m.group(1):
                attrs[m.group(1).lower()] = m.group(2)
            else:
                attrs[m.group(3).lower()] = m.group(4)
        key = attrs.get("property") or attrs.get("name")
        val = attrs.get("content")
        if key and val is not None:
            tags[key.lower()] = val
    return tags


def _extract_title_tag(text: str) -> str | None:
    m = _TITLE_TAG_RE.search(text)
    if not m:
        return None
    title = re.sub(r"\s+", " ", m.group(1)).strip()
    return title or None


def _fetch_snapshot_meta(timestamp: str, original: str) -> dict:
    if not timestamp or not original:
        return {}
    snap_url = f"https://web.archive.org/web/{timestamp}id_/{original}"
    try:
        r = requests.get(
            snap_url, timeout=SNAPSHOT_TIMEOUT,
            headers={"User-Agent": "Mozilla/5.0"},
        )
        if r.status_code != 200 or not r.text:
            return {}
    except requests.RequestException:
        return {}

    body  = r.text[:META_PARSE_CAP]
    tags  = _parse_meta_tags(body)
    # og:/twitter: tags cover ~2012-2022 era captures; plain <meta name="description">
    # and <title> are what older (pre-2012) and some modern captures fall back to.
    title = tags.get("og:title") or tags.get("twitter:title") or _extract_title_tag(body)
    text  = tags.get("og:description") or tags.get("twitter:description") or tags.get("description")
    image = tags.get("og:image") or tags.get("twitter:image")

    out = {}
    if title:
        out["post_title"] = html.unescape(title).strip()
    if text:
        out["post_text"] = html.unescape(text).strip()
    # Archived pages are third-party content — an og:image value could in principle
    # be a "javascript:"/"data:" URI. Only ever keep it if it's a plain http(s) link,
    # since the frontend renders this straight into an <a href>.
    if image:
        image = html.unescape(image).strip()
        if _SAFE_URL_RE.match(image):
            out["preview_image"] = image
    return out


def _enrich_records(records: list[dict]) -> None:
    """Fetch post content for each html/200 snapshot in parallel. Mutates in place;
    failures are silently skipped so one dead snapshot doesn't sink the whole search."""
    candidates = [r for r in records if r.get("mimetype") == "text/html" and str(r.get("statuscode")) == "200"]
    if not candidates:
        return

    def _job(rec):
        rec.update(_fetch_snapshot_meta(rec.get("timestamp"), rec.get("original")))

    with ThreadPoolExecutor(max_workers=ENRICH_WORKERS) as pool:
        list(pool.map(_job, candidates))


# ── Public API ───────────────────────────────────────────────────────────────

def wayback_search(raw_target: str, count: int = 50, from_date: str = "", to_date: str = "") -> list[dict]:
    _validate_date("from_date", from_date)
    _validate_date("to_date", to_date)
    target       = _normalize_target(raw_target)
    is_permalink = "/status/" in target

    rows: list[dict] = []

    if is_permalink:
        rows = _fetch_cdx(target, count, from_date, to_date)
    else:
        domain, _, path = target.partition("/")
        candidates = [target]
        alt_domain = "twitter.com" if domain == "x.com" else ("x.com" if domain == "twitter.com" else None)
        if alt_domain:
            candidates.append(f"{alt_domain}/{path}")

        seen = set()
        for cand in candidates:
            for row in _fetch_cdx(cand, count, from_date, to_date, match_type="prefix"):
                key = (row.get("timestamp"), row.get("original"))
                if key in seen:
                    continue
                seen.add(key)
                rows.append(row)

    records = [_row_to_record(r) for r in rows]
    records.sort(key=lambda r: r["timestamp"], reverse=True)
    records = records[:count]

    _enrich_records(records)

    for r in records:
        r.pop("timestamp", None)
    return records
