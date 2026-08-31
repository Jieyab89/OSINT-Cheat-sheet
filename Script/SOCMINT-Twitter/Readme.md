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
9. Expand data user profile post, follower and following, reply post, retweet post in graph 
10. Add sentiment analysis for clustering data, pro, neutral, con. Based on archive data and dump data 
11. Add more data source and other parameter (soon) still research
12. Add more detail data source for the context 
13. Auto repair broken archive and sentiment analysis data dump
14. Update rendering data in sentiment analysis 
15. Update view as graph in archive 
16. Add date and timestamp pattern in sentiment analysis 
17. Delete entry node in graph visualizer 
18. Add new features save project (load case or load new case)
19. Checkpoint or save data 
20. Auto resume archive and dump data with state (state data to checkpoint)
21. Add date or timestamp paramater for all search module 
22. Update logic rate limit for X
23. Update add more paramater about account e.g account base location, total change username and etc 

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
  over a saved archive, a Maltego-style social network graph, plus who posts
  most, what's driving the most engagement, and word frequency — see
  [Sentiment Analysis](#sentiment-analysis) below.
- **Account-age forensics** — every result with a numeric X/Twitter ID gets
  its account creation date decoded straight from the ID's Snowflake bits
  (no extra API call), flagged New / Recent / Established.
- **Security-conscious by default** — strict CSP with per-request nonces,
  hardened cookies, a whitelisted SSRF-safe video proxy, per-source request
  throttling to protect the logged-in account from rate limits, and
  URL-scheme validation everywhere a scraped link is rendered as an image or
  embedded in CSS.

## Data Source

1. Xquik API (subs there is a price)
2. Cookie (your account cookie session)  
3. Wayback Machine (Cdx API)
4. Goole CSE API (free quota 100 per day u can increase u limit with buy the service)

## Setup

**1. Create a virtual environment** (a private folder for this project's
Python packages, kept separate from anything else on your machine — only
needs doing once):

```bash
python3 -m venv .venv
```

**2. Activate it** (do this every time you come back to work on the
project):

- macOS / Linux: `source .venv/bin/activate`
- Windows (Command Prompt): `.venv\Scripts\activate.bat`
- Windows (PowerShell): `.venv\Scripts\Activate.ps1`

Your terminal prompt should now start with `(.venv)`.

**3. Install dependencies:**

This installs Flask, the scraping/API clients, and the multilingual
sentiment model's packages (`torch`, `transformers`) — see
[Sentiment Analysis](#sentiment-analysis) for what that model runs. `torch`
comes in two flavors (same package, same version — just a different build)
and picking the right one matters: check which situation you're in first,
then follow that path. Don't run both — pick one.

First, check whether an NVIDIA GPU is actually reachable from where you're
running this:

```bash
nvidia-smi
```

- Prints a table (driver + CUDA version) → your GPU is reachable → **Option A**.
- `command not found` / no devices listed → **Option B**. This is also the
  normal outcome inside most VMs (VMware, VirtualBox, ...) even when the
  *host* machine has an NVIDIA GPU — a VM doesn't see the host's physical
  GPU unless you've specifically set up GPU passthrough, which most setups
  haven't. Docker Desktop on Windows (WSL2 backend) is the one common
  exception — it *can* reach the host's GPU if the NVIDIA driver is
  installed on Windows itself.

**Option A — GPU reachable:**

```bash
pip install -r requirements.txt
```

That's it. `transformers`' `pipeline()` auto-detects a usable GPU at
runtime (`torch.cuda.is_available()`) and uses it automatically — no code
changes, no extra flags. Sentiment scoring runs noticeably faster than on
CPU.

**Option B — no GPU reachable (including inside a VM without passthrough):**

```bash
pip install --index-url https://download.pytorch.org/whl/cpu torch
```

then 

```bash 
pip install -r requirements.txt
```

Installing the CPU-only build first means the plain `torch` line in
`requirements.txt` right after is already satisfied and won't pull the
much larger GPU-enabled build behind your back. This is the right choice
whenever `nvidia-smi` doesn't show a GPU — installing the GPU build there
wouldn't make anything faster (there's no GPU for it to use), it would
just download a few GB for nothing. The app runs fully functional either
way; sentiment scoring just runs on CPU (~11-12ms/item, fine for normal
archive sizes).

Whenever the project's dependencies change (new features, updates),
re-run whichever `pip install -r requirements.txt` command matches the
option you picked above:

```bash
pip install -r requirements.txt --upgrade
```

**4. Configure the Google CSE data source** (optional — only needed if you
want that source; everything else works without it):

1. Enable "Custom Search API" in the Google API Console.

<img width="2536" height="1210" alt="enable" src="https://github.com/user-attachments/assets/17aca5db-9869-40f0-8a9b-58eae51dce6c" />

2. Get an API key.

<img width="891" height="1354" alt="g-api" src="https://github.com/user-attachments/assets/1df5201e-9d8d-4450-9c46-cc83cb35eaba" />

Check the result in the table.

<img width="2121" height="1218" alt="g - api result" src="https://github.com/user-attachments/assets/1763dc2f-2382-4c94-8973-90f98678d477" />

3. Set up a Programmable Search Engine to get a `cx` key.

<img width="2533" height="1254" alt="cx key" src="https://github.com/user-attachments/assets/b8d04387-2ac9-4302-8b04-2ea1873e610a" />

4. Add the sites to crawl, e.g. `twitter.com` and `x.com`.

<img width="868" height="886" alt="add host and domain twitter" src="https://github.com/user-attachments/assets/caecb9d5-85c7-4fdb-8e38-e4acfc55630e" />

**5. Copy `config.ini.example` to `config.ini`** and fill in your keys.

**6. Run the app:**

```bash
python app.py
```

Open `http://127.0.0.1:5000`.

The first time you open the Analytics page, it downloads the sentiment
model (~1.1GB) from Hugging Face automatically — needs an internet
connection once, then it's cached locally and loads instantly after that.

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
- **Social network graph** — click **View as Graph** to see accounts as
  nodes, sized by how many items they posted in this archive and colored by
  their own pro/neutral/con mix, Maltego-style. Edges show reply
  relationships found in the archive; click a node to see its per-account
  sentiment breakdown.
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

# Results 

[![Watch the video](https://vumbnail.com/1216677900.jpg)](https://vimeo.com/1216677900)

Xquik Dashboard 

<img width="2556" height="1193" alt="image" src="https://github.com/user-attachments/assets/51e9d0f3-d079-44ce-9841-378a3e1ad7e4" />

Dasboard Home 

<img width="2423" height="1217" alt="Image" src="https://github.com/user-attachments/assets/6ba91a78-5845-4e17-87e2-8171da3cec19" />

Load Case / Project 

<img width="2532" height="1217" alt="image" src="https://github.com/user-attachments/assets/433d6f8a-a10f-4add-afeb-8935fc643e67" />

Checkpoint or Save the Project

<img width="2557" height="1218" alt="image" src="https://github.com/user-attachments/assets/d2ef01d6-108c-4ba7-ac90-52bb1fd881ce" />

Archive 

<img width="2511" height="1228" alt="Image" src="https://github.com/user-attachments/assets/9e4fab45-edda-45f5-a88c-963e6bfdaeaf" />

<img width="2540" height="1235" alt="Image" src="https://github.com/user-attachments/assets/a0c0c42a-d16d-41c9-aac2-c95740eb5dc6" />

Graph

<img width="2556" height="1215" alt="Image" src="https://github.com/user-attachments/assets/98253ea7-2db4-4425-bc43-21be28b99596" />

Search in Graph 

<img width="2550" height="1235" alt="image" src="https://github.com/user-attachments/assets/9de67226-5b12-4237-8057-690a4103a375" />

<img width="2550" height="1236" alt="image" src="https://github.com/user-attachments/assets/d585bb6b-910f-4079-abc8-c4e6c97a6df9" />

Vidio 

<img width="2553" height="1300" alt="Image" src="https://github.com/user-attachments/assets/2bb138ac-1605-4c98-a38e-7e0716d9f4d1" />

Dir Output 

<img width="2131" height="1065" alt="image" src="https://github.com/user-attachments/assets/22c8900f-1418-45aa-a773-f85ac0f3f8a3" />

Sentiment Analysis 

<img width="2556" height="1236" alt="image" src="https://github.com/user-attachments/assets/54f54f73-c739-4e1f-a0a0-431f2285f668" />

<img width="2555" height="1231" alt="image" src="https://github.com/user-attachments/assets/8f1b9bd5-2020-46fa-975a-ba418360ed91" />

<img width="2547" height="1178" alt="image" src="https://github.com/user-attachments/assets/7c5b5c21-a632-4513-8b8e-57f8da396d2f" />

Follower and Following 

<img width="2552" height="1226" alt="image" src="https://github.com/user-attachments/assets/d61d4b5d-f4eb-4b98-af59-7a77bf896f86" />

# Help

About SnowflakeID -> Twitter userid : https://en.wikipedia.org/wiki/Snowflake_ID

About paramater was provided in data and dump with json file type 

<img width="2512" height="1230" alt="Image" src="https://github.com/user-attachments/assets/9d1a3b1e-03a4-45d0-9146-c171eaa6dbce" />

Xquik API DOC

Offc doc: https://docs.xquik.com/api-reference/overview

Soon i will check more detail about Twitter or X mechanism and business logic also endpoint API was listed in Mobile and Web 

Wayback archive data source 

The server connection to the Wayback Machine archive is often down, so try bumping the thread and don't set the throttle too high, and try checking the connection manually using curl.

# Report Bug and Error 

If any error and bug also bussines process logic, please create an issue 