# Dark Web Search & Indexing

> *Tools sourced from [OSINT Cheat Sheet](https://github.com/Jieyab89/OSINT-Cheat-sheet) by [Jieyab89](https://github.com/Jieyab89)*

## Objective
Search and index dark web content using clearnet-accessible tools, proxies,
and aggregators — without requiring a Tor browser for most operations.

---

## 1. Clearnet Dark Web Search Engines

These index .onion content and are accessible from a regular browser:

```
https://ahmia.fi                          → Most established Tor search engine
                                            accessible via clearnet
https://darksearch.io                     → Dark web search via clearnet API
https://lolarchiver.com                   → Archived dark web content
https://osint.lolarchiver.com             → OSINT-focused dark archive
https://open-search.aleph-networks.eu     → Open search with dark web data
```

### Ahmia.fi Usage
```
# Basic search
https://ahmia.fi/search/?q=ransomware+group

# Search for specific onion addresses
https://ahmia.fi/search/?q=site:ONIONADDRESS.onion

# API
curl "https://ahmia.fi/api/query?q=keyword&limit=10"
```

### DarkSearch.io API
```bash
# Search via API (free tier available)
curl "https://darksearch.io/api/search?query=keyword&page=1"

# Python
import requests
resp = requests.get("https://darksearch.io/api/search",
    params={"query": "ransomware group", "page": 1})
print(resp.json())
```

---

## 2. Intelligence X (IntelX)

One of the most powerful dark web indexing platforms — indexes Tor, I2P, paste
sites, public leaks, and document archives:

```
https://intelx.io/?s=keyword
https://intelx.io/?s=email@target.com
https://intelx.io/?s=target.com
https://intelx.io/?s=BITCOIN_WALLET_ADDRESS

# Selectors to search:
# - Email addresses
# - Domains
# - IP addresses
# - Bitcoin addresses
# - IPFS hashes
# - URLs
# - Phone numbers
```

---

## 3. Tor Hidden Service Search (Requires Tor Browser)

> Only use this for authorized research. Use a dedicated sandbox VM + Tor Browser.
> Never access from your real machine or identity.

```
# Popular .onion search engines (access via Tor Browser only)
DuckDuckGo onion : https://3g2upl4pq6kufc4m.onion
Torch            : http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5ayieeo2through7sh6turd.onion
Not Evil         : http://notevilmtxf25uw7tskqxj6njlpebyrmlrerfv5hc4tuq7c7hilbyiqd.onion
Haystak          : http://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion
```

---

## 4. Specialized Dark Web Index Tools

### DeepDarkCTI
Threat intelligence from deep and dark web sources:
```bash
# From Jieyab89's list
git clone https://github.com/fastfire/deepdarkCTI
# Contains curated .onion links categorized by type:
# - Forums, markets, ransomware leak sites, paste services
# - Updated list of active dark web resources for CTI
cat deepdarkCTI/ransomware.md         # Ransomware sites list
cat deepdarkCTI/forum.md              # Forum list
cat deepdarkCTI/combolist.md          # Combo/leak list sites
```

### OnionSearch
```bash
pip install onionsearch
onionsearch "keyword"
# Searches across multiple .onion search engines simultaneously
```

---

## 5. OSINT Framework — Dark Web Section

```
https://osintframework.com
# Navigate to: Digital Footprint → Dark Web
# Contains categorized links to:
# - Dark web search engines
# - Forums (indexed/cached versions)
# - Cryptocurrency tracking
# - Paste services
```

---

## 6. Cached & Archived Dark Web Content

Access dark web content without connecting to Tor:

```
https://osint.lolarchiver.com         → Cached dark web content
https://lolarchiver.com               → Dark web archiver
https://www.libraryofleaks.org        → Leaked document library
https://search.libraryofleaks.org     → Search leaked documents

# DDO Secrets (Distributed Denial of Secrets) — public leak archive
https://ddosecrets.com/wiki/Distributed_Denial_of_Secrets
# Contains: government leaks, corporate data, hacked datasets
# Browse without accessing dark web directly

# ALEPH (OCCRP)
https://aleph.occrp.org
# Investigative journalism data repository
# Contains leaked documents, corporate records, court data
```

---

## 7. I2P & Freenet Monitoring (Passive)

```
# I2P eepsites search (passive indexing services)
https://i2psearch.com
http://i2pforum.i2p   (requires I2P)

# Freenet content search (passive)
# Use Freenet indexes accessible via clearnet bridges
```

---

## 8. Darkweb Academy

```
# From Jieyab89's OSINT Academy list
https://www.darkwebacademy.com/labs/
# Provides labs and training for dark web OSINT
# Safe, sandboxed environments for learning
```

---

## Search Strategies

### Finding Specific Content
```
# Entity-based search
"company name" site:ransomgroup.onion     (via Ahmia)
"email@domain.com" intext:password       (via IntelX)
"domain.com" leak OR breach OR dump      (via DarkSearch)

# Hash-based search
"MD5HASH" OR "SHA256HASH"               (malware samples)
"bitcoin:WALLETADDRESS"                  (crypto payment traces)

# Forum activity
"threat actor alias" forum               (track actor across platforms)
```

### Building a Search Query
```
1. Start broad: target name, domain, or keyword
2. Narrow with context: + "breach" / "leaked" / "sale" / "dump"
3. Add time filter if available
4. Cross-reference hits across multiple platforms
5. Extract and pivot from any new selectors found (emails, wallets, aliases)
```

---

## Tips

- **Ahmia** is the most reliable clearnet index for general .onion search
- **IntelX** has the deepest historical index — worth using for any serious investigation
- **DeepDarkCTI** repo is regularly updated with active dark web site links
- **DDO Secrets** is the best clearnet source for leaked government/corporate data
- **ALEPH/OCCRP** is excellent for cross-referencing against investigative journalism leaks
- Always **document your search queries** — reproducibility matters in investigations

---

*Reference: [OSINT Cheat Sheet — Data Breached OSINT & Forums sections](https://github.com/Jieyab89/OSINT-Cheat-sheet) by [Jieyab89](https://github.com/Jieyab89)*
