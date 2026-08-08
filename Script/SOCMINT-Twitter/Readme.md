# Jieyab ft Xquik 

<img width="2552" height="1237" alt="Image" src="https://github.com/user-attachments/assets/20465836-89f0-453b-a0d5-fa2700b8ace1" />

# Update Note

1. Update infinity scroll and load new data for each search also in graph 
2. Update data corelation 
3. Fix business logic flow 
4. Monitoring (Soon)
5. MCP (Soon)
6. Add more parameter for enrichment 
7. Add no rate limit (throttle) 
8. Add Google CSE data source 
9. Expand data user profile post, follower and following, reply post, retweet post in graph — 
10. Add sentiment analysis for clustering data, pro, neutral, con based on archive data and dump data 
11. Add more data source and other parameter (soon) still research
12. Add more detail data source for the context 

## Features

- **Multi-source search** — one query fans out to Cookie, Xquik API,
  Wayback Machine, and Google CSE in parallel, each result tagged with
  which source it came from.
- **10 extraction tools** — tweet search, follower/following explorer, post
  (timeline) extractor, article extractor, community posts, tweet replies,
  tweet retweeters, geo-tagged search with a map view, Wayback archive
  search, and multi-source search.
- **Infinite scroll + inline nested reply threads** — scroll to load more
  pages automatically; expand a reply's own replies in place, recursively,
  the way X's own UI threads a conversation.
- **Relationship graph** (`/graph`) — a Cytoscape-based node graph. Select a
  node to expand its replies, retweeters, posts, followers, or following;
  pivot from any tweet straight to its author (no extra request — the data's
  already on the tweet); box-select multiple nodes and drag them together;
  edges are labeled by relationship (*replied by*, *followed by*, *authored
  by*, ...) and a distinct color flags where two different paths through the
  graph converge on the same account or tweet.
- **Archive** (`/archives`) — one-click (or auto-) save of a search's full
  raw results, including downloaded media, browsable and re-searchable later
  independent of whether the source is still reachable.
- **Analytics** (`/analytics`) — sentiment clustering (pro / neutral / con)
  over a saved archive, plus who posts most, what's driving the most
  engagement, and word frequency — see [Sentiment Analysis](#sentiment-analysis)
  below.
- **Account-age forensics** — every result with a numeric X/Twitter ID gets
  its account creation date decoded straight from the ID's Snowflake bits
  (no extra API call), flagged New / Recent / Established.
- **Security-conscious by default** — strict CSP with per-request nonces,
  hardened cookies, a whitelisted SSRF-safe video proxy, per-source request
  throttling to protect the logged-in account from rate limits, and
  URL-scheme validation everywhere a scraped link is rendered as an image or
  embedded in CSS.

# Sett up 

1. Config your Google api console here, enable and manage API Custom Search by Google  

<img width="2536" height="1210" alt="enable" src="https://github.com/user-attachments/assets/17aca5db-9869-40f0-8a9b-58eae51dce6c" />

2. Sett the api key in web console Google 

<img width="891" height="1354" alt="g-api" src="https://github.com/user-attachments/assets/1df5201e-9d8d-4450-9c46-cc83cb35eaba" />

Check the result in the table 

<img width="2121" height="1218" alt="g - api result" src="https://github.com/user-attachments/assets/1763dc2f-2382-4c94-8973-90f98678d477" />

3. Settings CSE Google to put the cx key 

<img width="2533" height="1254" alt="cx key" src="https://github.com/user-attachments/assets/b8d04387-2ac9-4302-8b04-2ea1873e610a" />

4. Add site want to crawll e.g twitter.com and x.com 

<img width="868" height="886" alt="add host and domain twitter" src="https://github.com/user-attachments/assets/caecb9d5-85c7-4fdb-8e38-e4acfc55630e" />

## Data Source 

1. Xquik API (subs there is a price)
2. Cookie (your account cookie session)  
3. Wayback Machine (Cdx API)
4. Goole CSE API (free quota 100 per day u can increase u limit with buy the service)

## Usage

### Search (`/`)

Pick a tool from the dropdown, fill in the field it asks for (query,
username, tweet ID, ...), and hit **Run**. Cookie-only tools (marked
`[Cookie]`) always use your logged-in session; everything else lets you
toggle between **Cookie** (your session, no xquik quota used) and **xquik
API** (uses your API key's quota) mode.

- Scroll down to auto-load more pages on any tool that supports pagination.
- Any card whose post has replies of its own gets an **Expand N replies**
  button — click it to thread the conversation inline, as deep as it
  actually goes.
- Toggle **Auto Archive** before running a search to save results as you go
  (including every scrolled-in page) — see [Archives](#archives-archives).
- **Geo Post Extractor** switches the results view to a map, geocoding each
  author's profile location.
- The `↓ JSON` button downloads exactly what's on screen as raw JSON.

### Graph (`/graph`)

Same 10 tools, rendered as a node graph instead of a card list.

- Click a node to inspect its full raw data in the side panel.
- **Expand Replies / Retweets** (tweet or reply nodes), **Expand Posts /
  Followers / Following** (user or retweeter nodes), and **View Author
  Profile** (tweet/reply nodes — pulls the author out as their own node,
  for free) all attach new nodes with a labeled edge showing the
  relationship.
- **Shift/Alt/Ctrl + drag** on empty canvas to box-select multiple nodes;
  drag any one of them to move the whole selection together. Plain drag
  still pans, scroll still zooms.
- A **yellow edge** means two different paths through the graph converged
  on the same node — worth a second look.
- **Archive All** / **Dump JSON** export everything currently on canvas.
- Click the **?** button (bottom-left) for the full legend.

### Archives (`/archives`)

Browse everything saved from Search or Graph. Pick an archive from the
sidebar to see its full raw results and any downloaded media. Archives
persist independent of whether the original source is still reachable —
useful for content that gets deleted or a session that expires.

### Analytics (`/analytics`)

Pick a saved archive to run sentiment clustering and the surrounding
aggregates over it:

- **Sentiment clustering** — every item with text gets classified **pro** /
  **neutral** / **con**, shown as a diverging bar plus per-category tiles
  you can click to filter the item list below.
- **Most active accounts** — who shows up most often in that archive.
- **Most engagement** — which items drove the most reply+retweet+like
  activity.
- **Word frequency** — a word cloud sized by how often each word appears.
- **Item browser** — every scored item, filterable by sentiment and
  searchable by text/author, with the model's confidence (or, in lexicon
  fallback mode, the exact matched words) shown per item — a classification
  is always inspectable, never a black box.

## Sentiment Analysis

Two backends, tried in this order (see `sentiment.py`):

1. **ML (preferred)** — [`cardiffnlp/twitter-xlm-roberta-base-sentiment`](https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment),
   an XLM-RoBERTa model fine-tuned for tweet sentiment across 8 languages
   (Arabic, English, French, German, Hindi, Italian, Portuguese, Spanish).
   Its underlying pretraining covers roughly 100 languages, so it degrades
   gracefully rather than failing outright on a language outside that
   fine-tuned set — this is what makes the tool usable for a global
   audience, not just Indonesian speakers. Requires `torch` + `transformers`
   (see `requirements.txt`) and downloads ~1.1GB of model weights from
   Hugging Face the first time it runs.
2. **Lexicon fallback** — a hand-built Indonesian positive/negative word
   list with negation handling (e.g. *"tidak bagus"* flips from positive to
   negative). Used automatically whenever `torch`/`transformers` aren't
   installed, so a lightweight install still has a working — if
   Indonesian-only — sentiment feature instead of a hard failure.

The `/api/analytics/<archive_id>` response always reports which backend
(`"ml"` or `"lexicon"`) produced its results, and the Analytics page's
banner reflects it. Neither backend is a ground-truth classifier — short
text, sarcasm, and irony degrade accuracy either way. Treat results as a
starting point for investigation, not a verdict.

## Settup

```bash
pip install -r requirements.txt
```

Edit `config.ini.example` to config.ini 

## Installing the ML sentiment model (optional, recommended)

The Analytics page's sentiment scoring works two ways — see
[Sentiment Analysis](#sentiment-analysis) above. Skipping everything on this
page is completely fine: the app still runs and Analytics still works, just
using the Indonesian-only lexicon instead of the multilingual model. This
section is only for turning on the better (multilingual) one. **You don't
need to know Python or be a developer to follow this — it's copy/paste.**

**Why a "virtual environment" (venv)?** It's just a private, throwaway
folder for this project's Python packages, kept separate from anything else
Python-related already on your computer. The ML packages (`torch`,
`transformers`) are large and can conflict with other unrelated tools if
installed system-wide — a venv avoids that entirely, and if anything ever
goes wrong, you just delete the `.venv` folder and start over, nothing else
on your machine is touched.

**1. Open a terminal in this project's folder** (the same folder as
`app.py`).

**2. Create the venv** (only needs to be done once):

```bash
python3 -m venv .venv
```

**3. Activate it** (needs to be done every time you open a new terminal to
work on this project):

- macOS / Linux:
  ```bash
  source .venv/bin/activate
  ```
- Windows (Command Prompt):
  ```bat
  .venv\Scripts\activate.bat
  ```
- Windows (PowerShell):
  ```powershell
  .venv\Scripts\Activate.ps1
  ```

Your terminal prompt should now start with `(.venv)` — that means it's
active and every `pip install` from here on stays inside this project's
private folder.

**4. Install everything** (the base app + the ML packages), in this order:

```bash
pip install --upgrade pip
pip install flask requests twifork
pip install --index-url https://download.pytorch.org/whl/cpu torch
pip install transformers sentencepiece protobuf
```

The third line is deliberately its own command — installing `torch` the
plain way can pull down a multi-gigabyte GPU-enabled build depending on your
system, when this app only ever needs the much smaller CPU version. Using
that exact command is what keeps the download small.

**5. Run the app as usual** (make sure `.venv` is still active — you'll see
`(.venv)` in your prompt):

```bash
python app.py
```

The **first time** you use the Analytics page after this, it will download
the sentiment model itself (~1.1GB) from Hugging Face automatically — this
needs an internet connection and can take a few minutes depending on your
connection, but only happens once. After that, it's cached on your computer
and loads instantly.

**Next time you come back to work on this project**, you only need step 3
again (activate) before running the app — steps 1, 2, and 4 are one-time
setup.

## Run Local Web Server 

```bash
python app.py
```

Open `http://127.0.0.1:5000`

# Results 

Xquik Dashboard 

<img width="2556" height="1193" alt="image" src="https://github.com/user-attachments/assets/51e9d0f3-d079-44ce-9841-378a3e1ad7e4" />

Dasboard Home 

<img width="2423" height="1217" alt="Image" src="https://github.com/user-attachments/assets/6ba91a78-5845-4e17-87e2-8171da3cec19" />

Archive 

<img width="2511" height="1228" alt="Image" src="https://github.com/user-attachments/assets/9e4fab45-edda-45f5-a88c-963e6bfdaeaf" />

<img width="2540" height="1235" alt="Image" src="https://github.com/user-attachments/assets/a0c0c42a-d16d-41c9-aac2-c95740eb5dc6" />

Graph

<img width="2556" height="1215" alt="Image" src="https://github.com/user-attachments/assets/98253ea7-2db4-4425-bc43-21be28b99596" />

Vidio 

<img width="2553" height="1300" alt="Image" src="https://github.com/user-attachments/assets/2bb138ac-1605-4c98-a38e-7e0716d9f4d1" />

Dir Output 

<img width="2131" height="1065" alt="image" src="https://github.com/user-attachments/assets/22c8900f-1418-45aa-a773-f85ac0f3f8a3" />

Sentiment Analysis 

<img width="2556" height="1243" alt="Image" src="https://github.com/user-attachments/assets/9138564b-9777-4697-a15d-0fda1898c250" />

<img width="2550" height="1231" alt="Image" src="https://github.com/user-attachments/assets/cddea86b-30ea-4f2d-ad14-c5e8751aa482" />

<img width="2553" height="1225" alt="Image" src="https://github.com/user-attachments/assets/0b10340a-1503-434a-9015-1719e169a664" />

# Help

About SnowflakeID -> Twitter userid : https://en.wikipedia.org/wiki/Snowflake_ID

About paramater was provided in data and dump with json file type 

<img width="2512" height="1230" alt="Image" src="https://github.com/user-attachments/assets/9d1a3b1e-03a4-45d0-9146-c171eaa6dbce" />

Xquik API DOC

Offc doc: https://docs.xquik.com/api-reference/overview

Soon i will check more detail about Twitter or X mechanism and business logic also endpoint API was listed in Mobile and Web 

Wayback archive data source 

The server connection to the Wayback Machine archive is often down, so try bumping the thread and don't set the throttle too high, and try checking the connection manually using curl.