import json
import re
import secrets
import shutil
import threading
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import requests as _req
from flask import Flask, g, jsonify, render_template, request, Response, stream_with_context, send_from_directory

import archive as _archive
from xquik_client import XquikClient, XquikError, load_config
from wayback_client import wayback_search, WaybackError
from id_forensics import enrich_account_age
from cookie_client import (
    cookie_tweet_search,
    cookie_follower_explorer,
    cookie_post_extractor,
    cookie_article_extractor,
    cookie_community_post_extractor,
    cookie_tweet_replies,
    cookie_tweet_retweeters,
    cookie_geo_search,
    CookieClientError,
)

app = Flask(__name__)
config = load_config()

MAX_CONCURRENT_REQUESTS = 3   # parallel execution slots
ACQUIRE_TIMEOUT         = 15  # seconds to wait before returning 429

_sem = threading.Semaphore(MAX_CONCURRENT_REQUESTS)

# ── Cookie & session security ─────────────────────────────────────────────────

_https = config.getboolean("server", "https", fallback=False)

app.config.update(
    SECRET_KEY              = config.get("server", "secret_key", fallback=secrets.token_hex(32)),
    SESSION_COOKIE_HTTPONLY = True,
    SESSION_COOKIE_SAMESITE = "Strict",
    SESSION_COOKIE_SECURE   = _https,   # True only when TLS is terminated at Flask
)

# ── Security headers ──────────────────────────────────────────────────────────

@app.before_request
def _make_nonce():
    g.csp_nonce = secrets.token_urlsafe(16)


@app.after_request
def _set_security_headers(response):
    nonce = getattr(g, "csp_nonce", "")
    csp = (
        "default-src 'none'; "
        f"script-src 'nonce-{nonce}' https://unpkg.com; "
        "style-src 'unsafe-inline' https://unpkg.com; "
        "img-src 'self' data: blob: "
            "https://*.twimg.com "
            "https://*.tile.openstreetmap.org "
            "https://server.arcgisonline.com "
            "https://*.tile.opentopomap.org "
            "https://unpkg.com; "
        "media-src 'self'; "
        "connect-src 'self' https://nominatim.openstreetmap.org; "
        "font-src 'none'; "
        "frame-src 'none'; "
        "object-src 'none'; "
        "base-uri 'self'; "
        "form-action 'self';"
    )
    response.headers["Content-Security-Policy"] = csp
    response.headers["X-Content-Type-Options"]  = "nosniff"
    response.headers["X-Frame-Options"]         = "DENY"
    response.headers["Referrer-Policy"]         = "no-referrer"
    response.headers["Permissions-Policy"]      = "geolocation=(), camera=(), microphone=()"
    response.headers["X-XSS-Protection"]        = "0"   # disable legacy broken auditor

    # Harden every Set-Cookie header regardless of where it originates
    raw_cookies = response.headers.getlist("Set-Cookie")
    if raw_cookies:
        response.headers.remove("Set-Cookie")
        for raw in raw_cookies:
            parts = [p.strip() for p in raw.split(";")]
            flags = {p.split("=")[0].strip().lower() for p in parts[1:]}
            if "httponly" not in flags:
                parts.append("HttpOnly")
            if "samesite" not in flags:
                parts.append("SameSite=Strict")
            if "secure" not in flags and _https:
                parts.append("Secure")
            response.headers.add("Set-Cookie", "; ".join(parts))

    return response


@app.route("/")
def index():
    return render_template("index.html")


# ── Multi-source search ────────────────────────────────────────────────────────
# Fans one query out to every available Twitter/X data source in parallel and
# tags each result with where it came from, so e.g. a search for "elonmusk"
# shows what's live via cookie session, what xquik's API returns, and what the
# Wayback Machine has archived — all in one merged list.

SOURCE_LABELS = {
    "cookie":  "Twitter Cookie",
    "xquik":   "Xquik API",
    "wayback": "Wayback Machine",
}


def _tag_source(items, label):
    if not isinstance(items, list):
        items = [items]
    return [{**it, "source": label} if isinstance(it, dict) else it for it in items]


# ── Optional date-range narrowing ───────────────────────────────────────────
# Dates come in from the client as free-text fields, so every value is run
# through this strict YYYYMMDD check before it touches a search query string
# or gets parsed — malformed input is just ignored (treated as "no bound"),
# never interpolated as-is.

_DATE8_RE = re.compile(r"^\d{8}$")


def _valid_date8(s: str) -> bool:
    if not s or not _DATE8_RE.match(s):
        return False
    try:
        datetime.strptime(s, "%Y%m%d")
        return True
    except ValueError:
        return False


def _apply_date_operators(query: str, from_date: str, to_date: str) -> str:
    """Narrow a Twitter search query with since:/until: operators. Only ever
    appends values that already passed strict date validation, so the date
    fields can't be used to smuggle arbitrary search syntax into the query."""
    parts = [query]
    if _valid_date8(from_date):
        parts.append(f"since:{from_date[0:4]}-{from_date[4:6]}-{from_date[6:8]}")
    if _valid_date8(to_date):
        parts.append(f"until:{to_date[0:4]}-{to_date[4:6]}-{to_date[6:8]}")
    return " ".join(parts)


def _parse_bound(date8: str, end_of_day: bool):
    if not _valid_date8(date8):
        return None
    dt = datetime.strptime(date8, "%Y%m%d")
    return dt.replace(hour=23, minute=59, second=59) if end_of_day else dt


def _item_datetime(item: dict):
    iso = item.get("iso_date")
    if iso:
        try:
            return datetime.strptime(iso, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            pass
    created = item.get("created_at")
    if created:
        try:
            return datetime.strptime(created, "%a %b %d %H:%M:%S %z %Y").replace(tzinfo=None)
        except ValueError:
            pass
    return None


def _filter_by_date(items: list, from_date: str, to_date: str) -> list:
    """Second pass over the merged results: drop anything whose own timestamp
    (iso_date for Wayback rows, created_at for tweets) falls outside the
    requested range. since:/until: and Wayback's from/to already narrow at
    the source — this catches whatever slips through that."""
    lo = _parse_bound(from_date, end_of_day=False)
    hi = _parse_bound(to_date, end_of_day=True)
    if not lo and not hi:
        return items

    kept = []
    for it in items:
        if not isinstance(it, dict):
            kept.append(it)
            continue
        dt = _item_datetime(it)
        if dt is None:
            kept.append(it)   # can't verify — keep rather than silently drop
            continue
        if lo and dt < lo:
            continue
        if hi and dt > hi:
            continue
        kept.append(it)
    return kept


def _multi_source_search(query: str, count: int, from_date: str = "", to_date: str = "") -> list:
    twitter_query = _apply_date_operators(query, from_date, to_date)
    jobs = {
        "cookie":  lambda: cookie_tweet_search(twitter_query, count=count, config=config),
        "xquik":   lambda: XquikClient(config).tweet_search(twitter_query),
        "wayback": lambda: wayback_search(query, count=count, from_date=from_date, to_date=to_date),
    }
    with ThreadPoolExecutor(max_workers=len(jobs)) as pool:
        futures = {key: pool.submit(fn) for key, fn in jobs.items()}
        results = []
        for key in ("cookie", "xquik", "wayback"):   # deterministic display order
            try:
                data = futures[key].result()
            except Exception:
                continue   # a source failing (missing creds, network, ...) shouldn't sink the others
            results.extend(_tag_source(data, SOURCE_LABELS[key]))

    return _filter_by_date(results, from_date, to_date)


# Whitelist: only proxy Twitter's video CDN to prevent SSRF
_VIDEO_CDN = ("https://video.twimg.com/",)

@app.route("/api/video")
def video_proxy():
    url = request.args.get("url", "").strip()
    if not any(url.startswith(prefix) for prefix in _VIDEO_CDN):
        return jsonify({"ok": False, "error": "URL not allowed"}), 403
    try:
        upstream = _req.get(
            url,
            stream=True,
            timeout=20,
            headers={"Referer": "https://x.com/", "User-Agent": "Mozilla/5.0"},
        )
        headers = {"Content-Type": upstream.headers.get("Content-Type", "video/mp4")}
        if "Content-Length" in upstream.headers:
            headers["Content-Length"] = upstream.headers["Content-Length"]
        return Response(
            stream_with_context(upstream.iter_content(chunk_size=32768)),
            status=upstream.status_code,
            headers=headers,
        )
    except _req.RequestException as e:
        return jsonify({"ok": False, "error": str(e)}), 502


@app.route("/api/run", methods=["POST"])
def run_tool():
    body      = request.get_json(silent=True) or {}
    tool_type = body.get("toolType")
    mode      = body.get("mode", "api")   # "api" | "cookie"
    count     = max(1, min(int(body.get("count", 20)), 200))

    if not _sem.acquire(blocking=True, timeout=ACQUIRE_TIMEOUT):
        return jsonify({
            "ok": False,
            "error": "Server is busy — max concurrent requests reached. Please try again shortly.",
        }), 429

    try:
        if tool_type == "tweet_search_extractor":
            query = body.get("searchQuery", "")
            if mode == "cookie":
                data = cookie_tweet_search(query, count=count, config=config)
            else:
                data = XquikClient(config).tweet_search(query)

        elif tool_type == "follower_explorer":
            username = body.get("targetUsername", "")
            if mode == "cookie":
                data = cookie_follower_explorer(username, count=count, config=config)
            else:
                data = XquikClient(config).follower_explorer(username)

        elif tool_type == "article_extractor":
            tweet_id = body.get("targetTweetId", "")
            if mode == "cookie":
                data = cookie_article_extractor(tweet_id, config=config)
            else:
                data = XquikClient(config).article_extractor(tweet_id)

        elif tool_type == "community_post_extractor":
            community_id = body.get("targetCommunityId", "")
            if mode == "cookie":
                data = cookie_community_post_extractor(community_id, count=count, config=config)
            else:
                data = XquikClient(config).community_post_extractor(community_id)

        elif tool_type == "post_extractor":
            username = body.get("targetUsername", "")
            if mode == "cookie":
                data = cookie_post_extractor(username, count=count, config=config)
            else:
                data = XquikClient(config).post_extractor(username)

        elif tool_type == "tweet_replies_extractor":
            tweet_id = body.get("targetTweetId", "")
            if mode != "cookie":
                return jsonify({"ok": False, "error": "tweet_replies_extractor requires cookie mode"}), 400
            data = cookie_tweet_replies(tweet_id, count=count, config=config)

        elif tool_type == "tweet_retweeters_extractor":
            tweet_id = body.get("targetTweetId", "")
            if mode != "cookie":
                return jsonify({"ok": False, "error": "tweet_retweeters_extractor requires cookie mode"}), 400
            data = cookie_tweet_retweeters(tweet_id, count=count, config=config)

        elif tool_type == "geo_post_extractor":
            keyword = body.get("searchQuery", "")
            if mode != "cookie":
                return jsonify({"ok": False, "error": "geo_post_extractor requires cookie mode"}), 400
            data = cookie_geo_search(keyword, count=count, config=config)

        elif tool_type == "wayback_archive_search":
            target    = body.get("searchQuery", "")
            from_date = body.get("waybackFrom", "")
            to_date   = body.get("waybackTo", "")
            for label, val in (("waybackFrom", from_date), ("waybackTo", to_date)):
                if val and not _valid_date8(val):
                    return jsonify({"ok": False, "error": f"{label} must be an 8-digit date (YYYYMMDD)"}), 400
            data = wayback_search(target, count=count, from_date=from_date, to_date=to_date)

        elif tool_type == "multi_source_search":
            query     = body.get("searchQuery", "")
            from_date = body.get("dateFrom", "")
            to_date   = body.get("dateTo", "")
            for label, val in (("dateFrom", from_date), ("dateTo", to_date)):
                if val and not _valid_date8(val):
                    return jsonify({"ok": False, "error": f"{label} must be an 8-digit date (YYYYMMDD)"}), 400
            data = _multi_source_search(query, count=count, from_date=from_date, to_date=to_date)

        else:
            return jsonify({"ok": False, "error": f"Unknown toolType: {tool_type}"}), 400

        # Single choke point: every tool's output passes through here, so the
        # account-age label shows up everywhere downstream for free — cards,
        # graph nodes, JSON dump, and archives (once the fields are whitelisted
        # in archive.py's _pick_fields).
        data = enrich_account_age(data)

        return jsonify({"ok": True, "data": data})

    except (XquikError, CookieClientError, WaybackError) as e:
        return jsonify({"ok": False, "error": str(e)}), 400
    except Exception as e:  # noqa: BLE001
        return jsonify({"ok": False, "error": f"Unexpected error: {e}"}), 500
    finally:
        _sem.release()


# ── Archive routes ────────────────────────────────────────────────────────────

@app.route("/graph")
def graph_viewer():
    return render_template("graph.html")


@app.route("/archives")
def archive_viewer():
    return render_template("archive.html")


@app.route("/api/archive/<archive_id>/results")
def archive_results(archive_id):
    base = _archive.ARCHIVE_ROOT / archive_id
    results_file = base / "results.json"
    meta_file    = base / "meta.json"
    if not results_file.exists():
        return jsonify({"ok": False, "error": "Archive not found"}), 404
    return jsonify({
        "ok":      True,
        "results": json.loads(results_file.read_text()),
        "meta":    json.loads(meta_file.read_text()) if meta_file.exists() else {},
    })


@app.route("/api/archive/<archive_id>/media/<path:filename>")
def archive_media(archive_id, filename):
    media_dir = _archive.ARCHIVE_ROOT / archive_id / "media"
    return send_from_directory(str(media_dir), filename)


@app.route("/api/archive/<archive_id>", methods=["DELETE"])
def archive_delete(archive_id):
    archive_dir = _archive.ARCHIVE_ROOT / archive_id
    if not archive_dir.exists():
        return jsonify({"ok": False, "error": "Archive not found"}), 404
    shutil.rmtree(archive_dir)
    return jsonify({"ok": True})


@app.route("/api/archive", methods=["POST"])
def archive_start():
    body       = request.get_json(silent=True) or {}
    tool_type  = body.get("toolType", "unknown")
    data       = body.get("data")
    query_info = body.get("queryInfo", {})
    if not data:
        return jsonify({"ok": False, "error": "No data provided"}), 400
    archive_id = _archive.start(tool_type, data, query_info)
    return jsonify({"ok": True, "archiveId": archive_id})


@app.route("/api/archive/<archive_id>/status")
def archive_status(archive_id):
    s = _archive.status(archive_id)
    if s is None:
        return jsonify({"ok": False, "error": "Archive not found"}), 404
    return jsonify({"ok": True, **s})


@app.route("/api/archive/list")
def archive_list():
    return jsonify({"ok": True, "archives": _archive.list_all()})


if __name__ == "__main__":
    host  = config.get("server", "host",  fallback="127.0.0.1")
    port  = config.getint("server", "port", fallback=5000)
    debug = config.getboolean("server", "debug", fallback=True)
    app.run(host=host, port=port, debug=debug, threaded=True)
