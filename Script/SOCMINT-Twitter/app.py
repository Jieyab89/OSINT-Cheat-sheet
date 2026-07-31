import threading
from flask import Flask, jsonify, render_template, request

from xquik_client import XquikClient, XquikError, load_config
from cookie_client import (
    cookie_tweet_search,
    cookie_follower_explorer,
    cookie_post_extractor,
    cookie_article_extractor,
    cookie_community_post_extractor,
    CookieClientError,
)

app = Flask(__name__)
config = load_config()

MAX_CONCURRENT_REQUESTS = 3   # parallel execution slots
ACQUIRE_TIMEOUT         = 15  # seconds to wait before returning 429

_sem = threading.Semaphore(MAX_CONCURRENT_REQUESTS)


@app.route("/")
def index():
    return render_template("index.html")


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

        else:
            return jsonify({"ok": False, "error": f"Unknown toolType: {tool_type}"}), 400

        return jsonify({"ok": True, "data": data})

    except (XquikError, CookieClientError) as e:
        return jsonify({"ok": False, "error": str(e)}), 400
    except Exception as e:  # noqa: BLE001
        return jsonify({"ok": False, "error": f"Unexpected error: {e}"}), 500
    finally:
        _sem.release()


if __name__ == "__main__":
    host  = config.get("server", "host",  fallback="127.0.0.1")
    port  = config.getint("server", "port", fallback=5000)
    debug = config.getboolean("server", "debug", fallback=True)
    app.run(host=host, port=port, debug=debug, threaded=True)
