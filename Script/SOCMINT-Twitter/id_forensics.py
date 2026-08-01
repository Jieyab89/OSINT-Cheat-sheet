"""Best-effort forensics on Twitter/X's numeric account IDs.

Tweet IDs have been Snowflake-encoded (a millisecond timestamp packed into
the high bits of the 64-bit integer) since Twitter adopted the scheme in
~Nov 2010 — decoding one is exact. User IDs are a different story: Twitter
kept assigning them as plain sequential auto-increment integers for years
*after* tweet IDs went Snowflake, and only switched new accounts over to
real Snowflake-style user ids much later. Concretely, in this tool's own
test data: an account created 2015-08-18 (per Twitter's own record) has
user_id 3,319,260,420 — a 10-digit sequential number, nowhere near the
~10^17+ magnitude a Snowflake id from that date would need to have. Trying
to bit-shift-decode ids in that sequential era would silently produce a
bogus date (this happened during development: id 13,418,472, a real 2008
account, decoded as "2010-11-04" — the Snowflake epoch instant — before
this was caught and fixed).

So this module reports creation time at one of three confidence levels:

  exact      - id is unambiguously in the Snowflake range -> bit-shifted
               straight out of the id, precise to the millisecond.
  estimated  - id falls in the pre-Snowflake sequential range -> a rough
               era is interpolated from two real accounts whose creation
               dates were verified against Twitter's own API during actual
               use of this tool (see _CAL_LOW / _CAL_HIGH below). This is
               a genuine estimate, not a decode, and is always labeled as
               such — never presented as if it were precise.
  unknown    - id doesn't fall cleanly into either range (a gap we have no
               calibration data for, roughly 2015-era-volume up to the
               point new accounts started getting true Snowflake ids) ->
               reported as unknown rather than guessed.

X/Twitter exposes no public "account history" API the way GitHub or
Facebook do, so this — plus external correlation via Wayback Machine
snapshots of the same id over time — is the only way to forensically
establish an account's real age from data alone.
"""

import math
from datetime import datetime, timedelta, timezone

TWITTER_EPOCH_MS = 1288834974657   # 2010-11-04T01:42:54.657Z — Snowflake's custom epoch

# Ids at/above this are unambiguously true Snowflake ids: a genuine Snowflake
# id already exceeds 10^13 within ~40 minutes of the epoch (it grows by 2^22
# per millisecond), while real sequential-era user ids never got anywhere
# close to 10^13 (Twitter had on the order of a few hundred million accounts
# total during that whole era). Wide, safe gap between the two regimes.
_MIN_SNOWFLAKE_ID = 10 ** 13

# Calibration anchors for the pre-Snowflake sequential era — real accounts,
# creation dates verified against Twitter's own API response during actual
# use of this tool. Used to log-linearly interpolate a *rough* era estimate
# for ids that fall between them. Deliberately not extrapolated beyond this
# range: Twitter's early growth rate was too uneven to guess responsibly
# from just two points.
_CAL_LOW_ID,  _CAL_LOW_DT  = 13_418_472,    datetime(2008, 2, 13, tzinfo=timezone.utc)   # @willywoo
_CAL_HIGH_ID, _CAL_HIGH_DT = 3_319_260_420, datetime(2015, 8, 18, tzinfo=timezone.utc)   # @geloraco


def decode_snowflake(id_value) -> datetime | None:
    """Exact decode. Returns the UTC creation datetime embedded in a genuine
    Snowflake id, or None if the value isn't unambiguously one."""
    n = _as_int(id_value)
    if n is None or n < _MIN_SNOWFLAKE_ID:
        return None

    ts_ms = (n >> 22) + TWITTER_EPOCH_MS
    try:
        dt = datetime.fromtimestamp(ts_ms / 1000, tz=timezone.utc)
    except (OverflowError, OSError, ValueError):
        return None

    if dt > datetime.now(timezone.utc):
        return None
    return dt


def estimate_sequential_era(id_value) -> datetime | None:
    """Rough estimate for ids in the pre-Snowflake sequential range, via
    log-linear interpolation between the two calibration anchors. Returns
    None for ids outside [_CAL_LOW_ID, _CAL_HIGH_ID] — no extrapolation."""
    n = _as_int(id_value)
    if n is None or n < _CAL_LOW_ID or n > _CAL_HIGH_ID:
        return None

    frac = (math.log10(n) - math.log10(_CAL_LOW_ID)) / (math.log10(_CAL_HIGH_ID) - math.log10(_CAL_LOW_ID))
    span = (_CAL_HIGH_DT - _CAL_LOW_DT).total_seconds()
    return _CAL_LOW_DT + timedelta(seconds=span * frac)


def _as_int(id_value):
    try:
        return int(str(id_value).strip())
    except (TypeError, ValueError):
        return None


def humanize_age(dt: datetime) -> str:
    days = (datetime.now(timezone.utc) - dt).days
    if days < 1:
        return "today"
    if days < 30:
        return f"{days} day{'s' if days != 1 else ''} ago"
    if days < 365:
        months = days // 30
        return f"{months} month{'s' if months != 1 else ''} ago"
    years  = days // 365
    months = (days % 365) // 30
    suffix = f" {months} month{'s' if months != 1 else ''}" if months else ""
    return f"{years} year{'s' if years != 1 else ''}{suffix} ago"


def age_flag(dt: datetime) -> str:
    """Coarse bucket used for the "is this an old account" label — the
    <30-day bucket in particular is a classic bot/sockpuppet signal. Coarse
    enough (years, not days) that estimated dates still bucket reliably."""
    days = (datetime.now(timezone.utc) - dt).days
    if days < 30:
        return "new"
    if days < 365:
        return "recent"
    return "established"


def _account_id_for(item: dict):
    """Which field holds the *account's own* numeric ID for this item shape."""
    if item.get("user_id"):
        return item["user_id"]
    # User-shaped records (follower_explorer, retweeters, ...) carry the
    # account's own id directly in `id` — identified by a field only users have.
    if item.get("id") and ("screen_name" in item or "followers_count" in item):
        return item["id"]
    return None


def enrich_account_age(data):
    """Mutates every dict in `data` (list or single dict) in place, adding
    account_created / account_age / account_age_flag / account_age_precision
    wherever a usable account id is present. No-op for items with no such id
    (e.g. Wayback snapshot rows, which carry no numeric account id at all)."""
    items = data if isinstance(data, list) else [data]
    for item in items:
        if not isinstance(item, dict):
            continue
        acc_id = _account_id_for(item)
        if not acc_id:
            continue

        exact_dt = decode_snowflake(acc_id)
        if exact_dt is not None:
            item["account_created"]        = exact_dt.strftime("%Y-%m-%d")
            item["account_age"]            = humanize_age(exact_dt)
            item["account_age_flag"]       = age_flag(exact_dt)
            item["account_age_precision"]  = "exact"
            continue

        est_dt = estimate_sequential_era(acc_id)
        if est_dt is not None:
            item["account_created"]        = "~" + est_dt.strftime("%Y")
            item["account_age"]            = "~" + humanize_age(est_dt) + " (estimated)"
            item["account_age_flag"]       = age_flag(est_dt)
            item["account_age_precision"]  = "estimated"
            continue

        n = _as_int(acc_id)
        if n is not None and n < _CAL_LOW_ID:
            # Below our earliest calibration point — id ordering is still a
            # safe signal even without a specific date (lower id = signed up
            # earlier), so we can at least say "very early" with confidence.
            item["account_created"]        = None
            item["account_age"]            = f"Very early account (id predates our {_CAL_LOW_DT.strftime('%b %Y')} calibration point)"
            item["account_age_flag"]       = "established"
            item["account_age_precision"]  = "estimated"
        else:
            item["account_created"]        = None
            item["account_age"]            = "Unknown (id falls outside both the Snowflake and calibrated-estimate ranges)"
            item["account_age_flag"]       = None
            item["account_age_precision"]  = "unknown"
    return data
