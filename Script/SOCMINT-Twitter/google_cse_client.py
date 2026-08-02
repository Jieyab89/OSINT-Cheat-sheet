"""Look up general web results via the Google Custom Search JSON API
(https://developers.google.com/custom-search/v1/overview) — a 4th data
source alongside Cookie/Xquik (live X data) and Wayback (archived X pages).

Unlike the other three, this source isn't X-specific: it searches whatever
scope the Custom Search Engine (cx) itself is configured for on Google's
side, so it's the one lane that can surface a username/keyword showing up
*off* X entirely — news mentions, forum posts, cached pages, other social
platforms — which is what makes it worth adding to Multi Source Search.

Requires two values in config.ini [google_cse]:
  api_key — issued via Google Cloud/API Console (enable "Custom Search API")
  cx      — the Search Engine ID from https://programmablesearchengine.google.com/

Free tier: 100 queries/day. Each page here costs exactly one query
(Google caps `num` at 10 results/request), so `count` is served in
10-result pages up to a hard ceiling well under the daily quota.
"""

import configparser
import html
import re
from concurrent.futures import ThreadPoolExecutor

import requests

from id_forensics import decode_snowflake

CSE_URL         = "https://www.googleapis.com/customsearch/v1"
REQUEST_TIMEOUT = 20
PAGE_SIZE        = 10    # Google's hard max for `num`
MAX_RESULTS      = 50    # ceiling on results served per call, regardless of `count`

# Google truncates BOTH the title and the snippet it hands back in the SERP
# JSON — title gets clipped just like the snippet does (see the module intro
# reasoning). For text-intel use we want the page's own full title and
# description instead, so every result with a link gets a best-effort live
# fetch to pull its real og:/twitter: tags — same technique wayback_client.py
# uses on archived snapshots, just against the live page instead.
ENRICH_TIMEOUT = 10
ENRICH_WORKERS = 8
META_PARSE_CAP = 300_000   # bytes of HTML scanned for meta tags

_SAFE_URL_RE  = re.compile(r"^https?://", re.IGNORECASE)
_META_TAG_RE  = re.compile(r"<meta\b[^>]*>", re.IGNORECASE)
_ATTR_RE      = re.compile(r'''([\w:-]+)\s*=\s*"([^"]*)"|([\w:-]+)\s*=\s*'([^']*)\'''')
_TITLE_TAG_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.IGNORECASE | re.DOTALL)
_TWEET_ID_RE  = re.compile(r"/status/(\d+)")


def _tweet_created_at(url: str) -> str | None:
    """When `url` is a tweet permalink (…/status/<id>), decode the actual
    post-creation time straight out of the id's Snowflake bits. Same field
    name/format cookie and xquik already populate (`created_at`, Twitter's
    own classic timestamp string), so every source is consistent — and
    absent entirely for non-X results, same as it's absent for anything
    without a usable id."""
    m = _TWEET_ID_RE.search(url or "")
    if not m:
        return None
    dt = decode_snowflake(m.group(1))
    if not dt:
        return None
    return dt.strftime("%a %b %d %H:%M:%S +0000 %Y")


class GoogleCSEError(Exception):
    pass


def _get_client_config(config: configparser.ConfigParser) -> tuple[str, str]:
    api_key = config.get("google_cse", "api_key", fallback="").strip()
    cx      = config.get("google_cse", "cx", fallback="").strip()
    if not api_key or api_key == "YOUR_GOOGLE_API_KEY":
        raise GoogleCSEError("api_key belum diisi di config.ini [google_cse]")
    if not cx or cx == "YOUR_SEARCH_ENGINE_ID":
        raise GoogleCSEError("cx (Search Engine ID) belum diisi di config.ini [google_cse]")
    return api_key, cx


def _extract_thumbnail(item: dict) -> str | None:
    pagemap = item.get("pagemap") or {}
    for key in ("cse_image", "cse_thumbnail"):
        candidates = pagemap.get(key) or []
        if candidates and isinstance(candidates, list):
            src = (candidates[0] or {}).get("src", "").strip()
            # Third-party page metadata — only trust it if it's a plain http(s)
            # link, since the frontend renders this straight into an <a href>.
            if src and _SAFE_URL_RE.match(src):
                return src
    return None


def _row_to_record(item: dict) -> dict:
    record = {}
    title = item.get("title")
    if title:
        record["post_title"] = html.unescape(title).strip()
    snippet = item.get("snippet")
    if snippet:
        record["post_text"] = html.unescape(snippet).strip()
    link = item.get("link")
    if link and _SAFE_URL_RE.match(link):
        record["result_url"] = link
        created_at = _tweet_created_at(link)
        if created_at:
            record["created_at"] = created_at   # when the post itself was actually made
    display_link = item.get("displayLink")
    if display_link:
        record["display_link"] = display_link
    thumb = _extract_thumbnail(item)
    if thumb:
        record["preview_image"] = thumb
    return record


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


def _fetch_live_meta(url: str) -> dict:
    """Best-effort live fetch of the result's own page — pulls its real
    title and og:/twitter:/meta description to replace Google's clipped SERP
    title+snippet. Any failure (timeout, non-200, no usable tags) is
    swallowed — the caller just keeps Google's own (possibly truncated)
    values as a fallback."""
    try:
        r = requests.get(url, timeout=ENRICH_TIMEOUT, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240"})
        if r.status_code != 200 or not r.text:
            return {}
    except requests.RequestException:
        return {}

    body  = r.text[:META_PARSE_CAP]
    tags  = _parse_meta_tags(body)
    out   = {}

    title = tags.get("og:title") or tags.get("twitter:title") or _extract_title_tag(body)
    if title:
        out["post_title"] = html.unescape(title).strip()

    desc = tags.get("og:description") or tags.get("twitter:description") or tags.get("description")
    if desc:
        out["post_text"] = html.unescape(desc).strip()

    image = tags.get("og:image") or tags.get("twitter:image")
    if image:
        image = html.unescape(image).strip()
        if _SAFE_URL_RE.match(image):
            out["preview_image"] = image

    return out


def _enrich_records(records: list[dict]) -> None:
    """Mutates each record in place. Runs in parallel — one slow/dead site
    shouldn't hold up the rest of the result set."""
    candidates = [r for r in records if r.get("result_url")]
    if not candidates:
        return

    def _job(rec):
        extra = _fetch_live_meta(rec["result_url"])
        if extra.get("post_title"):
            rec["post_title"] = extra["post_title"]
        if extra.get("post_text"):
            rec["post_text"] = extra["post_text"]
        if extra.get("preview_image") and not rec.get("preview_image"):
            rec["preview_image"] = extra["preview_image"]

    with ThreadPoolExecutor(max_workers=ENRICH_WORKERS) as pool:
        list(pool.map(_job, candidates))


def _fetch_page(query: str, api_key: str, cx: str, start: int) -> list[dict]:
    params = {
        "key":  api_key,
        "cx":   cx,
        "q":    query,
        "num":  PAGE_SIZE,
        "start": start,
    }
    try:
        r = requests.get(CSE_URL, params=params, timeout=REQUEST_TIMEOUT)
    except requests.RequestException as e:
        raise GoogleCSEError(f"Google CSE request failed: {e}") from e

    if r.status_code == 429:
        raise GoogleCSEError("Google CSE daily quota exceeded (100 free queries/day)")
    if r.status_code == 403:
        raise GoogleCSEError("Google CSE request forbidden — check api_key/cx and that the "
                              "Custom Search API is enabled for that key's project")
    if r.status_code >= 400:
        raise GoogleCSEError(f"Google CSE API error {r.status_code}: {r.text[:300]}")

    try:
        body = r.json()
    except ValueError as e:
        raise GoogleCSEError(f"Response bukan JSON valid: {r.text[:300]}") from e

    return body.get("items") or []


# ── Public API ───────────────────────────────────────────────────────────────

def google_cse_search(raw_query: str, count: int = 20, config: configparser.ConfigParser = None,
                       cursor: str | None = None) -> tuple[list[dict], str | None]:
    """Returns (records, next_cursor). `cursor` is the opaque 1-based `start`
    index from a previous call's next_cursor — pass it back to fetch the next
    page. None once there's nothing more to load (or the MAX_RESULTS ceiling
    is hit, to keep one Multi Source Search from burning the whole daily quota)."""
    query = (raw_query or "").strip()
    if not query:
        raise GoogleCSEError("Search query is required")

    api_key, cx = _get_client_config(config)

    try:
        start = int(cursor) if cursor else 1
    except ValueError:
        start = 1

    target  = min(max(1, count), MAX_RESULTS)
    records: list[dict] = []
    next_cursor = None

    while len(records) < target:
        items = _fetch_page(query, api_key, cx, start)
        if not items:
            break
        for item in items:
            records.append(_row_to_record(item))
            if len(records) >= target:
                break
        start += PAGE_SIZE
        if len(items) < PAGE_SIZE:
            break   # Google itself signaled this was the last page
        if start > MAX_RESULTS:
            break

    _enrich_records(records)

    if records and start <= MAX_RESULTS:
        next_cursor = str(start)

    return records, next_cursor
