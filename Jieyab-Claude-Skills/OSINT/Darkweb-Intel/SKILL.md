---
name: osint-darkweb-intel
description: >
  Comprehensive guide for Dark Web OSINT Intelligence — monitoring threat actor activity,
  ransomware group tracking, leak site enumeration, IOC collection from dark web sources,
  breach data discovery, paste site monitoring, CTI (Cyber Threat Intelligence) from
  underground forums, cryptocurrency transaction tracing, and dark web search techniques.
  All methods are PASSIVE and use publicly accessible intelligence feeds, clearnet proxies,
  and monitoring services — no illegal access required. Use this skill WHENEVER the user
  asks about dark web monitoring, threat intel, ransomware tracking, underground forum
  intelligence, dark web OSINT, CTI from dark sources, leak site monitoring, stealer
  log analysis, threat actor profiling, or any investigation involving dark web content.
---

# OSINT Dark Web Intelligence Skill

> **Credits**: Tool references and methodology sourced from the
> [OSINT Cheat Sheet](https://github.com/Jieyab89/OSINT-Cheat-sheet) by
> **[Jieyab89](https://github.com/Jieyab89)** — a comprehensive, community-driven
> OSINT resource covering tools, datasets, techniques, and tips for security
> researchers, journalists, investigators, and CTF players. All credit for the
> tool collection goes to him. Please use responsibly and wisely.

This skill covers **passive** dark web intelligence gathering — all techniques
access dark web content through clearnet proxies, monitoring services, aggregators,
and indexed feeds. **No Tor browser required for most techniques.**

> ⚠️ **Ethics & Legal Notice**
> - Use ONLY for legitimate purposes: threat intelligence, authorized research,
>   investigative journalism, incident response, CTF, and law enforcement support
> - Do NOT join, register, purchase, or interact with criminal forums/markets
> - Do NOT facilitate, assist, or enable any illegal activity
> - Comply with local law: Indonesia UU ITE, US CFAA 18 U.S.C. § 1030, EU GDPR
> - Use a sandbox VM + VPN for any active browsing; never from your real identity
> - Following Jieyab89's tip: use fake accounts, sandbox machines, enable AV/firewall

---

## INTELLIGENCE MODULES — Read Reference Files as Needed

| Module | Reference File | When to Use |
|--------|---------------|-------------|
| Dark Web Search & Indexing | `references/darkweb-search.md` | Search dark web content from clearnet |
| Ransomware Group Tracking | `references/ransomware-tracking.md` | Monitor ransomware gangs, victim lists |
| Breach & Leak Intelligence | `references/breach-leak-intel.md` | Breach forums, stealer logs, dump sites |
| Threat Actor Profiling | `references/threat-actor-profiling.md` | APT groups, TTPs, attribution |
| Cryptocurrency Tracing | `references/crypto-tracing.md` | Trace crypto payments, wallet clustering |
| Malware & IOC Intelligence | `references/malware-ioc-intel.md` | Malware samples, C2, IOC feeds |
| CTI Feeds & Platforms | `references/cti-feeds-platforms.md` | Threat intel feeds, MISP, OTX, etc. |
| Paste & Leak Monitoring | `references/paste-leak-monitoring.md` | Monitor paste sites and public leaks |
| OPSEC for Dark Web OSINT | `references/opsec-darkweb.md` | Safe investigation procedures |

---

## INVESTIGATION WORKFLOW

### Phase 1 — Define Intelligence Requirement

Before starting, clarify:
1. **Target**: Threat actor? Ransomware group? Specific breach? Organization exposure?
2. **Type**: Passive monitoring? Historical research? Incident response?
3. **Timeframe**: Recent (last 30 days)? Historical? Ongoing?
4. **Output**: IOC list? Threat report? Executive summary? Timeline?

### Phase 2 — Clearnet First (Safe, No Tor Needed)

```
Start with public intelligence aggregators:

1. Search dark web indexes (Ahmia, DarkSearch via clearnet)
2. Check ransomware tracking dashboards
3. Query breach/leak intelligence platforms
4. Pull IOC feeds from threat intel services
5. Check paste site aggregators
6. Query cryptocurrency explorer (if financial traces needed)
7. Cross-reference APT group databases
```

### Phase 3 — Specialized Intelligence Platforms

```
8.  Stealthmole / Flare / Recorded Future (commercial dark web monitoring)
9.  Hudson Rock (stealer log intelligence)
10. IntelX (dark web indexed content)
11. DeepDark CTI feeds
12. Ransomware.live / ransomwatch (gang tracking)
```

### Phase 4 — Structured Report

```
INTELLIGENCE REPORT
===================
Date           : [date]
Target / Actor : [name / group]
Confidence     : [Low / Medium / High]

[EXECUTIVE SUMMARY]

[ACTOR PROFILE]
  - Known aliases
  - Affiliated groups
  - TTPs (MITRE ATT&CK)
  - Active since

[TECHNICAL INDICATORS]
  - IOCs (IPs, domains, hashes, URLs)
  - Malware families
  - Infrastructure

[DARK WEB PRESENCE]
  - Forums mentioned
  - Leak sites
  - Victim claims

[CRYPTOCURRENCY]
  - Wallet addresses
  - Transaction patterns

[TIMELINE OF ACTIVITY]

[SOURCES]

[RECOMMENDED ACTIONS]
```

---

## QUICK REFERENCE — Clearnet Dark Web Intelligence

### Dark Web Search (No Tor Required)
```
https://ahmia.fi                          → Tor hidden service search engine
https://darksearch.io                     → Dark web search engine (clearnet)
https://www.osintframework.com            → OSINT framework with dark web section
https://osint.rocks                       → Multi-source OSINT including dark sources
```

### Ransomware Tracking
```
https://www.ransomware.live               → Live ransomware victim tracker
https://ransomwatch.telemetry.ltd         → Ransomwatch group monitoring
https://www.ransom-db.com                 → Ransomware database
https://ransom.privtools.eu               → Ransomware posts aggregator
https://id-ransomware.malwarehunterteam.com → Ransomware identification
https://www.nomoreransom.org              → Decryption tools
https://watchguard.com/wgrd-security-hub/ransomware-tracker → Watchguard tracker
```

### Breach & Leak Intelligence
```
https://intelx.io                         → Intelligence X (dark web indexed)
https://breachdirectory.org               → Breach directory
https://search.0t.rocks                   → Open breach database
https://leakix.net                        → Exposed service & leak intelligence
https://www.hudsonrock.com/threat-intelligence-cybercrime-tools → Stealer intel
https://whiteintel.io                     → Stealer log intelligence
https://breach.house                      → Stealer/breach aggregator
```

### CTI Platforms
```
https://otx.alienvault.com               → AlienVault OTX (free, community)
https://www.talosintelligence.com        → Cisco Talos
https://pulsedive.com                    → Pulsedive CTI
https://www.threatminer.org              → ThreatMiner
https://threatfox.abuse.ch               → ThreatFox IOC database
https://www.virustotal.com               → VirusTotal intelligence
https://malpedia.caad.fkie.fraunhofer.de → Malware encyclopedia
https://attack.mitre.org                 → MITRE ATT&CK framework
```

### Malware & IOC Feeds
```
https://bazaar.abuse.ch/browse           → MalwareBazaar samples
https://urlhaus.abuse.ch                 → Malicious URL feed
https://threatfox.abuse.ch               → IOC feed
https://vx-underground.org               → Malware sample archive
https://malpedia.caad.fkie.fraunhofer.de → Malware families
https://www.malware-traffic-analysis.net → PCAP & malware traffic analysis
```

### Crypto Tracing
```
https://www.blockchain.com/explorer      → Bitcoin explorer
https://etherscan.io                     → Ethereum explorer
https://www.arkham.io                    → Crypto intelligence (Jieyab89's tip)
https://explorer.btc.com                 → BTC explorer
https://tronscan.org                     → TRON explorer
https://breadcrumbs.app                  → Crypto wallet graph
```

---

## OPSEC QUICK CHECKLIST

- [ ] Use isolated sandbox VM (not your main machine)
- [ ] Route through VPN before any browsing
- [ ] Use Tor Browser for any .onion access (separate from daily browser)
- [ ] Use fake/throwaway accounts — never your real identity
- [ ] Enable antivirus + firewall on sandbox
- [ ] Do not download files from dark web to your host machine
- [ ] Do not screenshot content that could identify you
- [ ] Never interact with, purchase from, or register on criminal forums
- [ ] Keep notes in encrypted container (VeraCrypt recommended)
- [ ] Disconnect VM from network when not actively investigating

---

## REFERENCE FILES

Load relevant reference based on investigation type:

- `references/darkweb-search.md`         → Search & indexing techniques
- `references/ransomware-tracking.md`    → Ransomware group intelligence
- `references/breach-leak-intel.md`      → Breach & stealer log analysis
- `references/threat-actor-profiling.md` → APT/actor attribution & TTPs
- `references/crypto-tracing.md`         → Cryptocurrency transaction analysis
- `references/malware-ioc-intel.md`      → Malware samples & IOC collection
- `references/cti-feeds-platforms.md`    → CTI platforms & feed integration
- `references/paste-leak-monitoring.md`  → Paste & public leak monitoring
- `references/opsec-darkweb.md`          → Full OPSEC procedures

---

*Tool list and methodology sourced from the
[OSINT Cheat Sheet](https://github.com/Jieyab89/OSINT-Cheat-sheet)
by [Jieyab89](https://github.com/Jieyab89).
Use responsibly, ethically, and legally.*
