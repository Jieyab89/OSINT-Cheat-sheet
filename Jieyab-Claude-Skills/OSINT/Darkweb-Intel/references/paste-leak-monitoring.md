# Paste & Leak Monitoring

> *Tools sourced from [OSINT Cheat Sheet](https://github.com/Jieyab89/OSINT-Cheat-sheet) by [Jieyab89](https://github.com/Jieyab89)*

## Objective
Monitor paste sites, anonymous publishing services, and public leak channels
for early detection of data disclosures, credential dumps, and sensitive
information related to a target — before it spreads or is sold.

---

## 1. Paste Site Inventory

### Primary Targets for Monitoring
```
https://pastebin.com                    → Largest paste site
https://psbdmp.ws                       → Pastebin dump aggregator/search
https://cybdetective.com/pastebin.html  → Multi-paste search (Jieyab89's list)
https://paste.centos.org                → CentOS community paste
https://justpaste.it                    → Popular alternative
https://gist.github.com                 → GitHub Gist (code snippets)
https://friendpaste.com                 → Alternative paste site
https://telegra.ph                      → Telegram's publish platform
https://psbdmp.ws                       → Pastebin dump search
```

---

## 2. Search Strategies

### Google Dork Paste Search
```
# Find mentions of target on paste sites
site:pastebin.com "target.com"
site:pastebin.com "@target.com" password
site:pastebin.com "target.com" database OR dump OR leak OR breach
site:pastebin.com "target.com" username OR email OR credential

site:gist.github.com "target.com" secret OR key OR password
site:justpaste.it "target.com"
site:paste.centos.org "target.com"
site:telegra.ph "target.com" breach OR leak

# Broader search
"target.com" site:pastebin.com OR site:gist.github.com OR site:justpaste.it
```

### Intelligence X Paste Search
```
https://intelx.io/?s=target.com
# IntelX indexes many paste sites including dark web pastes
# More comprehensive than Google for paste monitoring
```

---

## 3. Automated Paste Monitoring

### Pastebin Scraping API (Requires Pastebin Pro Account)
```python
import requests, time, hashlib, json
from datetime import datetime

class PasteMonitor:
    """Monitor Pastebin scraping API for keyword matches"""

    def __init__(self, keywords, scraping_key=None):
        self.keywords = [k.lower() for k in keywords]
        self.scraping_key = scraping_key
        self.seen = set()
        self.hits = []

    def fetch_recent(self):
        """Get recent public pastes via scraping API"""
        url = "https://scrape.pastebin.com/api_scraping.php?limit=100"
        if self.scraping_key:
            url += f"&scraping_key={self.scraping_key}"
        try:
            resp = requests.get(url, timeout=10)
            return resp.json()
        except:
            return []

    def fetch_content(self, paste_key):
        """Fetch raw content of a paste"""
        url = f"https://scrape.pastebin.com/api_scrape_item.php?i={paste_key}"
        try:
            resp = requests.get(url, timeout=10)
            return resp.text
        except:
            return ""

    def scan(self):
        """One monitoring cycle"""
        pastes = self.fetch_recent()
        for paste in pastes:
            key = paste.get("key")
            if not key or key in self.seen:
                continue
            self.seen.add(key)

            content = self.fetch_content(key)
            content_lower = content.lower()

            matched = [kw for kw in self.keywords if kw in content_lower]
            if matched:
                hit = {
                    "time": datetime.now().isoformat(),
                    "url": f"https://pastebin.com/{key}",
                    "keywords": matched,
                    "size": paste.get("size"),
                    "title": paste.get("title", ""),
                    "content_preview": content[:200]
                }
                self.hits.append(hit)
                print(f"[HIT] {hit['url']} | Keywords: {matched}")

    def run(self, interval=300):
        """Continuous monitoring loop"""
        print(f"Monitoring for: {self.keywords}")
        while True:
            self.scan()
            time.sleep(interval)

# Usage
monitor = PasteMonitor(keywords=["target.com", "targetcompany", "@target.com"])
monitor.run(interval=300)  # Check every 5 minutes
```

---

## 4. Telegram Channel Monitoring

Many breach actors publish on Telegram before or instead of dark web forums:

```
# Search Telegram content (clearnet)
https://www.tgstat.com               → Telegram channel statistics & search
https://telemetr.io                  → Telegram analytics
https://www.telegramchannels.me      → Channel directory

# Search for relevant channels
# Keywords: "leaks", "breach", "database", "credentials", "combolist"

# Telegram web search (no account needed)
https://t.me/s/CHANNEL_NAME          → View channel posts in browser

# Archive Telegram content
# Reference from Jieyab89:
https://www.bellingcat.com/resources/how-tos/2022/03/08/how-to-archive-telegram-content-to-document-russias-invasion-of-ukraine/
```

---

## 5. DDO Secrets — Document & Leak Archive

```
https://ddosecrets.com/wiki/Distributed_Denial_of_Secrets
# Clearnet accessible archive of major leaks
# Categories: government leaks, corporate data, hacked datasets
# Contains: BlueLeaks (US law enforcement), Epik (hosting), ransomware dumps, etc.

# How to use:
# - Browse by category or search by organization name
# - Download index files to understand scope before downloading full datasets
# - All content is legally accessible via clearnet
```

---

## 6. Library of Leaks

```
https://search.libraryofleaks.org
# Searchable archive of public interest leaks
# Includes: Wikileaks, Panama Papers, Pandora Papers, FinCEN Files, etc.

https://aleph.occrp.org
# OCCRP investigative data platform
# Cross-reference leaked documents with corporate registries and court data
```

---

## 7. Early Warning Intelligence

### Signals to Watch For
```
Indicators that a breach may be incoming or just happened:

1. Threat actor posts "we are selling [company] data" in forums
   → Monitor via: ransomware.live, darkfeed.io, flare.io

2. Internal credentials appearing on paste sites
   → Monitor via: pastebin scraping + IntelX

3. Domain mentioned in stealer log markets
   → Monitor via: Hudson Rock, whiteintel.io

4. Company name appears in Telegram breach channels
   → Monitor via: tgstat.com search

5. Unusual volume of mentions in dark web search results
   → Monitor via: IntelX, Ahmia, darksearch.io
```

### Building a Keyword Watchlist
```python
# Keywords to monitor for a target organization
WATCHLIST = {
    "company_names": ["Target Corp", "TargetCo", "target-corp"],
    "domains": ["target.com", "targetcorp.com"],
    "email_patterns": ["@target.com", "@targetcorp.com"],
    "brand_names": ["TargetProduct", "TargetBrand"],
    "executive_names": ["John CEO Smith", "Jane CFO Doe"],  # Key executives
    "internal_terms": ["internal_system_name", "product_codename"]
}
```

---

## 8. Breach Validation

Before escalating or reporting a potential breach find:

```
Step 1: Verify the data is real
  - Check sample records against known public info (are names/emails plausible?)
  - Check date fields — are they consistent with claimed breach date?
  - Do NOT contact individuals in the dataset to verify

Step 2: Determine if already known
  - Cross-check against HIBP: https://haveibeenpwned.com/PwnedWebsites
  - Check databreaches.net: https://databreaches.net
  - Search intelx.io for the same dataset

Step 3: Assess severity
  - What data types: passwords? PII? financial? health?
  - Plaintext vs hashed passwords?
  - Volume of records?
  - Date of the data (older = lower risk of active exploitation)

Step 4: Document and report
  - Screenshot with timestamps
  - Archive the paste/post URL (use archive.today)
  - Preserve hash of any downloaded evidence files
  - Report to affected organization's security team (responsible disclosure)
```

---

## Tips

- **Monitor daily** — paste site data disappears quickly (Pastebin auto-deletes)
- **Archive immediately** when you find something relevant — use archive.today
- **IntelX** is the most reliable for historical paste search and dark web content
- **Telegram** is now a primary distribution channel for breach data — don't ignore it
- **False positives** are common — always validate before escalating
- **GDPR/legal caution**: in some jurisdictions, downloading breach data may have legal implications — consult your legal counsel

---

*Reference: [OSINT Cheat Sheet — Data Breached OSINT, Forums & Sites sections](https://github.com/Jieyab89/OSINT-Cheat-sheet) by [Jieyab89](https://github.com/Jieyab89)*
