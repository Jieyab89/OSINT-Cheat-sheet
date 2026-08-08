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
