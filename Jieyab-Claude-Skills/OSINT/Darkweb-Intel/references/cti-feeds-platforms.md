# CTI Feeds & Platforms

> *Tools sourced from [OSINT Cheat Sheet](https://github.com/Jieyab89/OSINT-Cheat-sheet) by [Jieyab89](https://github.com/Jieyab89)*

## Objective
Integrate structured threat intelligence feeds and platforms into an investigation
or detection workflow — covering open-source, community, and commercial CTI sources.

---

## 1. Open-Source CTI Platforms

### MISP — Malware Information Sharing Platform
```
https://www.misp-project.org
# Industry-standard open-source CTI sharing platform
# Self-hosted: share IOCs within a trusted community or organization
# Integrates with: Splunk, TheHive, Cortex, QRadar, etc.

# Public MISP instances (read access)
https://www.circl.lu/doc/misp/         → CIRCL MISP (Luxembourg CSIRT)

# MISP feed consumption
# Most major feeds (OTX, abuse.ch, etc.) have MISP format exports
```

### OpenCTI
```
# From Jieyab89's list
https://github.com/OpenCTI-Platform/opencti
# Open-source CTI platform — store, analyze, and share intelligence
# Knowledge graph: actor → campaign → malware → IOC → victim
# Integrates with MISP, STIX/TAXII, TheHive
# Self-host via Docker: docker-compose up -d  (demo.opencti.io no longer reliable)
```

### IntelOwl
```
# From Jieyab89's list
https://github.com/intelowlproject/IntelOwl/
# Aggregates results from 50+ analyzers (VT, OTX, Shodan, etc.)
# Single API call → enriched IOC from all sources simultaneously
# Self-hosted, free, open-source
```

---

## 2. Community Intelligence Feeds

### AlienVault OTX
```
https://otx.alienvault.com
# Free, community-driven threat intelligence
# "Pulses" = collections of IOCs around a specific threat

# Subscribe to relevant pulses
# Follow actors: APT28, LockBit, Emotet, etc.

# DirectConnect API
curl "https://otx.alienvault.com/api/v1/pulses/subscribed" \
  -H "X-OTX-API-KEY: YOUR_KEY"

# Pull IOCs from a pulse
curl "https://otx.alienvault.com/api/v1/pulses/PULSE_ID/indicators" \
  -H "X-OTX-API-KEY: YOUR_KEY"

# Python SDK
pip install OTXv2
from OTXv2 import OTXv2
otx = OTXv2("YOUR_API_KEY")
pulse = otx.get_pulse_details("PULSE_ID")
indicators = otx.get_pulse_indicator_details("PULSE_ID")
```

### Pulsedive
```
# From Jieyab89's list
https://pulsedive.com/dashboard/
# Free tier available
# IOC enrichment, threat feeds, risk scoring

# API
curl "https://pulsedive.com/api/?indicator=suspicious.com&key=YOUR_KEY"
```

### ThreatMiner
```
# From Jieyab89's list
https://www.threatminer.org
# Passive threat intelligence — no API key needed for basic use

# Lookups:
https://www.threatminer.org/domain.php?q=suspicious.com
https://www.threatminer.org/ip.php?q=1.2.3.4
https://www.threatminer.org/sample.php?q=SHA256_HASH
```

---

## 3. Commercial CTI Platforms (Free Tiers Available)

### Recorded Future
```
https://www.recordedfuture.com/vulnerability-database
# Free risk score lookup for IPs, domains, CVEs

# Risk API (limited free access)
curl "https://api.recordedfuture.com/v2/ip/1.2.3.4" \
  -H "X-RFToken: YOUR_TOKEN"
```

### Flare
```
# From Jieyab89's list
https://flare.io
# Dark web monitoring + CTI platform
# Monitors: paste sites, dark web forums, leak sites, Telegram
```

### Stealthmole
```
# From Jieyab89's list
https://www.stealthmole.com
# Dark web tracker with CTI focus
```

### Cybersixgill
```
# From Jieyab89's list
https://cybersixgill.com
# Deep and dark web intelligence
# Real-time monitoring of underground forums
```

### Darkfeed
```
# From Jieyab89's list
https://darkfeed.io
# Dark web IOC feed
```

### Falcon Feeds
```
# From Jieyab89's list
https://falconfeeds.io
# Threat intelligence from dark web sources
```

---

## 4. STIX/TAXII — Structured Intelligence Sharing

Standard format for machine-readable threat intelligence:

```python
# Install dependencies
pip install taxii2-client stix2

from taxii2client.v21 import Server

# MITRE ATT&CK TAXII (confirmed active)
server = Server("https://cti-taxii.mitre.org/taxii/")
for api_root in server.api_roots:
    for collection in api_root.collections:
        print(collection.title, collection.id)

# Note: CISA TAXII (ais.cisa.gov) and Anomali Limo (limo.anomali.com)
# are no longer resolving as of 2025 — use alternatives above instead
```

### Active Public TAXII Servers
```
https://cti-taxii.mitre.org/taxii/    → MITRE ATT&CK (confirmed active)

# Note: limo.anomali.com and ais.cisa.gov/taxii2/ no longer resolve (dead)
# Use MITRE ATT&CK TAXII or self-hosted MISP feeds instead
```

### Alternative — MITRE ATT&CK via GitHub JSON (Simpler, No TAXII Client)
```python
import requests

# Fetch all ATT&CK groups directly
url = "https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json"
data = requests.get(url).json()

groups = [obj for obj in data["objects"] if obj["type"] == "intrusion-set"]
for g in groups:
    print(g.get("name"), "|", g.get("aliases", []))
```

### CISA KEV Feed (Replaces CISA TAXII)
```python
import requests

# CISA Known Exploited Vulnerabilities — always updated JSON feed
url = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
data = requests.get(url).json()

vulns = data.get("vulnerabilities", [])
print(f"Total KEVs: {len(vulns)}")
for v in vulns[-5:]:  # Latest 5
    print(v.get("cveID"), "|", v.get("vendorProject"), "|", v.get("dueDate"))
```

---

## 5. Threat Hunting Platforms

### Splunk (SIEM)
```
# From Jieyab89's list
https://www.splunk.com
# Leading SIEM for log analysis and threat hunting

# Free: Splunk Free (500MB/day)
# Useful SPL for hunting:
# index=* sourcetype=* [inputlookup ioc_list.csv]
```

### Wazuh (Open-Source SIEM/XDR)
```
# From Jieyab89's list
https://wazuh.com
# Free, open-source security monitoring
# Integrates with MISP and threat intel feeds
```

### Grafana
```
# From Jieyab89's list
https://grafana.com
# Visualization for threat intelligence dashboards
# Connect to MISP, OpenCTI, or custom CTI databases
```

---

## 6. Integrating Feeds into a Pipeline

### Simple IOC Aggregation Pipeline
```python
import requests, json
from datetime import datetime

class CTIPipeline:
    def __init__(self, otx_key):
        self.otx_key = otx_key
        self.iocs = {"domains": [], "ips": [], "hashes": [], "urls": []}

    def pull_threatfox(self, days=1):
        """Pull recent IOCs from ThreatFox"""
        resp = requests.post("https://threatfox-api.abuse.ch/api/v1/",
            json={"query": "get_iocs", "days": days})
        for ioc in resp.json().get("data", []):
            ioc_type = ioc.get("ioc_type")
            value = ioc.get("ioc")
            if ioc_type == "domain":
                self.iocs["domains"].append(value)
            elif ioc_type in ("ip:port", "ip"):
                self.iocs["ips"].append(value.split(":")[0])
            elif ioc_type in ("sha256_hash", "md5_hash"):
                self.iocs["hashes"].append(value)
            elif ioc_type == "url":
                self.iocs["urls"].append(value)

    def pull_urlhaus(self):
        """Pull malicious URLs from URLhaus"""
        resp = requests.get("https://urlhaus.abuse.ch/downloads/csv_online/")
        for line in resp.text.split("\n"):
            if line.startswith("#") or not line.strip():
                continue
            parts = line.split(",")
            if len(parts) > 2:
                self.iocs["urls"].append(parts[2].strip('"'))

    def deduplicate(self):
        for key in self.iocs:
            self.iocs[key] = list(set(self.iocs[key]))

    def export(self, path):
        self.deduplicate()
        with open(path, "w") as f:
            json.dump({"generated": str(datetime.now()), "iocs": self.iocs}, f, indent=2)
        print(f"Exported {sum(len(v) for v in self.iocs.values())} IOCs to {path}")

# Usage
pipeline = CTIPipeline(otx_key="YOUR_KEY")
pipeline.pull_threatfox(days=1)
pipeline.pull_urlhaus()
pipeline.export("daily_iocs.json")
```

---

## Tips

- **IntelOwl** gives the broadest enrichment with a single API call — deploy it first
- **OpenCTI** is the best self-hosted platform — run via Docker, the public demo is unreliable
- **ThreatFox + URLhaus** from abuse.ch are the highest-quality free IOC feeds
- **MITRE ATT&CK GitHub JSON** is more reliable than their TAXII endpoint for automation
- **CISA KEV JSON feed** is the best free vulnerability intelligence — no auth needed
- **Pulsedive** is excellent for quick IOC risk scoring without many API keys
- Automate daily feed pulls and delta-compare against your existing blocklists

---

## Removed / Dead Links (Verified April 2025)

| Site | Status | Reason |
|------|--------|--------|
| `misp.seccodeid.com` | Offline | DNS does not resolve |
| `limo.anomali.com` | Offline | DNS does not resolve — Anomali shut down free Limo service |
| `ais.cisa.gov/taxii2/` | Offline | DNS does not resolve |
| `demo.opencti.io` | Removed | Public demo unreliable — self-host via Docker instead |

---

*Reference: [OSINT Cheat Sheet — SOC & Threat Hunting, Researching Cyber Threats sections](https://github.com/Jieyab89/OSINT-Cheat-sheet) by [Jieyab89](https://github.com/Jieyab89)*