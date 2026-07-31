"""
cookie_client.py
Cookie-based wrapper for all five xquik tools, hitting X.com directly via
twikit/twifork — no xquik API quota consumed.

Install: pip install twifork
  (NOT the upstream `twikit` package — it is broken since X changed ondemand.s.js.
   twifork is a drop-in replacement; imports remain `from twikit import Client`.)

How to obtain cookies:
  1. Log in to x.com in your browser.
  2. Open DevTools > Application > Cookies > https://x.com
  3. Copy the values of `auth_token` and `ct0`.
  4. Paste them into config.ini under [twitter_cookies].
"""

import asyncio
import configparser
import os

CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.ini")


class CookieClientError(Exception):
    pass


def load_config(path: str = CONFIG_PATH) -> configparser.ConfigParser:
    cfg = configparser.ConfigParser()
    cfg.read(path)
    return cfg


def _get_creds(config: configparser.ConfigParser) -> tuple[str, str]:
    auth_token = config.get("twitter_cookies", "auth_token", fallback="").strip()
    ct0        = config.get("twitter_cookies", "ct0",        fallback="").strip()
    if not auth_token or not ct0:
        raise CookieClientError(
            "auth_token / ct0 are not set in config.ini [twitter_cookies]"
        )
    return auth_token, ct0


async def _make_client(auth_token: str, ct0: str):
    try:
        from twikit import Client
    except ImportError as e:
        raise CookieClientError(
            "Required package not installed. Run: pip install twifork  "
            "(not `twikit` — the upstream package is broken due to X's ondemand.s.js change)"
        ) from e
    client = Client(language="en-US")
    client.set_cookies({"auth_token": auth_token, "ct0": ct0})
    return client


# ── Serialisers ───────────────────────────────────────────────────────────────

def _extract_media(t: object) -> list:
    """Return [{type, thumb, url}] for each media item attached to a tweet."""
    result = []
    for m in getattr(t, "media", None) or []:
        mtype = getattr(m, "type", "photo")
        thumb = (
            getattr(m, "media_url_https", None)
            or getattr(m, "media_url", None)
            or getattr(m, "url", None)
        )
        if not thumb:
            continue
        url = thumb
        if mtype in ("video", "animated_gif"):
            vid = getattr(m, "video_info", None)
            if isinstance(vid, dict):
                mp4s = [
                    v for v in vid.get("variants", [])
                    if isinstance(v, dict) and v.get("content_type") == "video/mp4"
                ]
                if mp4s:
                    url = max(mp4s, key=lambda v: v.get("bitrate", 0)).get("url", thumb)
        result.append({"type": mtype, "thumb": thumb, "url": url})
    return result


def _tweet_to_dict(t: object) -> dict:
    d = {
        "id":             getattr(t, "id", None),
        "created_at":     getattr(t, "created_at", None),
        "text":           getattr(t, "text", None),
        "user":           getattr(t.user, "screen_name", None) if getattr(t, "user", None) else None,
        "reply_count":    getattr(t, "reply_count", None),
        "retweet_count":  getattr(t, "retweet_count", None),
        "favorite_count": getattr(t, "favorite_count", None),
        "view_count":     getattr(t, "view_count", None),
    }
    media = _extract_media(t)
    if media:
        d["media"] = media
    return d


def _user_to_dict(u: object) -> dict:
    return {
        "id":               getattr(u, "id", None),
        "name":             getattr(u, "name", None),
        "screen_name":      getattr(u, "screen_name", None),
        "description":      getattr(u, "description", None),
        "followers_count":  getattr(u, "followers_count", None),
        "following_count":  getattr(u, "following_count", None),
        "tweet_count":      getattr(u, "statuses_count", None),
        "created_at":       getattr(u, "created_at", None),
        "verified":         getattr(u, "verified", None),
        "is_blue_verified": getattr(u, "is_blue_verified", None),
    }


# ── Async implementations ─────────────────────────────────────────────────────

async def _tweet_search_async(query: str, auth_token: str, ct0: str, count: int) -> list:
    client  = await _make_client(auth_token, ct0)
    results = await client.search_tweet(query, "Latest", count=count)
    return [_tweet_to_dict(t) for t in results]


async def _follower_explorer_async(username: str, auth_token: str, ct0: str, count: int) -> list:
    client    = await _make_client(auth_token, ct0)
    user      = await client.get_user_by_screen_name(username)
    followers = await user.get_followers(count=count)
    return [_user_to_dict(u) for u in followers]


async def _post_extractor_async(username: str, auth_token: str, ct0: str, count: int) -> list:
    client = await _make_client(auth_token, ct0)
    user   = await client.get_user_by_screen_name(username)
    tweets = await user.get_tweets("Tweets", count=count)
    return [_tweet_to_dict(t) for t in tweets]


async def _article_extractor_async(tweet_id: str, auth_token: str, ct0: str) -> dict:
    client = await _make_client(auth_token, ct0)
    tweet  = await client.get_tweet_by_id(tweet_id)
    result = _tweet_to_dict(tweet)
    note   = getattr(tweet, "note_tweet", None)
    if note:
        result["article_text"] = note
    card = getattr(tweet, "card", None)
    if card:
        result["card"] = str(card)
    return result


async def _community_posts_async(community_id: str, auth_token: str, ct0: str, count: int) -> list:
    client = await _make_client(auth_token, ct0)
    posts  = await client.get_community_tweets(community_id, "Latest", count=count)
    return [_tweet_to_dict(t) for t in posts]


# ── Public sync wrappers ──────────────────────────────────────────────────────

def cookie_tweet_search(query: str, count: int = 20, config: configparser.ConfigParser = None) -> list:
    cfg = config or load_config()
    auth, ct0 = _get_creds(cfg)
    return asyncio.run(_tweet_search_async(query, auth, ct0, count))


def cookie_follower_explorer(username: str, count: int = 20, config: configparser.ConfigParser = None) -> list:
    cfg = config or load_config()
    auth, ct0 = _get_creds(cfg)
    return asyncio.run(_follower_explorer_async(username, auth, ct0, count))


def cookie_post_extractor(username: str, count: int = 20, config: configparser.ConfigParser = None) -> list:
    cfg = config or load_config()
    auth, ct0 = _get_creds(cfg)
    return asyncio.run(_post_extractor_async(username, auth, ct0, count))


def cookie_article_extractor(tweet_id: str, config: configparser.ConfigParser = None) -> dict:
    cfg = config or load_config()
    auth, ct0 = _get_creds(cfg)
    return asyncio.run(_article_extractor_async(tweet_id, auth, ct0))


def cookie_community_post_extractor(
    community_id: str, count: int = 20, config: configparser.ConfigParser = None
) -> list:
    cfg = config or load_config()
    auth, ct0 = _get_creds(cfg)
    return asyncio.run(_community_posts_async(community_id, auth, ct0, count))


# Legacy alias — kept for any external scripts that import this name directly
fetch_user_timeline = cookie_post_extractor


# ── CLI entry-point ───────────────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Cookie-based X data extraction CLI")
    sub    = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("tweet_search").add_argument("query")

    p = sub.add_parser("follower_explorer")
    p.add_argument("username")
    p.add_argument("--count", type=int, default=20)

    p = sub.add_parser("post_extractor")
    p.add_argument("username")
    p.add_argument("--count", type=int, default=20)

    sub.add_parser("article_extractor").add_argument("tweet_id")

    p = sub.add_parser("community_post_extractor")
    p.add_argument("community_id")
    p.add_argument("--count", type=int, default=20)

    args = parser.parse_args()
    try:
        if args.cmd == "tweet_search":
            out = cookie_tweet_search(args.query)
        elif args.cmd == "follower_explorer":
            out = cookie_follower_explorer(args.username, count=args.count)
        elif args.cmd == "post_extractor":
            out = cookie_post_extractor(args.username, count=args.count)
        elif args.cmd == "article_extractor":
            out = cookie_article_extractor(args.tweet_id)
        elif args.cmd == "community_post_extractor":
            out = cookie_community_post_extractor(args.community_id, count=args.count)
        print(json.dumps(out, indent=2, ensure_ascii=False))
    except CookieClientError as e:
        print(f"[ERROR] {e}")
        raise SystemExit(1)
