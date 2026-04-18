# Ransomware Group Tracking

> *Tools sourced from [OSINT Cheat Sheet](https://github.com/Jieyab89/OSINT-Cheat-sheet) by [Jieyab89](https://github.com/Jieyab89)*

## Objective
Monitor ransomware group activity, track victim postings on leak sites,
identify which groups are active, understand their TTPs, and collect
intelligence from their public-facing infrastructure — all via clearnet.

---

## 1. Ransomware Tracking Dashboards

### ransomware.live (Primary Source)
```
https://www.ransomware.live
# Real-time tracking of ransomware group victim posts
# Covers 100+ active ransomware groups
# Shows: victim name, country, sector, date posted, group name
# Includes screenshots of leak site posts

# Features:
# - Timeline of attacks
# - Group statistics
# - Sector/country breakdown
# - Search by victim name or group
```

### ransomwatch
```
https://ransomwatch.telemetry.ltd
# Monitors ransomware leak site posts
# Structured JSON data available for programmatic use
# Open source: https://github.com/joshhighet/ransomwatch

# API / Data access
curl https://raw.githubusercontent.com/joshhighet/ransomwatch/main/posts.json
curl https://raw.githubusercontent.com/joshhighet/ransomwatch/main/groups.json

# Python
import requests
posts = requests.get("https://raw.githubusercontent.com/joshhighet/ransomwatch/main/posts.json").json()
for post in posts:
    if "target_org" in post.get("post_title", "").lower():
        print(post)
```

### Ransom DB
```
https://www.ransom-db.com
# Searchable database of ransomware incidents
# Filter by: group, country, sector, date
```

### Ransom Private Tools
```
https://ransom.privtools.eu
# Aggregated ransomware group posts
# Useful for historical research
```

### WatchGuard Ransomware Tracker
```
https://www.watchguard.com/wgrd-security-hub/ransomware-tracker
# Curated ransomware incident tracker
```

---

## 2. Ransomware Group Intelligence

### Known Active Groups (Reference)
```
# Tier 1 (Most Active / Dangerous):
LockBit, ALPHV/BlackCat, Cl0p, Play, Akira, Black Basta,
Hunters International, RansomHub, Medusa, INC Ransom

# Leak Site Monitoring via ransomware.live covers all major groups
```

### Group Profiles via MITRE ATT&CK
```
https://attack.mitre.org/groups/
# Search for specific ransomware group
# Contains: TTPs, techniques, software used, campaigns

# Examples:
https://attack.mitre.org/groups/G0032/   → Lazarus Group
https://attack.mitre.org/groups/G0034/   → Sandworm
https://attack.mitre.org/software/       → Malware used by groups
```

### Malpedia — Ransomware Encyclopedia
```
https://malpedia.caad.fkie.fraunhofer.de
# Search by ransomware family name
# Contains: technical details, YARA rules, references, actor links

# Example
https://malpedia.caad.fkie.fraunhofer.de/details/win.lockbit
https://malpedia.caad.fkie.fraunhofer.de/details/win.blackcat
```

---

## 3. Ransomware Identification

If you have a sample or ransom note:

```
https://id-ransomware.malwarehunterteam.com
# Upload: encrypted file, ransom note, or file extension
# Identifies ransomware family

https://www.nomoreransom.org/en/identification-tool.html
# Ransomware identification + decryption tools if available
# Maintained by Europol + cybersecurity vendors
```

---

## 4. Ransomware Decryption Tools

```
https://www.nomoreransom.org/en/decryption-tools.html
# Free decryptors for many ransomware families
# Organized by ransomware name

https://github.com/erasmus-dsg-university/ransomware-decryptors
# Community collection of decryptors
```

---

## 5. Programmatic Data Collection

### Fetch ransomwatch JSON Data
```python
import requests
import json
from datetime import datetime

def get_recent_ransomware_posts(days=7):
    """Get ransomware posts from the last N days"""
    url = "https://raw.githubusercontent.com/joshhighet/ransomwatch/main/posts.json"
    posts = requests.get(url).json()

    cutoff = datetime.now().timestamp() - (days * 86400)
    recent = []
    for post in posts:
        try:
            ts = datetime.strptime(post["discovered"], "%Y-%m-%d %H:%M:%S.%f").timestamp()
            if ts > cutoff:
                recent.append(post)
        except:
            pass
    return recent

def search_victim(keyword):
    """Search for a specific victim across all posts"""
    url = "https://raw.githubusercontent.com/joshhijom/ransomwatch/main/posts.json"
    posts = requests.get(url).json()
    return [p for p in posts if keyword.lower() in p.get("post_title", "").lower()]

# Usage
recent = get_recent_ransomware_posts(days=30)
print(f"Posts in last 30 days: {len(recent)}")

victim_hits = search_victim("target company name")
for hit in victim_hits:
    print(hit.get("group_name"), "|", hit.get("post_title"), "|", hit.get("discovered"))
```

### Fetch Group List from ransomware.live
```python
import requests

# Get all tracked groups
resp = requests.get("https://api.ransomware.live/v2/groups")
groups = resp.json()
for g in groups:
    print(g.get("name"), "|", g.get("location"))
```

---

## 6. Cross-Reference with Threat Intelligence

After identifying a ransomware group, pivot to:

```
# CISA advisories
https://www.cisa.gov/known-exploited-vulnerabilities-catalog

# FBI flash alerts
https://www.ic3.gov/Media/News/2024

# Talos intelligence
https://www.talosintelligence.com/ransomware_roundup

# AlienVault OTX pulse for the group
https://otx.alienvault.com/browse/pulses?q=GROUPNAME

# VirusTotal collections
https://www.virustotal.com/gui/collections → search group name
```

---

## 7. Sector & Country Statistics

```
# From ransomware.live statistics
https://www.ransomware.live/charts

# Useful for:
# - Identifying most targeted sectors
# - Country-specific threat landscape
# - Time-based trend analysis
# - Executive-level reporting
```

---

## Tips

- **ransomware.live** is the single best free resource — bookmark it
- **ransomwatch JSON** is machine-readable — great for automated monitoring and alerting
- **MITRE ATT&CK** group pages have the most authoritative TTP mappings
- **Malpedia** is the best technical reference for malware family details and YARA rules
- Set up **automated alerts**: scrape ransomwatch JSON periodically and alert on new keyword matches
- **Victim names are often redacted** initially — monitor for updates where full names appear
- Cross-reference group names across **Malpedia + MITRE + VirusTotal** for complete picture

---

*Reference: [OSINT Cheat Sheet — Researching Cyber Threats & SOC/Threat Hunting sections](https://github.com/Jieyab89/OSINT-Cheat-sheet) by [Jieyab89](https://github.com/Jieyab89)*
