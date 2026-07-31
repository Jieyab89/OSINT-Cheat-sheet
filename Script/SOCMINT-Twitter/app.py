import json
import secrets
import shutil
import threading
import requests as _req
from flask import Flask, g, jsonify, render_template, request, Response, stream_with_context, send_from_directory

import archive as _archive
from xquik_client import XquikClient, XquikError, load_config
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

        else:
            return jsonify({"ok": False, "error": f"Unknown toolType: {tool_type}"}), 400

        return jsonify({"ok": True, "data": data})

    except (XquikError, CookieClientError) as e:
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
