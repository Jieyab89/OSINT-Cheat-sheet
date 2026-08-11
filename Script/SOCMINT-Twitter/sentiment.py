"""Sentiment clustering (pro / neutral / con) for archived X/Twitter data,
plus the supporting "who's loudest, what's trending, what words dominate"
aggregates — the same shape of dashboard Drone Emprit-style tools give a
dataset.

Two scoring backends, tried in this order:

1. ML (preferred) — cardiffnlp/twitter-xlm-roberta-base-sentiment, an
   XLM-RoBERTa model fine-tuned for tweet sentiment across 8 languages
   (ar/en/fr/de/hi/it/pt/es). Its base pretraining covers ~100 languages, so
   it degrades gracefully rather than failing outright on a language outside
   that fine-tuning set — this is what makes the tool usable for an
   open-source audience that isn't Indonesian-only. Needs torch +
   transformers (see requirements.txt) and ~1.1GB of model weights
   downloaded from Hugging Face on first use.
2. Lexicon fallback — a hand-built Indonesian positive/negative word list
   with basic negation handling ("tidak bagus" flips "bagus" from positive
   to negative). Used automatically whenever torch/transformers aren't
   installed, so a lightweight install (just requirements.txt's base deps)
   still has a working — if Indonesian-only — sentiment feature rather than
   a hard failure. Every scored item exposes exactly which backend produced
   it (`method` on the analyze() payload), so a classification's provenance
   is never ambiguous, and the lexicon path additionally exposes the exact
   words that drove its score for full transparency.

Neither backend is a ground-truth classifier — short text, sarcasm, and
irony all degrade accuracy regardless of approach. Treat results as a
starting point for investigation, not a verdict.
"""

import re
import threading
from collections import Counter

# Local fallback 

# ── Sentiment lexicon ───────────────────────────────────────────────────────
# Indonesian words skew political/social-discourse (matches the kind of
# content this tool actually pulls — keyword searches on public affairs,
# government programs, public figures) as well as general register.
#
# Lexicon-parity note: an earlier version of this list ran ~130 positive vs.
# ~220 negative entries. That gap isn't neutral — with score_text() summing
# one point per matched word, a lexicon with substantially more negative
# coverage (more synonyms per concept: bohong/kebohongan/hoax/menipu/penipu/
# penipuan/tipu for one idea, "lying," vs. jujur/kejujuran for its opposite)
# structurally nudges mixed/ambiguous text toward "con" independent of the
# text's actual sentiment, simply because there's more negative surface area
# to match against. The additions below restore rough parity for the same
# governance/social-discourse register the negative list already covers
# (accountability, honesty, inclusion, rule of law) rather than padding with
# unrelated filler — pair each new word against the negative concept it
# offsets in a review. This is still a heuristic, not a bias-free scorer:
# see analyze()'s docstring and the module docstring above for the standing
# caveat that neither backend is ground truth.

# Arr data words 
# Need to feedback and research to sett the all parameter for each words 
# Need to help netizen Indo, with slang and words 

POSITIVE_WORDS = {
    "bagus", "baik", "hebat", "keren", "mantap", "mantul", "top", "terbaik",
    "sukses", "berhasil", "tepat", "benar", "setuju", "dukung", "dukungan",
    "mendukung", "apresiasi", "mengapresiasi", "bangga", "membanggakan",
    "senang", "gembira", "puas", "memuaskan", "bersyukur", "syukur",
    "alhamdulillah", "semoga", "maju", "kemajuan", "bijak", "bijaksana",
    "cerdas", "pintar", "amanah", "jujur", "kejujuran", "adil", "keadilan",
    "peduli", "kepedulian", "bermanfaat", "manfaat", "membantu", "bantuan",
    "solusi", "prestasi", "berprestasi", "unggul", "keunggulan", "luar biasa",
    "joss", "jos", "gas terus", "lanjutkan", "sip", "oke", "aman", "tenang",
    "damai", "sejahtera", "kesejahteraan", "makmur", "kemakmuran", "indah",
    "cantik", "tampan", "ramah", "sopan", "santun", "hormat", "menghormati",
    "salut", "kagum", "mengagumkan", "respect", "terharu", "terinspirasi",
    "inspiratif", "positif", "optimis", "optimisme", "harapan", "berharap",
    "cinta", "mencintai", "sayang", "suka", "menyukai", "rindu", "kangen",
    "gemas", "lucu", "menghibur", "menyenangkan", "menginspirasi", "tegas",
    "berani", "keberanian", "kuat", "gigih", "semangat", "bersemangat",
    "sukacita", "kompeten", "profesional", "berkualitas", "kualitas",
    "elegan", "canggih", "inovatif", "inovasi", "kreatif", "efisien",
    "efektif", "transparan", "transparansi", "akuntabel", "akuntabilitas",
    "merakyat", "membela rakyat", "pro rakyat", "berpihak pada rakyat",
    "terpuji", "membanggakan", "gemilang", "cemerlang", "berkah", "istimewa",
    # Governance/social-discourse counterparts added for lexicon parity
    # (offsetting korupsi/nepotisme/kkn, otoriter/diktator/fasis/represif,
    # rasis/intoleran, bohong/hoax/menipu, and pelanggaran/ilegal below).
    "bersih", "antikorupsi", "berintegritas", "integritas", "kredibel",
    "kredibilitas", "terpercaya", "dapat dipercaya", "netral", "imparsial",
    "objektif", "demokratis", "reformasi", "reformis", "inklusif",
    "inklusi", "toleran", "toleransi", "egaliter", "partisipatif",
    "aspiratif", "taat hukum", "patuh hukum", "sesuai aturan", "legal",
    "sah", "melindungi", "perlindungan", "membangun", "pembangunan",
    "sinergi", "berkolaborasi", "kolaboratif", "harmonis", "kondusif",
    "stabil", "stabilitas", "humanis", "empati", "berempati", "rendah hati",
    "dermawan",
}

NEGATIVE_WORDS = {
    "buruk", "keburukan", "jelek", "gagal", "kegagalan", "bodoh", "tolol",
    "goblok", "bego", "dungu", "idiot", "korupsi", "korup", "koruptor",
    "bohong", "kebohongan", "hoax", "menipu", "penipu", "penipuan", "tipu",
    "curang", "kecurangan", "culas", "zalim", "menzalimi", "kejam",
    "kekejaman", "jahat", "kejahatan", "rusak", "merusak", "hancur",
    "menghancurkan", "kacau", "mengacaukan", "parah", "memalukan",
    "memuakkan", "bejat", "biadab", "tolak", "menolak", "penolakan",
    "kecewa", "mengecewakan", "kekecewaan", "marah", "kemarahan", "murka",
    "benci", "membenci", "kebencian", "muak", "jijik", "menjijikkan",
    "sampah", "anjing", "bangsat", "bajingan", "kampret", "sialan",
    "kacung", "boneka", "munafik", "kemunafikan", "pengkhianat",
    "mengkhianati", "khianat", "pengkhianatan", "penjajah", "menjajah",
    "licik", "licin", "serakah", "keserakahan", "tamak", "otoriter",
    "diktator", "fasis", "salah", "kesalahan", "blunder", "konyol",
    "ngawur", "ngaco", "absurd", "aneh", "ironis", "ironi", "tragis",
    "miris", "prihatin", "keprihatinan", "sedih", "menyedihkan", "susah",
    "kesusahan", "sulit", "kesulitan", "sengsara", "menderita",
    "penderitaan", "korban", "dizalimi", "ditindas", "menindas",
    "penindasan", "kriminal", "pelanggaran", "melanggar", "ilegal",
    "pungli", "sogok", "menyuap", "disuap", "suap", "nepotisme", "kkn",
    "provokasi", "provokator", "memprovokasi", "fitnah", "memfitnah",
    "ancaman", "mengancam", "teror", "intimidasi", "mengintimidasi",
    "brutal", "kekerasan", "sadis", "tragedi", "bencana", "krisis",
    "darurat", "gawat", "resah", "keresahan", "meresahkan", "cemas",
    "kecemasan", "khawatir", "kekhawatiran", "takut", "ketakutan", "geram",
    "kesal", "jengkel", "dongkol", "malu", "hina", "menghina",
    "penghinaan", "murahan", "norak", "kampungan", "terbelakang", "mundur",
    "kemunduran", "ambruk", "bangkrut", "kebangkrutan", "defisit",
    "terlilit", "terjerat", "terjebak", "cengeng", "lemah", "kelemahan",
    "pengecut", "penakut", "plin-plan", "labil", "egois", "keegoisan",
    "sombong", "kesombongan", "angkuh", "arogan", "sok", "songong",
    "kurang ajar", "tidak becus", "amburadul", "berantakan", "semrawut",
    "menyengsarakan", "represif", "represi", "diskriminasi", "ruwet",
    "mendiskriminasi", "rasis", "rasisme", "intoleran", "intoleransi",
    "penjilat", "kontol", "memek", "paok", "stress", "goblog", "kontlo",
    "kepala batu", "oon", "bacot", "asu", "gijil", "jembut", "kanjut",
    "ngentot", "puki", "meki", "jembot", "pukimak", "kimak", "tembelek", 
    "tai", "bacod", "telaso", "dongo", "pauk", "jemboot", "Komdongo", 
    "komintod", "komintol", "cabul", "pencabulan", "omdo", "kunyuk",
    "munyuk", "monyet", "nyet", "jawir", "j4wir", "j4w1r", "kentu",
    "kenthu", "komdonggo", "komdungu", "kolot", "wowok", "cok",  
    "cokil", "jancok", "jiancuk", "jancook", "ancok", "ancook", 
    "coli", "nyoli", "oten", "0ten", "ten oten", "kadrun", "drun",
    "k4drun", "bgst", "bangset", "jingan", "bgsd", "antek2", "antek",
    "carut marut", "parcok", "parjo", "BUZZER", "buzzer", "buzer", 
    "kimbek", "bodat", "lapet", "muncung kau", "pukimai", "babi",
    "setan", "khuontol", "khontol", "ngacau", "gemblung", "ancur",
    "anjj", "anj", "wowi", "owi", "owok", "wok", "suram", "ecek2",
    "ecek ecek", "anak abah", "najis", "bunted", "modar", "modyar",
    "lud4h", "gblk", "zionis", "laknat", "provokasi", "provokator",
    "zionist", "bodo", "ludahi", "ludahin", "penjajah", "pajet", 
    "pajeet", "cemoohan", "cemooh", "rusuh", "barbar", "paj3t", 
    "cuih", "ngibul", "boong", 
}

# Flips the polarity of a sentiment word found within NEGATION_WINDOW tokens
# after it ("tidak bagus" -> negative even though "bagus" alone is positive).
# Indonesian often puts more distance between the negation and the word it
# actually governs than English does — "ngga ngajarin cara ngmg yg sopan"
# ("doesn't teach how to speak politely") is 5 tokens from negation to the
# sentiment word it negates. A wider window catches more of those at the
# cost of occasionally flipping something the negation wasn't really about;
# lexicon scoring is a heuristic either way, this just picks which failure
# mode to lean toward.
NEGATION_WORDS = {"tidak", "tak", "bukan", "belum", "jangan", "nggak", "ga", "gak", "kagak", "ngga"}
NEGATION_WINDOW = 5

# Boosts a sentiment word's weight rather than changing its polarity.
INTENSIFIERS = {"sangat", "banget", "sekali", "sungguh", "amat", "terlalu", "sangatlah"}
INTENSIFIER_MULTIPLIER = 1.5

STOPWORDS = {
    "yang", "dan", "di", "ke", "dari", "untuk", "dengan", "ini", "itu", "ya",
    "nya", "adalah", "akan", "saya", "kamu", "kita", "kami", "mereka", "dia",
    "juga", "saja", "sudah", "belum", "atau", "karena", "jika", "kalau",
    "agar", "supaya", "pada", "oleh", "dalam", "luar", "atas", "bawah",
    "antara", "seperti", "sebagai", "tentang", "bahwa", "namun", "tetapi",
    "tapi", "hingga", "sampai", "sejak", "setelah", "sebelum", "ketika",
    "saat", "ada", "punya", "milik", "lah", "kah", "pun", "deh", "dong",
    "sih", "kok", "loh", "nih", "gitu", "gini", "dsb", "dll", "dst", "yg",
    "utk", "dgn", "krn", "gak", "ga", "nggak", "tak", "tidak", "bukan",
    "jangan", "apa", "apakah", "siapa", "mengapa", "kenapa", "bagaimana",
    "dimana", "kapan", "para", "si", "sang", "an", "kan", "in", "the", "is",
    "are", "was", "were", "be", "been", "being", "to", "of", "for", "on",
    "with", "as", "by", "at", "an", "a", "rt",
} | NEGATION_WORDS | INTENSIFIERS

_WORD_RE  = re.compile(r"[a-zA-ZÀ-ÿ]+(?:-[a-zA-ZÀ-ÿ]+)?")
_URL_RE   = re.compile(r"https?://\S+")
_MENTION_RE = re.compile(r"@\w+")


def _tokenize(text: str) -> list[str]:
    """Lowercased word tokens with URLs/@mentions stripped first (both would
    otherwise pollute the lexicon match and the word cloud with usernames/
    link fragments neither list has any business scoring)."""
    if not text:
        return []
    cleaned = _URL_RE.sub(" ", text)
    cleaned = _MENTION_RE.sub(" ", cleaned)
    return [w.lower() for w in _WORD_RE.findall(cleaned)]


def score_text(text: str) -> dict:
    """Returns {label, score, matches} for one piece of text. label is one of
    "pro" / "neutral" / "con". matches lists (word, polarity, weight) for
    every lexicon hit, so a classification can be inspected rather than
    trusted blindly — a defining trait of a rule-based classifier is that you
    CAN see exactly why it decided what it decided."""
    tokens  = _tokenize(text)
    score   = 0.0
    matches = []

    for i, tok in enumerate(tokens):
        polarity = 1 if tok in POSITIVE_WORDS else -1 if tok in NEGATIVE_WORDS else 0
        if polarity == 0:
            continue

        weight = 1.0
        # Negation: any negation word in the preceding window flips polarity.
        window_start = max(0, i - NEGATION_WINDOW)
        if any(t in NEGATION_WORDS for t in tokens[window_start:i]):
            polarity = -polarity
        # Intensifier: any intensifier immediately before boosts magnitude
        # (checked after negation so "tidak sangat bagus" still flips first).
        if i > 0 and tokens[i - 1] in INTENSIFIERS:
            weight = INTENSIFIER_MULTIPLIER

        contribution = polarity * weight
        score += contribution
        matches.append({"word": tok, "polarity": "pro" if polarity > 0 else "con", "weight": weight})

    label = "pro" if score > 0 else "con" if score < 0 else "neutral"
    return {"label": label, "score": round(score, 2), "matches": matches}


def _item_text(item: dict) -> str:
    """The text worth scoring/tokenizing for a given archived record —
    varies by which tool produced it (a tweet's own text vs. a Wayback/CSE
    page's scraped title+description).

    `description` is deliberately NOT pulled from a bare user record (a
    follower/following/retweeter entry — cookie_client.py's _user_to_dict
    always sets `followers_count`, even to None, which no tweet/CSE/Wayback
    record ever carries, so that key's mere presence identifies the shape
    reliably). For a CSE result, `description` is Google's own snippet of
    the matched page — genuinely relevant text. For a user record it's the
    account's own bio, which says nothing about the search topic; scoring
    "suka kucing dan kopi ☕" as pro/con toward whatever was searched would
    just be noise. Those accounts are still kept for clustering/leaderboard
    purposes (top_users() below runs over every item regardless of text) —
    they're just excluded from sentiment/word-cloud scoring specifically."""
    is_bare_user_record = "followers_count" in item
    parts = [
        item.get("text"), item.get("full_text"), item.get("article_text"),
        item.get("post_title"), item.get("post_text"),
        None if is_bare_user_record else item.get("description"),
    ]
    return " ".join(p for p in parts if p)


def _item_author(item: dict) -> str | None:
    return item.get("screen_name") or item.get("user") or item.get("name")


def _item_engagement(item: dict) -> int:
    total = 0
    for k in ("reply_count", "retweet_count", "favorite_count"):
        v = item.get(k)
        if isinstance(v, (int, float)):
            total += v
    return total


def word_frequencies(items: list[dict], top_n: int = 60) -> list[dict]:
    """Word-cloud data: [{word, count}], most frequent first. Stopwords and
    single-character tokens are dropped; everything else counts regardless
    of whether it happened to be in the sentiment lexicon."""
    counts = Counter()
    for item in items:
        for tok in _tokenize(_item_text(item)):
            if len(tok) < 3 or tok in STOPWORDS:
                continue
            counts[tok] += 1
    return [{"word": w, "count": c} for w, c in counts.most_common(top_n)]


def top_users(items: list[dict], top_n: int | None = None) -> list[dict]:
    """Who shows up most often across the archive — every record with an
    identifiable author counts once, regardless of whether it's a tweet, a
    reply, a retweeter entry, or a bare follower/following record. Carries
    along the most recently seen avatar/name for that handle so the
    dashboard can show a face, not just a bare count.

    top_n=None (the default) returns EVERY account, not just the busiest N
    — this backs a digital-evidence archive, and silently dropping which
    accounts even show up here isn't something an OSINT tool gets to do.
    Counter.most_common(None) already returns everything sorted, so this
    costs nothing when unset; the dashboard paces rendering via scroll
    instead (see analytics.html's TOP_LIST_BATCH), not by the backend ever
    truncating the data. Pass an explicit top_n only if some future caller
    genuinely wants a fixed-size top list instead."""
    counts: Counter = Counter()
    display: dict[str, dict] = {}
    for item in items:
        handle = item.get("screen_name") or item.get("user")
        if not handle:
            continue
        counts[handle] += 1
        display[handle] = {
            "screen_name": handle,
            "name":        item.get("name"),
            "avatar":      item.get("avatar") or item.get("user_avatar"),
            "verified":    item.get("verified"),
            "is_blue_verified": item.get("is_blue_verified"),
            # Same account-age fields id_forensics.py's enrich_account_age()
            # already stamps onto every raw item at the /api/run choke point
            # (app.py) — index.html/archive.html/graph.html already surface
            # these as a badge; the analytics dashboard just wasn't pulling
            # them through to its own account list yet.
            "account_created":       item.get("account_created"),
            "account_age":           item.get("account_age"),
            "account_age_flag":      item.get("account_age_flag"),
            # account_age_flag is None whenever id_forensics.py's
            # enrich_account_age() lands in its own "unknown" bucket (an id
            # just outside the calibrated range — see that module's
            # docstring) — account_age_precision is what tells the frontend
            # "this account really is unresolvable," as opposed to just
            # never having had an account id to enrich in the first place.
            "account_age_precision": item.get("account_age_precision"),
        }
    ranked = []
    for handle, count in counts.most_common(top_n):
        ranked.append({**display[handle], "count": count})
    return ranked


def top_engagement(items: list[dict], top_n: int | None = None) -> list[dict]:
    """Which posts drove the most reply+retweet+favorite activity — "paling
    ramai" (busiest/most-discussed), not just most recent.

    top_n=None (the default) returns every scored item with positive
    engagement, not just the busiest N — same reasoning as top_users()
    above: this is digital evidence, the backend doesn't get to decide
    which posts are worth showing. `scored[:None]` is the full list."""
    scored = [(_item_engagement(it), it) for it in items if _item_text(it)]
    scored.sort(key=lambda pair: pair[0], reverse=True)
    return [{"engagement": score, "item": it} for score, it in scored[:top_n] if score > 0]


# ── ML backend (preferred) ───────────────────────────────────────────────────
# Lazy-loaded: importing torch/transformers and loading ~1.1GB of weights is
# slow, and both packages are optional (requirements.txt notes how to add
# them) — doing this at module import time would slow down every single use
# of this app, including ones that never touch analytics, and would hard-crash
# an install that skipped the ML deps entirely instead of just falling back.
_ML_MODEL_NAME    = "cardiffnlp/twitter-xlm-roberta-base-sentiment"
_ML_LABEL_MAP     = {"positive": "pro", "negative": "con", "neutral": "neutral"}
_ml_pipeline      = None
_ml_unavailable   = False   # sticky once loading fails — stop retrying every call
_ml_load_lock     = threading.Lock()


def _get_ml_pipeline():
    global _ml_pipeline, _ml_unavailable
    if _ml_pipeline is not None or _ml_unavailable:
        return _ml_pipeline
    with _ml_load_lock:
        if _ml_pipeline is not None or _ml_unavailable:   # re-check post-lock
            return _ml_pipeline
        try:
            from transformers import pipeline
            _ml_pipeline = pipeline("sentiment-analysis", model=_ML_MODEL_NAME)
        except Exception:
            # Missing torch/transformers, no internet for the first-time
            # model download, out of memory, ... any of these should fall
            # back to the lexicon scorer rather than take the whole
            # analytics endpoint down.
            _ml_unavailable = True
            _ml_pipeline = None
    return _ml_pipeline


def warm_up_ml() -> None:
    """Loads the ML pipeline right now instead of waiting for the first real
    analytics request to trigger it lazily. Measured at ~15-20s the first
    time any process calls _get_ml_pipeline() (importing transformers,
    constructing the pipeline, reading the cached weights off disk) — vs.
    ~11-12ms/item for actual scoring once loaded. Without this, that whole
    one-time cost lands inside the FIRST user's analytics job, during which
    the progress bar has nothing to report yet (on_progress only fires once
    scoring itself starts) and just sits at 0/0 looking stuck. Meant to be
    called from a background thread at server startup (see app.py) — still
    completely safe to skip calling this at all, or to have the first real
    request race it, since _get_ml_pipeline() is lock-protected and
    idempotent either way; this is purely a warm-up, not a dependency."""
    _get_ml_pipeline()


_ML_PROGRESS_CHUNK = 64   # texts per pipeline call — see _score_texts_ml docstring


def _score_texts_ml(texts: list[str], on_progress=None) -> list[dict] | None:
    """Scores every text, chunked (rather than one giant pipeline call), so
    a caller running this in a background thread can report real progress —
    on a CPU this measures ~11-12ms/item (~1000 items ≈ 12s, ~5000 ≈ ~1min),
    linear with volume, so a large archive genuinely takes a while and a
    caller polling for status needs something better to show than a blind
    spinner. _ML_PROGRESS_CHUNK=64 batches (each itself pipelined
    batch_size=16 internally by HF) keeps ticks frequent enough to feel
    live (~0.7-0.8s apart) without paying per-call overhead for every
    single item. Returns None if the model isn't available, so the caller
    falls back to the lexicon scorer instead. `score` is signed (positive
    for pro, negative for con, 0 for neutral) to match the lexicon
    backend's convention; `confidence` carries the model's own unsigned
    probability for the label it picked."""
    clf = _get_ml_pipeline()
    if clf is None:
        return None

    results = []
    for start in range(0, len(texts), _ML_PROGRESS_CHUNK):
        chunk = texts[start:start + _ML_PROGRESS_CHUNK]
        # truncation=True alone is NOT enough here: it truncates to the
        # tokenizer's own model_max_length, which for this tokenizer's
        # shipped config is left at HF's "unset" sentinel (~1e30, i.e.
        # effectively no limit) rather than the model's real 512-token
        # capacity. A single long post (a fact-check thread, an
        # article-length tweet — anything past ~512 tokens once
        # subword-tokenized) then sails through "truncation" untruncated,
        # overflows the model's position-embedding table, and crashes the
        # whole batch with a raw RuntimeError ("index 514 is out of bounds
        # for dimension 1 with size 514" — 514 = 512 + the 2-position
        # offset RoBERTa-style embeddings use). max_length=512 forces the
        # real limit regardless of what the tokenizer config claims.
        raw = clf(chunk, truncation=True, max_length=512, batch_size=16)
        for r in raw:
            label      = _ML_LABEL_MAP.get(str(r.get("label", "")).lower(), "neutral")
            confidence = float(r.get("score", 0.0))
            signed     = confidence if label == "pro" else -confidence if label == "con" else 0.0
            results.append({
                "label": label, "score": round(signed, 3),
                "confidence": round(confidence, 3), "matches": [],
            })
        if on_progress:
            on_progress(len(results), len(texts))
    return results


def analyze(items: list[dict], on_progress=None) -> dict:
    """Full analytics payload for one archive's worth of raw items.
    on_progress, if given, is called as on_progress(scored_count,
    total_to_score) — zero or more times during ML scoring (chunked, see
    _score_texts_ml), and always at least once at the very end regardless
    of which backend actually ran, so a caller polling for status always
    sees a final 100%-done tick even on the lexicon path (fast enough that
    per-chunk progress wouldn't mean anything, but a job registry watching
    for "did this reach total" still needs that terminal call)."""
    if not isinstance(items, list):
        items = [items]
    # archive.py's own _run() passes non-dict entries through as-is rather
    # than dropping them (see its "if not isinstance(item, dict)" branch),
    # so a saved archive can legitimately contain a stray non-dict item —
    # every function below assumes dict.get(), so those get filtered here
    # once rather than each helper needing its own isinstance guard.
    items = [it for it in items if isinstance(it, dict)]

    text_items, texts = [], []
    for item in items:
        text = _item_text(item)
        if text:   # skip e.g. a bare follower/following record with no post text of its own
            text_items.append(item)
            texts.append(text)

    ml_results = _score_texts_ml(texts, on_progress=on_progress) if texts else None
    method     = "ml" if ml_results is not None else "lexicon"
    if ml_results is None:
        ml_results = [score_text(t) for t in texts]
        if on_progress:
            on_progress(len(texts), len(texts))

    sentiment_counts = {"pro": 0, "neutral": 0, "con": 0}
    scored_items = []
    for item, text, result in zip(text_items, texts, ml_results):
        sentiment_counts[result["label"]] += 1
        scored_items.append({
            "label":      result["label"],
            "score":      result["score"],
            "confidence": result.get("confidence"),
            "matches":    result.get("matches", []),
            "author":     _item_author(item),
            "text":       text,
            "item":       item,
        })

    total = len(scored_items)
    return {
        "method":            method,
        "total_items":       len(items),
        "total_scored":      total,
        "sentiment_counts":  sentiment_counts,
        "sentiment_pct": {
            k: round(v / total * 100, 1) if total else 0.0
            for k, v in sentiment_counts.items()
        },
        "scored_items":  scored_items,
        "word_freq":     word_frequencies(items),
        "top_users":     top_users(items),
        "top_engagement": top_engagement(items),
    }
