# Breach & Leak Intelligence

> *Tools sourced from [OSINT Cheat Sheet](https://github.com/Jieyab89/OSINT-Cheat-sheet) by [Jieyab89](https://github.com/Jieyab89)*

## Objective
Identify, analyze, and monitor data breaches and leaks related to a target —
including credential dumps, database leaks, stealer logs, and sensitive document
disclosures originating from dark web sources. All via clearnet services.

---

## 1. Breach Search Platforms

### HaveIBeenPwned (HIBP)
```
https://haveibeenpwned.com                → Single email check
https://haveibeenpwned.com/DomainSearch   → All emails at a domain (verify ownership)

# API
curl -s "https://haveibeenpwned.com/api/v3/breachedaccount/user@target.com" \
  -H "hibp-api-key: YOUR_KEY" \
  -H "User-Agent: investigator-tool" | python3 -m json.tool

# List all known breaches
curl -s "https://haveibeenpwned.com/api/v3/breaches" | \
  python3 -c "import sys,json; [print(b['Name'],'|',b['BreachDate'],'|',b['PwnCount']) for b in json.load(sys.stdin)]"
```

### Intelligence X
```
https://intelx.io/?s=target.com
https://intelx.io/?s=email@target.com
https://intelx.io/?s=TARGET_IP

# Indexes: Tor, I2P, paste sites, public leaks, documents, dark web forums
# Historical search — finds content from years back
# API (paid plan for full access)
curl -X POST "https://2.intelx.io/intelligent/search" \
  -H "x-key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"term":"target.com","maxresults":10,"media":0,"target":0,"timeout":10}'
```

### Breach Directory
```
https://breachdirectory.org
https://search.0t.rocks
https://osintleak.com
https://leakcheck.io                      → Free tier available
https://snusbase.com                      → Paid
https://dehashed.com                      → Paid, limited free
https://leakpeek.com
https://9ghz.com
https://weleakinfo.io
https://leakradar.io
https://exposed.lol
https://bf.based.re                       → BF database search
https://osintleak.com
```

---

## 2. Stealer Log Intelligence

Malware stealers (RedLine, Raccoon, Vidar, etc.) exfiltrate browser credentials,
cookies, crypto wallets. Their dumps appear on dark web markets and Telegram channels.

### Clearnet Monitoring Services
```
https://www.hudsonrock.com/threat-intelligence-cybercrime-tools
# Free search: enter domain to see if employee credentials were stolen
# by info-stealers and circulating in criminal markets

https://whiteintel.io
# Stealer log intelligence platform
# Check if domain credentials appear in stealer data

https://breach.house/all_stealers
# Aggregated stealer data viewer

https://www.infostealers.com
# Infostealer intelligence and research
```

### Hudson Rock — Free Domain Check
```python
import requests

domain = "target.com"
url = f"https://cavalier.hudsonrock.com/api/json/v2/osint-tools/search-by-domain?domain={domain}"
headers = {"User-Agent": "osint-research/1.0"}
resp = requests.get(url, headers=headers)
data = resp.json()

print(f"Employees in stealer logs: {data.get('total_employees', 0)}")
print(f"Users in stealer logs: {data.get('total_users', 0)}")
```

---

## 3. Paste Site Monitoring

Breached data often first appears on paste sites before being sold:

```
# Search
https://pastebin.com/search?q=target.com
https://psbdmp.ws                         → Pastebin dump search
https://cybdetective.com/pastebin.html    → Multi-paste aggregator

# Google dorks for paste sites
site:pastebin.com "target.com"
site:pastebin.com "@target.com" password OR credentials OR dump
site:pastebin.com "target.com" database
site:gist.github.com "target.com" password
site:paste.centos.org "target.com"
site:justpaste.it "target.com"

# Telegra.ph (Telegram's paste service)
site:telegra.ph "target.com"
```

### Automated Paste Monitoring
```python
import requests, time

def monitor_pastebin(keyword, interval=300):
    """Poll Pastebin scraping API for keyword matches"""
    seen = set()
    while True:
        try:
            # Pastebin scraping API (requires Pastebin Pro)
            r = requests.get("https://scrape.pastebin.com/api_scraping.php?limit=100")
            pastes = r.json()
            for paste in pastes:
                pid = paste["key"]
                if pid in seen:
                    continue
                seen.add(pid)
                content = requests.get(f"https://scrape.pastebin.com/api_scrape_item.php?i={pid}").text
                if keyword.lower() in content.lower():
                    print(f"[MATCH] https://pastebin.com/{pid}")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(interval)
```

---

## 4. Dark Web Breach Forum Intelligence (Clearnet Monitoring)

Monitor without directly accessing forums:

```
# DDO Secrets — public leak publishing
https://ddosecrets.com/wiki/Distributed_Denial_of_Secrets
# Contains government, corporate, and organizational leaks
# Accessible via clearnet

# Breach House
https://breach.house
# Aggregates publicly known breach data

# LeakIX — exposed services that may lead to breaches
https://leakix.net
# Indexes exposed databases, services, and leaked data

# Commercial dark web monitoring (passive intelligence)
https://www.stealthmole.com          → Dark web tracker
https://flare.io                     → Dark web monitoring platform
https://cyble.com                    → Cyble threat intelligence
https://cybersixgill.com             → Deep/dark web intelligence
https://darktrace.com                → AI-powered dark web monitoring
https://darkradar.io                 → Dark radar
```

---

## 5. Database Leak Analysis

When a leak dataset is available for analysis:

```python
import gzip, json

def analyze_leak(filepath, search_term):
    """Search a leak file for specific term"""
    opener = gzip.open if filepath.endswith('.gz') else open
    mode = 'rt' if filepath.endswith('.gz') else 'r'

    matches = []
    with opener(filepath, mode, encoding='utf-8', errors='ignore') as f:
        for i, line in enumerate(f):
            if search_term.lower() in line.lower():
                matches.append({"line": i, "content": line.strip()})
    return matches

# Example usage
results = analyze_leak("breach_dump.txt", "target.com")
for r in results[:10]:
    print(r)
```

### Common Leak File Formats
```
Format 1 — email:password
  user@domain.com:Password123

Format 2 — email:hash
  user@domain.com:5f4dcc3b5aa765d61d8327deb882cf99

Format 3 — JSON structured
  {"email":"user@domain.com","password":"...","name":"..."}

Format 4 — SQL dump
  INSERT INTO users VALUES (1,'user@domain.com','hash','name');
```

---

## 6. COMB & Large Dataset Search

```
https://proxynova.com/tools/comb/
# Search in "Collection of Many Breaches" — 3.2B+ records
# Free search by email or domain

https://www.proxynova.com/tools/comb/
# Alternative mirror
```

---

## 7. Library of Leaks

```
https://search.libraryofleaks.org
# Searchable archive of public leaks
# Includes: Wikileaks, Panama Papers, Pandora Papers, etc.

https://aleph.occrp.org
# OCCRP's investigative data platform
# Leaked documents, corporate records, court data
# Used by professional investigative journalists
```

---

## Analyzing a Breach Report

When you find a breach record, extract:

```
1. Breach date           → When did it occur vs. when discovered?
2. Data types exposed    → Passwords? PII? Financial? Health?
3. Number of records     → Scale of exposure
4. Source               → Which company/service was breached?
5. Format               → Plaintext passwords = high risk
6. Validation           → Cross-check against HIBP for confirmation
7. Related breaches     → Same actor? Same infrastructure?
```

---

## Tips

- **Hudson Rock free tool** is one of the most powerful for corporate exposure assessment
- **IntelX** has the deepest dark web index — essential for any serious investigation
- **DDO Secrets** is the best clearnet source for large-scale organizational leaks
- **HIBP Domain Search** requires ownership verification — useful for incident responders
- Always **validate** breach data before reporting — not all claimed breaches are real
- **Stealer logs** are more dangerous than traditional breaches — they include live session cookies

---

*Reference: [OSINT Cheat Sheet — Data Breached OSINT section](https://github.com/Jieyab89/OSINT-Cheat-sheet) by [Jieyab89](https://github.com/Jieyab89)*
