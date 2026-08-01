import json
import os
import random
import threading
import time
from datetime import datetime
from pathlib import Path

import requests

ARCHIVE_ROOT   = Path(__file__).parent / "archives"
DELAY_MIN      = 1.5   # seconds between media downloads (anti-ban)
DELAY_MAX      = 3.5
REQUEST_TIMEOUT = 25

_registry: dict[str, dict] = {}   # archive_id → status dict
_lock = threading.Lock()


# ── Helpers ───────────────────────────────────────────────────────────────────

def _make_id(tool_type: str) -> str:
    return f"{tool_type}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"


def _tweet_url(item: dict) -> str | None:
    tid  = str(item.get("id", "")).strip()
    user = str(item.get("user", "")).strip()
    if tid and user:
        return f"https://x.com/{user}/status/{tid}"
    return None


def _media_ext(url: str, mtype: str) -> str:
    if mtype in ("video", "animated_gif"):
        return "mp4"
    for ext in (".jpg", ".jpeg", ".png", ".webp", ".gif"):
        if ext in url.lower():
            return ext.lstrip(".")
    return "jpg"


def _download_file(url: str, dest: Path) -> bool:
    """Download a single file. Returns True on success."""
    try:
        r = requests.get(
            url,
            timeout=REQUEST_TIMEOUT,
            headers={"Referer": "https://x.com/", "User-Agent": "Mozilla/5.0"},
            stream=True,
        )
        r.raise_for_status()
        dest.parent.mkdir(parents=True, exist_ok=True)
        with open(dest, "wb") as f:
            for chunk in r.iter_content(chunk_size=65536):
                f.write(chunk)
        return True
    except Exception:
        return False


def _pick_fields(item: dict) -> dict:
    """Keep only the fields we want to archive."""
    keys = ["id", "text", "full_text", "article_text", "user", "user_id",
            "created_at", "reply_count", "retweet_count", "favorite_count",
            "view_count", "in_reply_to_tweet_id", "name", "screen_name",
            "verified", "is_blue_verified",
            "description", "followers_count", "following_count", "tweet_count",
            "lat", "lon", "place",
            "retweeted_text", "retweeted_by_user", "retweeted_by_name",
            "retweeted_by_bio", "retweeted_at", "retweeted_tweet_id",
            "iso_date", "original", "statuscode", "mimetype", "length",
            "archive_url", "post_title", "post_text", "preview_image",
            "source", "account_created", "account_age", "account_age_flag",
            "account_age_precision"]
    return {k: item[k] for k in keys if k in item and item[k] is not None}


# ── Core archive runner (runs in background thread) ───────────────────────────

def _run(archive_id: str, tool_type: str, data, query_info: dict) -> None:
    archive_dir = ARCHIVE_ROOT / archive_id
    media_dir   = archive_dir / "media"
    archive_dir.mkdir(parents=True, exist_ok=True)
    media_dir.mkdir(exist_ok=True)

    items = data if isinstance(data, list) else [data]

    # Build enriched records + collect media download queue
    enriched     = []
    media_queue  = []   # list of (url, dest_path)

    for item in items:
        if not isinstance(item, dict):
            enriched.append(item)
            continue

        record              = _pick_fields(item)
        record["tweet_url"] = _tweet_url(item)
        local_media         = []

        for midx, m in enumerate(item.get("media", [])):
            url  = m.get("url") or m.get("thumb", "")
            if not url:
                continue
            mtype = m.get("type", "photo")
            ext   = _media_ext(url, mtype)
            fname = f"{item.get('id', 'unknown')}_{mtype}_{midx}.{ext}"
            dest  = media_dir / fname
            local_media.append(f"media/{fname}")
            # Skip re-downloading media that's already on disk — matters for
            # checkpoint updates, which re-run this on a growing dataset that
            # mostly overlaps with what was already archived.
            if not dest.exists():
                media_queue.append((url, dest))

        if local_media:
            record["archived_media"] = local_media
        enriched.append(record)

    # Preserve the original archived_at across checkpoint updates (re-runs
    # of this on an archive_id that already exists) rather than overwriting it.
    meta_path     = archive_dir / "meta.json"
    existing_meta = {}
    if meta_path.exists():
        try:
            existing_meta = json.loads(meta_path.read_text())
        except Exception:
            existing_meta = {}

    now_iso     = datetime.now().isoformat(timespec="seconds")
    total_media = sum(len(r.get("archived_media", [])) for r in enriched if isinstance(r, dict))

    # Write metadata + results immediately (no waiting on media)
    meta = {
        "tool":        tool_type,
        "query":       query_info,
        "archived_at": existing_meta.get("archived_at", now_iso),
        "updated_at":  now_iso,
        "total_items": len(items),
        "media_count": total_media,
    }
    meta_path.write_text(
        json.dumps(meta, indent=2, ensure_ascii=False)
    )
    (archive_dir / "results.json").write_text(
        json.dumps(enriched, indent=2, ensure_ascii=False)
    )

    with _lock:
        _registry[archive_id].update({"status": "downloading", "total": len(media_queue)})

    # Download media one-by-one with anti-ban delays
    for i, (url, dest) in enumerate(media_queue):
        if i > 0:
            time.sleep(random.uniform(DELAY_MIN, DELAY_MAX))
        _download_file(url, dest)
        with _lock:
            _registry[archive_id]["progress"] = i + 1

    with _lock:
        _registry[archive_id].update({"status": "done", "path": str(archive_dir)})


# ── Public API ────────────────────────────────────────────────────────────────

def start(tool_type: str, data, query_info: dict) -> str:
    """Kick off archiving in a background thread. Returns archive_id."""
    archive_id = _make_id(tool_type)
    with _lock:
        _registry[archive_id] = {"status": "saving", "progress": 0, "total": 0, "path": None}

    t = threading.Thread(
        target=_run,
        args=(archive_id, tool_type, data, query_info),
        daemon=True,
    )
    t.start()
    return archive_id


def update(archive_id: str, tool_type: str, data, query_info: dict) -> bool:
    """Re-run the archive pipeline against an EXISTING archive_id — the
    "save checkpoint" flow, used once scroll/expand-load-more has fetched
    more data than what was first archived. Overwrites results.json/meta.json
    with the current (larger) dataset; media already on disk is skipped
    rather than re-downloaded. Returns False if archive_id doesn't exist."""
    archive_dir = ARCHIVE_ROOT / archive_id
    if not archive_dir.exists():
        return False

    with _lock:
        _registry[archive_id] = {"status": "saving", "progress": 0, "total": 0, "path": None}

    t = threading.Thread(
        target=_run,
        args=(archive_id, tool_type, data, query_info),
        daemon=True,
    )
    t.start()
    return True


def status(archive_id: str) -> dict | None:
    with _lock:
        entry = _registry.get(archive_id)
        return dict(entry) if entry else None


def list_all() -> list[dict]:
    """Read meta.json from every archive folder, newest first — sorted by the
    archive's own archived_at/updated_at timestamp, not folder name. Folder
    names are prefixed by tool_type (e.g. "graph_tweet_search_..." vs
    "tweet_search_..."), so sorting by name doesn't actually sort
    chronologically once more than one tool has been archived. A checkpoint
    update bumps updated_at, so it resurfaces near the top too."""
    if not ARCHIVE_ROOT.exists():
        return []
    results = []
    for d in ARCHIVE_ROOT.iterdir():
        meta_file = d / "meta.json"
        if not meta_file.exists():
            continue
        try:
            meta       = json.loads(meta_file.read_text())
            meta["id"] = d.name
            results.append(meta)
        except Exception:
            pass
    results.sort(key=lambda m: m.get("updated_at") or m.get("archived_at") or "", reverse=True)
    return results
