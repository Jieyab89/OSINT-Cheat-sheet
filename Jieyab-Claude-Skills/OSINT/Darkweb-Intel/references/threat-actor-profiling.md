# Threat Actor Profiling & Attribution

> *Tools sourced from [OSINT Cheat Sheet](https://github.com/Jieyab89/OSINT-Cheat-sheet) by [Jieyab89](https://github.com/Jieyab89)*

## Objective
Build structured intelligence profiles on threat actors — including APT groups,
ransomware operators, hacktivists, and cybercriminals — using public sources,
CTI frameworks, and dark web intelligence feeds.

---

## 1. MITRE ATT&CK Framework

The gold standard for mapping threat actor behavior:

```
https://attack.mitre.org/groups/           → All documented threat groups
https://attack.mitre.org/techniques/       → Full technique catalog
https://attack.mitre.org/software/         → Malware & tools per group
https://attack.mitre.org/campaigns/        → Campaign-level attribution

# Useful group pages
https://attack.mitre.org/groups/G0032/    → Lazarus Group (DPRK)
https://attack.mitre.org/groups/G0034/    → Sandworm (Russia)
https://attack.mitre.org/groups/G0007/    → APT28 / Fancy Bear
https://attack.mitre.org/groups/G0016/    → APT41 (China)
```

### ATT&CK Navigator — Visualize Group TTPs
```
https://mitre-attack.github.io/attack-navigator/
# Load a group's technique layer to visualize which TTPs they use
# Useful for: detection gap analysis, hunting hypothesis generation
```

---

## 2. APT Group Databases

### Google APT Search CSE
```
# From Jieyab89's SOC & Threat Hunting list
https://cse.google.com/cse?cx=003248445720253387346:turlh5vi4xc
# Search across multiple APT reporting sources simultaneously
```

### APT Group Spreadsheet
```
# From Jieyab89's list
https://docs.google.com/spreadsheets/u/1/d/1H9_xaxQHpWaa4O_Son4Gx0YOIzlcBWMsdvePFX68EKU/pubhtml
# Comprehensive APT group list with:
# - Group names and aliases
# - Nation-state attribution
# - Target sectors
# - Active years
```

### Malpedia — Actor Profiles
```
https://malpedia.caad.fkie.fraunhofer.de/actors
# Threat actor profiles linked to malware families
# Each actor page contains:
# - Aliases (different vendor names for same group)
# - Associated malware families
# - References to reporting
# - Country attribution
```

---

## 3. Threat Intelligence Platforms

### AlienVault OTX (Free, Community-Driven)
```
https://otx.alienvault.com

# Search by actor/group name
https://otx.alienvault.com/browse/pulses?q=APT28

# Get pulses for a domain/IP/hash
https://otx.alienvault.com/indicator/domain/target.com
https://otx.alienvault.com/indicator/ip/1.2.3.4
https://otx.alienvault.com/indicator/file/HASH

# API
curl -X GET "https://otx.alienvault.com/api/v1/indicators/domain/target.com/general" \
  -H "X-OTX-API-KEY: YOUR_KEY"
```

### Talos Intelligence (Cisco)
```
https://www.talosintelligence.com
https://www.talosintelligence.com/reputation_center

# Actor-specific reporting
https://blog.talosintelligence.com/?q=APT  → Search for APT blog posts
```

### Recorded Future (Commercial)
```
https://www.recordedfuture.com/vulnerability-database
# Free tier: some intelligence available without subscription
```

### Mandiant / Google TI
```
https://www.mandiant.com/advantage/threat-intelligence
https://cloud.google.com/security/products/threat-intelligence

# Free access to some reports and IOCs
# APT naming convention: APT1, APT28, etc.
```

### Falcon Feeds
```
# From Jieyab89's list
https://falconfeeds.io
# Dark web threat intelligence feeds
# Actor profiles and IOC collections
```

---

## 4. Building an Actor Profile

### Profile Template
```markdown
## Threat Actor Profile

**Name**: [Primary name]
**Aliases**: [Vendor-specific names — different vendors name same group differently]
**Attribution**: [Suspected nation-state or criminal group]
**Active Since**: [Year]
**Motivation**: [Financial / Espionage / Hacktivism / Disruption]

### Targeting
- **Sectors**: [Finance, Healthcare, Government, etc.]
- **Regions**: [Geographic focus]
- **Typical Victims**: [Organization types]

### TTPs (MITRE ATT&CK)
- Initial Access: [T1566 Phishing / T1190 Exploit Public-Facing Application]
- Execution: [T1059 Command and Scripting Interpreter]
- Persistence: [T1053 Scheduled Task/Job]
- C2: [T1071 Application Layer Protocol]
- Exfiltration: [T1041 Exfiltration Over C2 Channel]

### Malware & Tools
- [Malware family 1] — [description, Malpedia link]
- [Malware family 2]
- [Custom tooling]

### Infrastructure
- [Known C2 domains/IPs]
- [Hosting patterns]
- [Certificate patterns]

### Dark Web Presence
- [Forum aliases if known]
- [Ransomware leak site if applicable]
- [Communication channels]

### Key Reports
- [Vendor report 1 — link]
- [Vendor report 2 — link]

### IOCs
- Domains: []
- IPs: []
- Hashes: []
- YARA: []
```

---

## 5. Alias Resolution — Same Actor, Different Names

Vendors name the same group differently. Always cross-reference:

```
# APT28 aka:
# Fancy Bear (CrowdStrike), Sofacy (Kaspersky), Pawn Storm (Trend Micro),
# STRONTIUM (Microsoft), BlueDelta (Recorded Future), TA422 (Proofpoint)

# Lookup tool — resolve aliases
https://apt.etda.or.th/cgi-bin/listgroups.cgi     → ETDA APT alias resolver
https://malpedia.caad.fkie.fraunhofer.de/actors    → Malpedia with aliases
```

---

## 6. Dark Web Forum Actor Tracking

Track threat actor aliases across underground forums (clearnet intelligence):

```
# Search actor alias on clearnet
site:github.com "actor_alias"
site:pastebin.com "actor_alias"
"actor_alias" site:twitter.com OR site:x.com

# Threat intelligence reports mentioning the alias
"actor_alias" filetype:pdf site:mandiant.com
"actor_alias" filetype:pdf site:crowdstrike.com
"actor_alias" site:securelist.com

# Searchable CTI sources
https://otx.alienvault.com/browse/pulses?q=actor_alias
https://www.talosintelligence.com/        → Blog search
https://www.group-ib.com/resources/       → Group-IB reports
```

---

## 7. CTI Report Aggregators

```
https://www.cisa.gov/news-events/cybersecurity-advisories   → CISA advisories
https://www.ic3.gov/Media/News                              → FBI alerts
https://www.ncsc.gov.uk/section/reports-advisories/         → UK NCSC
https://www.cyber.gov.au/about-us/advisories               → Australian ASD
https://seclists.org/fulldisclosure/                        → Full disclosure list

# Community feeds
https://otx.alienvault.com                                  → OTX Pulses
https://www.virustotal.com/gui/collections                  → VT collections
https://yaraify.abuse.ch/yarahub/                           → YARA rules from community

# Indonesian context
https://bssn.go.id                                          → BSSN (ID national cyber agency)
https://www.idsirtii.or.id                                  → ID-SIRTII national CSIRT
```

---

## Tips

- **Malpedia** is the best single source for actor ↔ malware ↔ alias mapping
- **MITRE ATT&CK** is authoritative for TTP mapping — always map to it for consistency
- **APT alias confusion** is common — always check multiple vendor names before concluding
- **OTX Pulses** are often the fastest community source for newly emerging actor intelligence
- **ETDA APT list** is excellent for quickly resolving vendor naming differences
- **Attribution** should always include a confidence level — it's rarely 100% certain

---

*Reference: [OSINT Cheat Sheet — SOC & Threat Hunting & Researching Cyber Threats sections](https://github.com/Jieyab89/OSINT-Cheat-sheet) by [Jieyab89](https://github.com/Jieyab89)*
