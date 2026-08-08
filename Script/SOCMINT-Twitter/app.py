import json
import os
import re
import secrets
import shutil
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import requests as _req
from flask import Flask, g, jsonify, render_template, request, Response, stream_with_context, send_from_directory

import archive as _archive
import sentiment as _sentiment
from xquik_client import XquikClient, XquikError, load_config
from wayback_client import wayback_search, WaybackError
from google_cse_client import google_cse_search, GoogleCSEError
from id_forensics import enrich_account_age
from cookie_client import (
    cookie_tweet_search,
    cookie_follower_explorer,
    cookie_following_explorer,
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
MAX_COUNT               = 2000  # upper bound on a single page's requested item count

_sem = threading.Semaphore(MAX_CONCURRENT_REQUESTS)

# ── Rate-limit protection for paginated load-more requests ─────────────────
# Separate from the concurrency semaphore above, which limits how many
# requests run *at once* — this limits how *often* the same external
# account/service gets hit, regardless of which tab/tool triggered it. All
# cookie-mode calls hit the same logged-in X account, so they share one
# clock (a fresh search 2s after a scroll-load-more should still wait);
# Wayback calls hit archive.org, unrelated to X's ban risk, so they get
# their own independent clock.
_THROTTLE_SECONDS = 5.0
_throttle_lock     = threading.Lock()
_last_call_at: dict = {"cookie": 0.0, "wayback": 0.0}

_COOKIE_TOOLS = {
    "tweet_search_extractor", "follower_explorer", "following_explorer", "post_extractor",
    "community_post_extractor", "tweet_replies_extractor",
    "tweet_retweeters_extractor", "geo_post_extractor",
}


def _check_throttle(sources):
    """None if the call may proceed (and starts the next cooldown window for
    every source in `sources`); otherwise the number of seconds still left to
    wait. Checking is atomic across all requested sources — if any one of
    them is still cooling down, none of the clocks are touched, so a
    rejected multi-source call (e.g. multi_source_search, which hits both
    the cookie and wayback clocks) never partially starts a window for the
    sources that *did* have room."""
    if isinstance(sources, str):
        sources = (sources,)
    now = time.monotonic()
    with _throttle_lock:
        wait = 0.0
        for source in sources:
            elapsed = now - _last_call_at[source]
            if elapsed < _THROTTLE_SECONDS:
                wait = max(wait, _THROTTLE_SECONDS - elapsed)
        if wait:
            return round(wait, 1)
        for source in sources:
            _last_call_at[source] = now
        return None

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
    "cse":     "Google CSE",
}


def _tag_source(items, label):
    if not isinstance(items, list):
        items = [items]
    return [{**it, "source": label} if isinstance(it, dict) else it for it in items]


def _stamp_fetched_at(data):
    """Mutates every dict in `data` (list or single dict) in place, adding
    fetched_at — when *this app* pulled the record, as opposed to created_at
    (a tweet's own post time) or iso_date (a Wayback snapshot's capture time).
    Applied uniformly across every source so results are comparable no
    matter which tool/source produced them."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    items = data if isinstance(data, list) else [data]
    for item in items:
        if isinstance(item, dict):
            item["fetched_at"] = now
    return data


def _stamp_tweet_url(data):
    """Mutates every dict in `data` (list or single dict) in place, adding
    tweet_url wherever id+user identify an actual tweet — the citable-link
    field Wayback (archive_url/original) and Google CSE (result_url) already
    carry directly in their own data. Cookie/xquik never set this on the raw
    tweet dict themselves — previously it only got built at archive time, so a
    live card, a JSON dump, and an archive of the same search could each show
    a different answer for "what's the URL." Building it once here means all
    three read the identical value. archive.py's build_tweet_url() reuses this
    same logic rather than recomputing it separately."""
    items = data if isinstance(data, list) else [data]
    for item in items:
        if isinstance(item, dict) and not item.get("tweet_url"):
            url = _archive.build_tweet_url(item)
            if url:
                item["tweet_url"] = url
    return data


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


def _multi_source_search(
    query: str, count: int, from_date: str = "", to_date: str = "", cursor: str | None = None,
) -> tuple[list, str | None, dict]:
    """Fans out across every source in parallel. cursor (if given) is an
    opaque JSON object of {source: source_cursor} built from a previous
    call's returned cursor — each key present in it is a source that still
    had more to give, so only those get re-queried. xquik has no pagination
    at all (no cursor concept), so it's only ever queried on the first page
    (cursor=None); every load-more page after that is cookie/wayback/cse only.
    A cursor value that doesn't parse as a JSON object is treated as "no
    cursor" (first page) rather than raising — same tolerant-of-garbage-input
    posture as the rest of this file's client-supplied-field handling.

    Third return value is {source: error_message} for any source that failed
    this round (missing creds, network blip, quota hit, ...) — a source
    failing shouldn't sink the others, but silently dropping it also leaves
    the caller unable to tell "this source ran dry" apart from "this source
    is broken right now," which matters most on a load-more page where the
    UI would otherwise just look like that source stopped contributing for
    no reason."""
    twitter_query = _apply_date_operators(query, from_date, to_date)

    try:
        incoming = json.loads(cursor) if cursor else {}
        if not isinstance(incoming, dict):
            incoming = {}
    except (TypeError, ValueError):
        incoming = {}
    first_page = not incoming

    jobs = {}
    if first_page or "cookie" in incoming:
        c = incoming.get("cookie")
        jobs["cookie"] = lambda c=c: cookie_tweet_search(twitter_query, count=count, config=config, cursor=c)
    if first_page:
        jobs["xquik"] = lambda: (XquikClient(config).tweet_search(twitter_query), None)
    if first_page or "wayback" in incoming:
        c = incoming.get("wayback")
        jobs["wayback"] = lambda c=c: wayback_search(query, count=count, from_date=from_date, to_date=to_date, cursor=c)
    if first_page or "cse" in incoming:
        c = incoming.get("cse")
        # Google has no since:/until: query syntax like Twitter/Wayback do, so
        # this lane runs unbounded by date — _filter_by_date below keeps
        # results whose own timestamp it can't verify rather than dropping them.
        jobs["cse"] = lambda c=c: google_cse_search(query, count=count, config=config, cursor=c)

    results          = []
    next_cursor_parts = {}
    source_errors     = {}
    with ThreadPoolExecutor(max_workers=len(jobs)) as pool:
        futures = {key: pool.submit(fn) for key, fn in jobs.items()}
        for key in ("cookie", "xquik", "wayback", "cse"):   # deterministic display order
            if key not in futures:
                continue
            try:
                data, next_c = futures[key].result()
            except Exception as e:
                source_errors[key] = str(e)
                continue   # a source failing (missing creds, network, ...) shouldn't sink the others
            results.extend(_tag_source(data, SOURCE_LABELS[key]))
            if next_c:
                next_cursor_parts[key] = next_c

    next_cursor = json.dumps(next_cursor_parts) if next_cursor_parts else None
    return _filter_by_date(results, from_date, to_date), next_cursor, source_errors


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
            headers={"Referer": "https://x.com/", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240"},
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
    count     = max(1, min(int(body.get("count", 20)), MAX_COUNT))
    cursor    = body.get("cursor") or None   # opaque page token from a previous response's nextCursor

    # Cookie/Wayback calls are throttled to one per 5s per source — checked
    # up front, before taking a concurrency slot, so a request that's about
    # to be rejected doesn't waste one. multi_source_search fans out to both
    # cookie and wayback internally, so it's checked (and, once it proceeds,
    # starts the cooldown) against both clocks at once.
    throttle_sources = []
    if mode == "cookie" and tool_type in _COOKIE_TOOLS:
        throttle_sources = ["cookie"]
    elif tool_type == "wayback_archive_search":
        throttle_sources = ["wayback"]
    elif tool_type == "multi_source_search":
        throttle_sources = ["cookie", "wayback"]
    if throttle_sources:
        wait = _check_throttle(throttle_sources)
        if wait is not None:
            return jsonify({
                "ok": False,
                "error": f"Please wait {wait}s before the next {'/'.join(throttle_sources)} request — this protects the account from rate limiting.",
                "retryAfter": wait,
            }), 429

    if not _sem.acquire(blocking=True, timeout=ACQUIRE_TIMEOUT):
        return jsonify({
            "ok": False,
            "error": "Server is busy — max concurrent requests reached. Please try again shortly.",
        }), 429

    next_cursor   = None   # stays None for tools/modes that don't paginate
    source_errors = None   # multi_source_search only — {source: error} for lanes that failed this page

    try:
        if tool_type == "tweet_search_extractor":
            query = body.get("searchQuery", "")
            if mode == "cookie":
                data, next_cursor = cookie_tweet_search(query, count=count, config=config, cursor=cursor)
            else:
                data = XquikClient(config).tweet_search(query)

        elif tool_type == "follower_explorer":
            username = body.get("targetUsername", "")
            if mode == "cookie":
                data, next_cursor = cookie_follower_explorer(username, count=count, config=config, cursor=cursor)
            else:
                data = XquikClient(config).follower_explorer(username)

        elif tool_type == "following_explorer":
            username = body.get("targetUsername", "")
            if mode != "cookie":
                return jsonify({"ok": False, "error": "following_explorer requires cookie mode"}), 400
            data, next_cursor = cookie_following_explorer(username, count=count, config=config, cursor=cursor)

        elif tool_type == "article_extractor":
            tweet_id = body.get("targetTweetId", "")
            if mode == "cookie":
                data = cookie_article_extractor(tweet_id, config=config)
            else:
                data = XquikClient(config).article_extractor(tweet_id)

        elif tool_type == "community_post_extractor":
            community_id = body.get("targetCommunityId", "")
            if mode == "cookie":
                data, next_cursor = cookie_community_post_extractor(community_id, count=count, config=config, cursor=cursor)
            else:
                data = XquikClient(config).community_post_extractor(community_id)

        elif tool_type == "post_extractor":
            username = body.get("targetUsername", "")
            if mode == "cookie":
                data, next_cursor = cookie_post_extractor(username, count=count, config=config, cursor=cursor)
            else:
                data = XquikClient(config).post_extractor(username)

        elif tool_type == "tweet_replies_extractor":
            tweet_id = body.get("targetTweetId", "")
            if mode != "cookie":
                return jsonify({"ok": False, "error": "tweet_replies_extractor requires cookie mode"}), 400
            data, next_cursor = cookie_tweet_replies(tweet_id, count=count, config=config, cursor=cursor)

        elif tool_type == "tweet_retweeters_extractor":
            tweet_id = body.get("targetTweetId", "")
            if mode != "cookie":
                return jsonify({"ok": False, "error": "tweet_retweeters_extractor requires cookie mode"}), 400
            data, next_cursor = cookie_tweet_retweeters(tweet_id, count=count, config=config, cursor=cursor)

        elif tool_type == "geo_post_extractor":
            keyword = body.get("searchQuery", "")
            if mode != "cookie":
                return jsonify({"ok": False, "error": "geo_post_extractor requires cookie mode"}), 400
            data, next_cursor = cookie_geo_search(keyword, count=count, config=config, cursor=cursor)

        elif tool_type == "wayback_archive_search":
            target    = body.get("searchQuery", "")
            from_date = body.get("waybackFrom", "")
            to_date   = body.get("waybackTo", "")
            for label, val in (("waybackFrom", from_date), ("waybackTo", to_date)):
                if val and not _valid_date8(val):
                    return jsonify({"ok": False, "error": f"{label} must be an 8-digit date (YYYYMMDD)"}), 400
            data, next_cursor = wayback_search(target, count=count, from_date=from_date, to_date=to_date, cursor=cursor)

        elif tool_type == "multi_source_search":
            query     = body.get("searchQuery", "")
            from_date = body.get("dateFrom", "")
            to_date   = body.get("dateTo", "")
            for label, val in (("dateFrom", from_date), ("dateTo", to_date)):
                if val and not _valid_date8(val):
                    return jsonify({"ok": False, "error": f"{label} must be an 8-digit date (YYYYMMDD)"}), 400
            data, next_cursor, source_errors = _multi_source_search(query, count=count, from_date=from_date, to_date=to_date, cursor=cursor)

        else:
            return jsonify({"ok": False, "error": f"Unknown toolType: {tool_type}"}), 400

        # Single choke point: every tool's output passes through here, so the
        # account-age label, fetch timestamp, and tweet_url all show up
        # everywhere downstream for free — cards, graph nodes, JSON dump, and
        # archives (which now store the item's full raw shape verbatim).
        data = enrich_account_age(data)
        data = _stamp_fetched_at(data)
        data = _stamp_tweet_url(data)

        resp = {"ok": True, "data": data, "nextCursor": next_cursor}
        if source_errors:
            resp["sourceErrors"] = source_errors
        return jsonify(resp)

    except (XquikError, CookieClientError, WaybackError, GoogleCSEError) as e:
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

    # json.loads() raising here used to fall through to Flask's default
    # error handler, which returns an HTML error page — the browser's
    # res.json() then fails with an opaque "SyntaxError: JSON.parse:
    # unexpected character..." instead of the actual problem. archive.py now
    # writes both files atomically (see _atomic_write_json), so a reader
    # should never see a torn file mid-checkpoint-update; this is the
    # backstop for any other cause (disk fault, a pre-existing archive
    # written before that fix, manual editing) — always answer with clean
    # JSON either way.
    try:
        results = json.loads(results_file.read_text())
    except (json.JSONDecodeError, OSError) as e:
        return jsonify({"ok": False, "error": f"Archive data is corrupted or unreadable ({e}). Try re-running the search and archiving again."}), 500

    meta = {}
    if meta_file.exists():
        try:
            meta = json.loads(meta_file.read_text())
        except (json.JSONDecodeError, OSError):
            pass   # meta is supplementary — a corrupt/missing meta shouldn't block viewing the results that DID load fine

    return jsonify({"ok": True, "results": results, "meta": meta})


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
    body        = request.get_json(silent=True) or {}
    tool_type   = body.get("toolType", "unknown")
    data        = body.get("data")
    query_info  = body.get("queryInfo", {})
    existing_id = body.get("archiveId")   # present -> checkpoint update, not a new archive
    if not data:
        return jsonify({"ok": False, "error": "No data provided"}), 400

    if existing_id:
        if not _archive.update(existing_id, tool_type, data, query_info):
            return jsonify({"ok": False, "error": "Archive not found"}), 404
        return jsonify({"ok": True, "archiveId": existing_id})

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


# ── Analytics (sentiment / clustering) ──────────────────────────────────────
# Same background-thread + polling shape archive.py's downloads already use
# (start() kicks off a thread and returns immediately, status() reports
# progress) — ML sentiment scoring runs locally on CPU at ~11-12ms/item
# (measured), so a large archive (thousands of items) can take a minute-plus.
# A blocking request for that long leaves the browser with nothing to show
# but a static spinner and no way to tell "still working" from "stuck."

_analytics_registry: dict[str, dict] = {}   # archive_id -> job status dict
_analytics_lock = threading.Lock()


def _run_analytics(archive_id: str, items: list) -> None:
    def on_progress(done, total):
        with _analytics_lock:
            entry = _analytics_registry.get(archive_id)
            if entry is not None:   # could've been cleared/overwritten by a re-run
                entry.update({"progress": done, "total": total})

    try:
        result = _sentiment.analyze(items, on_progress=on_progress)
        with _analytics_lock:
            _analytics_registry[archive_id] = {
                "status": "done", "progress": result.get("total_scored", 0),
                "total": result.get("total_scored", 0), "result": result, "error": None,
            }
    except Exception as e:  # noqa: BLE001
        with _analytics_lock:
            _analytics_registry[archive_id] = {
                "status": "error", "progress": 0, "total": 0, "result": None, "error": str(e),
            }


@app.route("/analytics")
def analytics_viewer():
    return render_template("analytics.html")


@app.route("/api/analytics/<archive_id>/start", methods=["POST"])
def analytics_start(archive_id):
    results_file = _archive.ARCHIVE_ROOT / archive_id / "results.json"
    if not results_file.exists():
        return jsonify({"ok": False, "error": "Archive not found"}), 404
    # Same reasoning as archive_results() above — never let a bad file turn
    # into an HTML error page here either, or the browser's res.json() call
    # fails with an opaque parse error instead of a readable message.
    try:
        items = json.loads(results_file.read_text())
    except (json.JSONDecodeError, OSError) as e:
        return jsonify({"ok": False, "error": f"Archive data is corrupted or unreadable ({e}). Try re-running the search and archiving again."}), 500

    with _analytics_lock:
        _analytics_registry[archive_id] = {
            "status": "scoring", "progress": 0, "total": 0, "result": None, "error": None,
        }
    t = threading.Thread(target=_run_analytics, args=(archive_id, items), daemon=True)
    t.start()
    return jsonify({"ok": True})


@app.route("/api/analytics/<archive_id>/status")
def analytics_status(archive_id):
    with _analytics_lock:
        entry = _analytics_registry.get(archive_id)
        entry = dict(entry) if entry else None
    if entry is None:
        return jsonify({"ok": False, "error": "No analysis running for this archive — call start first"}), 404
    if entry["status"] == "error":
        return jsonify({"ok": False, "error": entry["error"]}), 500

    resp = {"ok": True, "status": entry["status"], "progress": entry["progress"], "total": entry["total"]}
    if entry["status"] == "done":
        resp.update(entry["result"])
    return jsonify(resp)


if __name__ == "__main__":
    host  = config.get("server", "host",  fallback="127.0.0.1")
    port  = config.getint("server", "port", fallback=5000)
    debug = config.getboolean("server", "debug", fallback=True)

    # Warm up the ML sentiment model in the background so the FIRST
    # analytics request doesn't pay its ~15-20s one-time load cost live —
    # see sentiment.warm_up_ml()'s docstring. Skipped in the reloader's
    # outer "monitor" process (debug mode re-execs a child process to
    # actually serve requests, setting WERKZEUG_RUN_MAIN in that child
    # only) — otherwise a process that never serves a single request would
    # load ~1GB of model weights for nothing, repeating on every autoreload
    # during dev.
    if not debug or os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        threading.Thread(target=_sentiment.warm_up_ml, daemon=True).start()

    app.run(host=host, port=port, debug=debug, threaded=True)
