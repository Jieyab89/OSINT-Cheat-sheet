// ── Shared card-rendering rules — kept byte-identical across index.html and
// archive.html by loading this one file, so field order / drill-down /
// badges never drift between "live search" and "saved archive" views of the
// same data. (Previously included via Jinja {% include %} directly inside a
// <script> block — moved to a real .js file so editor/JS tooling can lint it
// normally instead of flagging the Jinja syntax as invalid JavaScript.)
const PRIORITY = [
  'source', 'account_age_flag', 'account_age', 'account_created',
  'user', 'screen_name', 'name', 'user_id', 'username',
  'verified', 'is_blue_verified',
  'text', 'full_text', 'article_text', 'post_title', 'post_text', 'content', 'title', 'description', 'bio',
  'reply_count', 'retweet_count', 'favorite_count', 'view_count',
  'followers_count', 'following_count', 'tweet_count',
  'created_at', 'in_reply_to_tweet_id',
  'retweeted_by_user', 'retweeted_by_name', 'retweeted_text', 'retweeted_by_bio', 'retweeted_at', 'retweeted_tweet_id',
  'lat', 'lon', 'place', 'user_location',
  'tweet_url', 'archive_url', 'preview_image',
  'iso_date', 'original', 'statuscode', 'mimetype', 'length',
];

// Which fields link out to a fresh extraction for that tweet — same anchor
// behavior whether you're looking at a live result or a saved archive.
const DRILLABLE = {
  reply_count:          'tweet_replies_extractor',
  retweet_count:        'tweet_retweeters_extractor',
  in_reply_to_tweet_id: 'tweet_replies_extractor',
};

const SOURCE_CLASS = { 'Twitter Cookie': 'src-cookie', 'Xquik API': 'src-xquik', 'Wayback Machine': 'src-wayback' };
const AGE_LABELS   = { new: 'New account', recent: 'Recent account', established: 'Established account' };
