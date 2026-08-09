// ── Shared card-rendering rules — kept byte-identical across index.html and
// archive.html by loading this one file, so field order / drill-down /
// badges never drift between "live search" and "saved archive" views of the
// same data. (Previously included via Jinja {% include %} directly inside a
// <script> block — moved to a real .js file so editor/JS tooling can lint it
// normally instead of flagging the Jinja syntax as invalid JavaScript.)

// Arr params 

const PRIORITY = [
  'source', 'content_type', 'account_age_flag', 'account_age', 'account_created',
  'user', 'screen_name', 'name', 'user_id', 'username',
  'verified', 'is_blue_verified',
  'text', 'full_text', 'article_text', 'post_title', 'post_text', 'content', 'title', 'description', 'bio',
  'reply_count', 'retweet_count', 'favorite_count', 'view_count',
  'followers_count', 'following_count', 'tweet_count',
  'created_at', 'fetched_at', 'in_reply_to_tweet_id',
  'retweeted_by_user', 'retweeted_by_name', 'retweeted_text', 'retweeted_by_bio', 'retweeted_at', 'retweeted_tweet_id',
  'quoted_user', 'quoted_name', 'quoted_text', 'quoted_at', 'quoted_tweet_id',
  'lat', 'lon', 'place', 'user_location',
  'tweet_url', 'archive_url', 'result_url', 'preview_image', 'display_link',
  'serp_title',
  'iso_date', 'original', 'statuscode', 'mimetype', 'length',
];

// content_type: what kind of X/Twitter page a Google CSE / Wayback result
// actually is — a search hit for a keyword could be a specific tweet, a
// bare profile page, some other X page, or (Google CSE only) a site off X
// entirely. Cookie/Xquik records don't carry this field at all (a tweet
// search result there is unambiguously always a tweet), so it only ever
// shows up for the two sources it's meant to disambiguate.
const CONTENT_TYPE_LABELS = {
  tweet:         'Tweet',
  profile:       'Profile page',
  twitter_other: 'Other X/Twitter page',
  other:         'External page (non-X)',
};

// Which fields link out to a fresh extraction for that tweet — same anchor
// behavior whether you're looking at a live result or a saved archive.
const DRILLABLE = {
  reply_count:          'tweet_replies_extractor',
  retweet_count:        'tweet_retweeters_extractor',
  in_reply_to_tweet_id: 'tweet_replies_extractor',
};

const SOURCE_CLASS = { 'Twitter Cookie': 'src-cookie', 'Xquik API': 'src-xquik', 'Wayback Machine': 'src-wayback', 'Google CSE': 'src-cse' };
const AGE_LABELS   = { new: 'New account', recent: 'Recent account', established: 'Established account' };

// ── Shared profile header (avatar/name/handle/banner/bio) ──────────────────
// Used by buildCard() in both index.html (live results) and archive.html
// (saved archives) so a record's author identity renders byte-identically
// whether you're looking at it live or after it's been archived — previously
// archive.html had no equivalent at all, so a saved card silently dropped
// the avatar/name/handle/bio/banner that the live card showed for the exact
// same record. `esc()` is expected to already be defined as a global by the
// time this actually runs (each page defines its own, loaded in a later
// <script> block — this file only *calls* esc() inside functions, it never
// runs at parse time, so load order is fine).

// Only a plain https URL (no quotes/angle-brackets/whitespace/parens) is
// ever interpolated into the CSS url('...') background-image — that goes
// through a second parsing pass CSS-side, so HTML-attribute escaping alone
// isn't sufficient there the way it is for a plain <img src>. Rejecting
// anything but a clean https URL up front closes that off rather than
// trying to escape a value for two contexts (HTML attribute + CSS token)
// wedged into one string.
function isSafeImageUrl(u) {
  return typeof u === 'string' && /^https:\/\/[^\s'"<>()]+$/.test(u);
}

// Blue-checkmark badge — is_blue_verified (paid X Premium) and verified
// (the legacy pre-2023 checkmark) are shown identically here since both are
// "this account has X's blue checkmark," just from different eras; which
// one it actually was is still visible as its own raw field further down
// the card, this is only the at-a-glance version next to the name.
function verifiedBadgeHtml(item) {
  if (!item || (!item.verified && !item.is_blue_verified)) return '';
  const title = item.is_blue_verified ? 'Blue verified (X Premium)' : 'Verified (legacy)';
  return `<span class="verified-badge" title="${esc(title)}">✓</span>`;
}

// Returns { html, usedFields } instead of just a string — buildCard() needs
// to know exactly which raw keys actually ended up rendered in the header
// so it can drop only THOSE from the generic row list. A static "always hide
// these field names" list doesn't work here: CSE/Wayback records also have a
// `description` field (Google's own snippet) that this header never touches
// (no avatar/name/handle on those records, so it returns empty) — hiding it
// unconditionally would silently delete the one thing the user asked to see.
function buildCardHeader(item) {
  const avatarRaw = item.avatar || item.user_avatar || '';
  const avatar    = isSafeImageUrl(avatarRaw) ? avatarRaw : '';
  const name      = item.name || '';
  const handle    = item.screen_name || item.user || item.username || '';

  if (!avatar && !name && !handle) return { html: '', usedFields: [] };

  const usedFields = [];
  if (avatar) usedFields.push(item.avatar ? 'avatar' : 'user_avatar');
  if (name) usedFields.push('name');
  if (handle) usedFields.push(item.screen_name ? 'screen_name' : item.user ? 'user' : 'username');

  const avatarHtml = avatar
    ? `<img class="card-avatar" src="${esc(avatar)}" alt="" loading="lazy" referrerpolicy="no-referrer">`
    : (name || handle)
      ? `<div class="card-avatar card-avatar-fallback">${esc((name || handle).charAt(0).toUpperCase())}</div>`
      : '';
  const identityHtml = (name || handle)
    ? `<div class="card-identity">
        ${name ? `<div class="card-name">${esc(name)}${verifiedBadgeHtml(item)}</div>` : ''}
        ${handle ? `<div class="card-handle">@${esc(handle)}</div>` : ''}
      </div>`
    : '';

  // A tweet or reply already leads with its own text a few rows down — a
  // full cover-photo-plus-bio header buries that under the *author's*
  // profile instead of the actual reply content. Those get a small inline
  // byline only; the full profile-card treatment (banner + bio) is reserved
  // for records that ARE a user — follower/retweeter results, not tweets a
  // user happened to write.
  const isTweetLike = item.text !== undefined || item.full_text !== undefined || item.article_text !== undefined;
  if (isTweetLike) {
    return { html: `<div class="card-byline">${avatarHtml}${identityHtml}</div>`, usedFields };
  }

  const bannerRaw = item.banner || item.user_banner || '';
  const banner    = isSafeImageUrl(bannerRaw) ? bannerRaw : '';
  const bio       = item.description || item.user_bio || '';
  if (banner) usedFields.push(item.banner ? 'banner' : 'user_banner');
  if (bio) usedFields.push(item.description ? 'description' : 'user_bio');

  const bioHtml = bio ? `<div class="card-bio">${esc(bio)}</div>` : '';
  const bannerHtml = banner
    ? `<div class="card-banner" style="background-image:url('${esc(banner)}')"></div>`
    : '';

  return {
    html: `<div class="card-header${banner ? ' has-banner' : ''}">${bannerHtml}<div class="card-header-row">${avatarHtml}${identityHtml}</div>${bioHtml}</div>`,
    usedFields,
  };
}
