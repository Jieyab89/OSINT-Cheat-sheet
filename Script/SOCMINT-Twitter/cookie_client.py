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


def _id_str(val) -> str | None:
    """Return ID as string, or None. Prevents 64-bit integer precision loss in JSON/JS."""
    return str(val) if val is not None else None


def _full_text(t: object) -> str | None:
    """twikit's `.text` is Twitter's own legacy `full_text` field — despite the
    name, X still truncates *that* mid-sentence into a t.co link for anything
    past the classic length limit (long-form "Note" tweets, e.g. Premium/Blue
    posts). twikit's `.full_text` PROPERTY (a different thing from the legacy
    field of the same name) checks the tweet's note_tweet payload first and
    returns the real complete text when one exists, falling back to `.text`
    itself otherwise — so it's always at least as complete, strictly more so
    for long tweets. Swallows a malformed note_tweet shape rather than letting
    one tweet's data take down the whole batch."""
    try:
        return getattr(t, "full_text", None)
    except Exception:
        return None


def _hashtags(t: object) -> list | None:
    """Same note_tweet-aware source as _full_text — a long-form tweet's
    hashtags live in the note_tweet entity set, not the legacy entities twikit
    falls back to otherwise."""
    try:
        tags = getattr(t, "hashtags", None)
        return tags or None
    except Exception:
        return None


def _leading_reply_mentions(t: object) -> list | None:
    """Tapping "Reply" on X auto-prefixes the compose box with every account
    the reply-chain already has tagged — not just the tweet being replied to
    — and that prefix is genuinely stored as the literal start of the
    reply's own full_text. X's own web/app UI never shows it inline though:
    it reads `display_text_range` (the slice of full_text actually meant to
    be *shown*) and renders anything before that start index as a separate
    "Replying to @x @y" line instead. Skipping this meant our raw `text`
    looked like the replier had typed those @mentions themselves — e.g. a
    reply that only ever says "Proyek kepentingan, bukan untuk rakyat..."
    displayed as if it opened with "@regar_op0sisi @prabowo ...", which is
    exactly what looked wrong compared to the tweet on x.com. This only
    covers the un-extended legacy text/entities — a long-form Note tweet's
    entity indices belong to its own separate note_tweet string, which this
    intentionally does not touch rather than risk slicing the wrong string.
    Reads twikit's private `_legacy`/`_note_tweet_results` (no public
    equivalent exists) — same trade-off already made for `_get_more_replies`
    elsewhere in this file. Returns None rather than raising on any
    unexpected shape, since this is purely a display aid, never the record
    of truth `text` already is."""
    try:
        if t._note_tweet_results:
            return None
        legacy = t._legacy
        start  = (legacy.get("display_text_range") or [0])[0]
        if not start:
            return None
        names = []
        for m in (legacy.get("entities") or {}).get("user_mentions", []) or []:
            idx = m.get("indices") or [None, None]
            if idx[0] is not None and idx[1] is not None and idx[1] <= start:
                sn = m.get("screen_name")
                if sn:
                    names.append(sn)
        return names or None
    except Exception:
        return None


def _quoted_tweet_fields(t: object) -> dict | None:
    """When `t` is a quote-tweet (retweeted-with-comment), the ORIGINAL post
    being quoted — the thing X's own UI renders as a nested card below the
    quoting user's own commentary. `t.text`/`.full_text` on the outer dict is
    already that commentary; this is what the commentary is ON. Distinct
    from a plain retweet (no added text of its own, and not surfaced as a
    separate quote card by X) and from `_tweet_retweeters_async`'s "who
    retweeted this" feature below, which walks the opposite direction
    (retweeters of one already-known tweet id, not quotes discovered while
    listing tweets normally — search, timeline, replies, community, geo).
    Swallows any twikit-shape surprise the same way _full_text/_hashtags do
    — a missing quote is just no quote, never worth failing the whole
    record over."""
    try:
        if not getattr(t, "is_quote_status", False):
            return None
        quoted = getattr(t, "quote", None)
        if quoted is None:
            return None
        quoted_user = getattr(quoted, "user", None)
        return {
            "quoted_text":     _full_text(quoted) or getattr(quoted, "text", None),
            "quoted_user":     getattr(quoted_user, "screen_name", None) if quoted_user else None,
            "quoted_name":     getattr(quoted_user, "name", None) if quoted_user else None,
            "quoted_at":       getattr(quoted, "created_at", None),
            "quoted_tweet_id": _id_str(getattr(quoted, "id", None)),
        }
    except Exception:
        return None


def _tweet_to_dict(t: object) -> dict:
    user_obj = getattr(t, "user", None)
    d = {
        "id":             _id_str(getattr(t, "id", None)),
        "created_at":     getattr(t, "created_at", None),
        "text":           _full_text(t) or getattr(t, "text", None),
        "user":           getattr(user_obj, "screen_name", None) if user_obj else None,
        "user_id":        _id_str(getattr(user_obj, "id", None)) if user_obj else None,
        "user_location":  getattr(user_obj, "location", None) if user_obj else None,
        # Display name + verification badge — Twitter's own reply UI shows both
        # next to the handle; twikit already exposes them on the tweet's user.
        "name":                 getattr(user_obj, "name", None) if user_obj else None,
        "verified":             getattr(user_obj, "verified", None) if user_obj else None,
        "is_blue_verified":     getattr(user_obj, "is_blue_verified", None) if user_obj else None,
        # Author's avatar/cover/bio — twikit's embedded user object on a tweet
        # already carries these, no extra lookup needed.
        "user_avatar":          getattr(user_obj, "profile_image_url", None) if user_obj else None,
        "user_banner":          getattr(user_obj, "profile_banner_url", None) if user_obj else None,
        "user_bio":             getattr(user_obj, "description", None) if user_obj else None,
        "reply_count":          getattr(t, "reply_count", None),
        "retweet_count":        getattr(t, "retweet_count", None),
        "favorite_count":       getattr(t, "favorite_count", None),
        "view_count":           getattr(t, "view_count", None),
        "in_reply_to_tweet_id": getattr(t, "in_reply_to", None),  # returns id_str directly
    }
    media = _extract_media(t)
    if media:
        d["media"] = media
    tags = _hashtags(t)
    if tags:
        d["hashtags"] = tags
    mentions = _leading_reply_mentions(t)
    if mentions:
        d["reply_to_mentions"] = mentions
    quote = _quoted_tweet_fields(t)
    if quote:
        d.update(quote)
    return d


def _user_to_dict(u: object) -> dict:
    return {
        "id":               _id_str(getattr(u, "id", None)),
        "name":             getattr(u, "name", None),
        "screen_name":      getattr(u, "screen_name", None),
        "description":      getattr(u, "description", None),
        "avatar":           getattr(u, "profile_image_url", None),
        "banner":           getattr(u, "profile_banner_url", None),
        "followers_count":  getattr(u, "followers_count", None),
        "following_count":  getattr(u, "following_count", None),
        "tweet_count":      getattr(u, "statuses_count", None),
        "created_at":       getattr(u, "created_at", None),
        "verified":         getattr(u, "verified", None),
        "is_blue_verified": getattr(u, "is_blue_verified", None),
    }


# ── Async implementations ─────────────────────────────────────────────────────

async def _resolve_user(client, identifier: str):
    """Accept either a screen_name or a numeric user ID string."""
    clean = identifier.lstrip("@").strip()
    if clean.isdigit():
        return await client.get_user_by_id(clean)
    return await client.get_user_by_screen_name(clean)


def _next_cursor(result) -> str | None:
    """A zero-item page always means "exhausted," regardless of what cursor
    value twikit hands back — avoids chasing a stale/looping cursor."""
    if not len(result):
        return None
    return getattr(result, "next_cursor", None) or None


async def _tweet_search_async(query: str, auth_token: str, ct0: str, count: int, cursor: str | None) -> tuple[list, str | None]:
    client  = await _make_client(auth_token, ct0)
    results = await client.search_tweet(query, "Latest", count=count, cursor=cursor)
    return [_tweet_to_dict(t) for t in results], _next_cursor(results)


async def _follower_explorer_async(username: str, auth_token: str, ct0: str, count: int, cursor: str | None) -> tuple[list, str | None]:
    client    = await _make_client(auth_token, ct0)
    user      = await _resolve_user(client, username)
    # Bypass the User.get_followers() convenience wrapper — it doesn't accept
    # a cursor at all, so it can't be resumed across requests.
    followers = await client.get_user_followers(str(user.id), count=count, cursor=cursor)
    return [_user_to_dict(u) for u in followers], _next_cursor(followers)


async def _following_explorer_async(username: str, auth_token: str, ct0: str, count: int, cursor: str | None) -> tuple[list, str | None]:
    """Who `username` follows — the other half of follower_explorer. twikit
    exposes this as Client.get_user_following, same shape/cursor contract as
    get_user_followers, so this mirrors _follower_explorer_async exactly."""
    client    = await _make_client(auth_token, ct0)
    user      = await _resolve_user(client, username)
    following = await client.get_user_following(str(user.id), count=count, cursor=cursor)
    return [_user_to_dict(u) for u in following], _next_cursor(following)


async def _post_extractor_async(username: str, auth_token: str, ct0: str, count: int, cursor: str | None) -> tuple[list, str | None]:
    client = await _make_client(auth_token, ct0)
    user   = await _resolve_user(client, username)
    # Bypass User.get_tweets() for the same reason as followers above.
    tweets = await client.get_user_tweets(str(user.id), "Tweets", count=count, cursor=cursor)
    return [_tweet_to_dict(t) for t in tweets], _next_cursor(tweets)


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


async def _community_posts_async(community_id: str, auth_token: str, ct0: str, count: int, cursor: str | None) -> tuple[list, str | None]:
    client = await _make_client(auth_token, ct0)
    posts  = await client.get_community_tweets(community_id, "Latest", count=count, cursor=cursor)
    return [_tweet_to_dict(t) for t in posts], _next_cursor(posts)


async def _tweet_replies_async(tweet_id: str, auth_token: str, ct0: str, count: int, cursor: str | None) -> tuple[list, str | None]:
    """Direct top-level replies to `tweet_id`, fetched via the same GraphQL
    TweetDetail call that powers Twitter's own UI reply view — not a keyword
    search. `search_tweet(f"conversation_id:...")` was tried first, but it
    caps out around ~20 raw results with no way to page further regardless
    of the requested count, and mixes in replies-to-replies from anywhere in
    the thread (a 29-reply post returned 20 raw items with only 3 actually
    replying to the target). TweetDetail already separates "direct replies to
    this exact tweet" cleanly and supports proper cursor pagination.

    `count` is advisory only here — `get_tweet_by_id` has no page-size knob,
    X's TweetDetail backend decides how many replies come back per page. We
    return the page whole rather than slicing to `count`: once the cursor is
    handed back to the caller for real cross-request resumption, slicing
    would permanently strand whatever got cut (the cursor already points
    past those rows). Getting the rest is what the next paginated request
    (scroll / expand-again) is for, not a bigger `count`.

    Continuation pages need a different call than the first page: X's
    TweetDetail response for a cursor-based request does NOT include the
    root tweet's own entry (only reply entries + a trailing cursor), but
    `get_tweet_by_id` unconditionally requires finding that entry — passing
    it a cursor beyond page 1 raises `AttributeError: 'NoneType' object has
    no attribute 'replies'` (confirmed empirically). `Client._get_more_replies`
    is twikit's own handler for exactly this response shape — it's what
    `Result.next()` calls internally — so we call it directly for page 2+.
    It's a private method (fragile to twikit internals changing), but
    there's no public equivalent for resuming pagination across a fresh
    request/session rather than an in-memory `Result` object.
    """
    client = await _make_client(auth_token, ct0)
    if cursor:
        replies = await client._get_more_replies(tweet_id, cursor)
    else:
        tweet   = await client.get_tweet_by_id(tweet_id)
        replies = tweet.replies
    return [_tweet_to_dict(t) for t in replies], _next_cursor(replies)


async def _tweet_retweeters_async(tweet_id: str, auth_token: str, ct0: str, count: int, cursor: str | None) -> tuple[list, str | None]:
    client = await _make_client(auth_token, ct0)

    # Fetch the original tweet once so every retweeter card shows what was retweeted
    rt_info: dict = {}
    try:
        orig      = await client.get_tweet_by_id(tweet_id)
        orig_user = getattr(orig, "user", None)
        rt_info = {
            "retweeted_text":        getattr(orig, "text", None),
            "retweeted_by_user":     getattr(orig_user, "screen_name", None) if orig_user else None,
            "retweeted_by_name":     getattr(orig_user, "name", None) if orig_user else None,
            "retweeted_by_bio":      getattr(orig_user, "description", None) if orig_user else None,
            "retweeted_at":          getattr(orig, "created_at", None),
            "retweeted_tweet_id":    _id_str(getattr(orig, "id", None)),
        }
        # The retweeted tweet can itself be a quote-tweet — surface what IT
        # quoted too, same fields _tweet_to_dict adds for a quote found
        # anywhere else, so a retweeters card is never missing context a
        # search/timeline card for the same tweet would have shown.
        quote = _quoted_tweet_fields(orig)
        if quote:
            rt_info.update(quote)
    except Exception:
        pass

    retweeters = await client.get_retweeters(tweet_id, count=count, cursor=cursor)

    result = []
    for u in retweeters:
        # retweeted content first → shows prominently in the card
        d = {**rt_info, **_user_to_dict(u)}
        result.append(d)
    return result, _next_cursor(retweeters)


async def _geo_search_async(keyword: str, auth_token: str, ct0: str, count: int, cursor: str | None) -> tuple[list, str | None]:
    """Keyword search; user_location (profile location string) is included in every
    result so the frontend can geocode and plot it on a map."""
    client  = await _make_client(auth_token, ct0)
    results = await client.search_tweet(keyword, "Latest", count=count, cursor=cursor)
    return [_tweet_to_dict(t) for t in results], _next_cursor(results)


# ── Public sync wrappers ──────────────────────────────────────────────────────
# Each pagination-capable wrapper returns (items, next_cursor). Pass the
# previous response's next_cursor back in as `cursor` to fetch the next page;
# `next_cursor` is None once there's nothing more to load.

def cookie_tweet_search(query: str, count: int = 20, config: configparser.ConfigParser = None, cursor: str | None = None) -> tuple[list, str | None]:
    cfg = config or load_config()
    auth, ct0 = _get_creds(cfg)
    return asyncio.run(_tweet_search_async(query, auth, ct0, count, cursor))


def cookie_follower_explorer(username: str, count: int = 20, config: configparser.ConfigParser = None, cursor: str | None = None) -> tuple[list, str | None]:
    cfg = config or load_config()
    auth, ct0 = _get_creds(cfg)
    return asyncio.run(_follower_explorer_async(username, auth, ct0, count, cursor))


def cookie_following_explorer(username: str, count: int = 20, config: configparser.ConfigParser = None, cursor: str | None = None) -> tuple[list, str | None]:
    cfg = config or load_config()
    auth, ct0 = _get_creds(cfg)
    return asyncio.run(_following_explorer_async(username, auth, ct0, count, cursor))


def cookie_post_extractor(username: str, count: int = 20, config: configparser.ConfigParser = None, cursor: str | None = None) -> tuple[list, str | None]:
    cfg = config or load_config()
    auth, ct0 = _get_creds(cfg)
    return asyncio.run(_post_extractor_async(username, auth, ct0, count, cursor))


def cookie_article_extractor(tweet_id: str, config: configparser.ConfigParser = None) -> dict:
    cfg = config or load_config()
    auth, ct0 = _get_creds(cfg)
    return asyncio.run(_article_extractor_async(tweet_id, auth, ct0))


def cookie_community_post_extractor(
    community_id: str, count: int = 20, config: configparser.ConfigParser = None, cursor: str | None = None
) -> tuple[list, str | None]:
    cfg = config or load_config()
    auth, ct0 = _get_creds(cfg)
    return asyncio.run(_community_posts_async(community_id, auth, ct0, count, cursor))


def cookie_tweet_replies(tweet_id: str, count: int = 50, config: configparser.ConfigParser = None, cursor: str | None = None) -> tuple[list, str | None]:
    cfg = config or load_config()
    auth, ct0 = _get_creds(cfg)
    return asyncio.run(_tweet_replies_async(tweet_id, auth, ct0, count, cursor))


def cookie_tweet_retweeters(tweet_id: str, count: int = 50, config: configparser.ConfigParser = None, cursor: str | None = None) -> tuple[list, str | None]:
    cfg = config or load_config()
    auth, ct0 = _get_creds(cfg)
    return asyncio.run(_tweet_retweeters_async(tweet_id, auth, ct0, count, cursor))


def cookie_geo_search(
    keyword: str, count: int = 20, config: configparser.ConfigParser = None, cursor: str | None = None,
) -> tuple[list, str | None]:
    cfg = config or load_config()
    auth, ct0 = _get_creds(cfg)
    return asyncio.run(_geo_search_async(keyword, auth, ct0, count, cursor))


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
            out, _ = cookie_tweet_search(args.query)
        elif args.cmd == "follower_explorer":
            out, _ = cookie_follower_explorer(args.username, count=args.count)
        elif args.cmd == "post_extractor":
            out, _ = cookie_post_extractor(args.username, count=args.count)
        elif args.cmd == "article_extractor":
            out = cookie_article_extractor(args.tweet_id)
        elif args.cmd == "community_post_extractor":
            out, _ = cookie_community_post_extractor(args.community_id, count=args.count)
        print(json.dumps(out, indent=2, ensure_ascii=False))
    except CookieClientError as e:
        print(f"[ERROR] {e}")
        raise SystemExit(1)
