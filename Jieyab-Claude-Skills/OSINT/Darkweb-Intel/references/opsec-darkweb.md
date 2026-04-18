# OPSEC for Dark Web OSINT Investigations

> *Safety guidelines inspired by [OSINT Cheat Sheet](https://github.com/Jieyab89/OSINT-Cheat-sheet) by [Jieyab89](https://github.com/Jieyab89) — who emphasizes: "Please use it wisely"*

## Objective
Protect your identity, devices, and legal standing while conducting dark web
intelligence investigations. Poor OPSEC can expose your real identity to threat
actors, compromise your organization, or create legal liability.

---

## 1. Environment Setup

### Recommended Stack (Layered Isolation)
```
Layer 1 — Host Machine
  └── Your regular computer (never used for OSINT)

Layer 2 — Hypervisor
  └── VirtualBox / VMware / Proxmox
      └── Isolated OSINT VM (no shared clipboard, no shared folders)

Layer 3 — Network
  └── VPN (kill-switch enabled) → Tor (for .onion) or direct (for clearnet OSINT)

Layer 4 — Browser
  └── Tor Browser (for .onion access)
  └── Firefox with hardened settings (for clearnet OSINT tools)

Layer 5 — Identity
  └── Throwaway accounts (not linked to real name/email/phone)
  └── Dedicated OSINT email (ProtonMail, Tutanota)
```

### Recommended OSINT Linux Distros (from Jieyab89's list)
```
https://github.com/tracelabs/tlosint-live   → Trace Labs OSINT VM
https://tails.net                           → Amnesic OS (leaves no trace)
https://www.qubes-os.org                    → Compartmentalized OS
https://www.parrotsec.org                   → Parrot OS (security/OSINT)
https://csilinux.com                        → CSI Linux (OSINT-focused)
```

---

## 2. Network OPSEC

### VPN Configuration
```
Requirements for OSINT VPN:
✓ No-logs policy (independently audited)
✓ Kill switch enabled (cuts internet if VPN drops)
✓ DNS leak protection
✓ Jurisdiction outside 5/9/14-eyes if sensitive work

# Test for leaks before starting
https://www.dnsleaktest.com
https://ipleak.net
https://browserleaks.com
```

### Tor Browser (for .onion access)
```
Download: https://www.torproject.org/download/
# Always use the latest version
# Never resize the window (browser fingerprinting)
# Never log into personal accounts inside Tor Browser
# Disable JavaScript for sensitive .onion sites (Security Level: Safest)
# Never download files directly — preview in sandbox first

# Check your Tor exit node
https://check.torproject.org    (accessible via Tor Browser)
```

### Network Isolation
```bash
# Linux: create isolated network namespace for OSINT tools
ip netns add osint-ns
ip netns exec osint-ns ip link set lo up
# Route all OSINT tool traffic through VPN interface only

# Verify no direct connections from OSINT VM
# Disable all non-essential network interfaces in the VM
```

---

## 3. Identity OPSEC

### Account Hygiene
```
✓ Use throwaway/sock puppet accounts for any platform registration
✓ Never use real name, photo, or biographical info in OSINT accounts
✓ Use dedicated email (ProtonMail / Tutanota) created over Tor
✓ Never reuse usernames across platforms
✓ Use separate accounts for OSINT work vs personal use
✓ Generate usernames with no connection to your real identity

# Jieyab89's tip on accounts:
# "Do a active on each platform example like post, follow, following to 
#  avoid bot detection or blocked by user (target)"
# "Use second account (not your real account)"
```

### Browser Fingerprinting Protection
```
https://browserleaks.com          → Test your browser fingerprint
https://coveryourtracks.eff.org   → EFF Cover Your Tracks test

# Key fingerprint vectors to neutralize:
# - Screen resolution (use common size: 1920x1080)
# - User agent (use common browser UA)
# - Timezone (match VPN exit location)
# - WebRTC leaks (disable WebRTC in browser)
# - Canvas fingerprinting (block or randomize)
```

---

## 4. Device OPSEC

### Sandbox VM Rules
```
✓ Snapshot the VM before each investigation session
✓ Revert snapshot after sensitive sessions
✓ No shared clipboard between host and OSINT VM
✓ No shared folders — transfer files through encrypted container only
✓ Disable USB passthrough
✓ Use separate VM for different investigation cases (no cross-contamination)
✓ Enable AV in VM (Jieyab89's tip: "Enable your firewall, AV and IDS")
```

### File Handling (from Jieyab89's tips)
```
# Jieyab89's direct guidance:
"Dont upload your private files make sure you have clean personal file in folder"
"Scan the files will you download"
"Encrypt your network traffic, message and disk"
"Beware about attachments such as docx, xlsm or macro documents"
"Beware about malicious script like programm lang always check will you run it"
"beware with code with obfuscate (dont trust it)"

# NEVER:
✗ Open malware samples on your host machine
✗ Click links from threat actors without sandbox isolation
✗ Download dark web files to your main machine
✗ Enable macros in Office documents from dark web sources
```

### File Analysis Before Opening
```bash
# Check file type (don't trust extension)
file suspicious_file.exe

# Compute hashes before opening
sha256sum suspicious_file.exe
md5sum suspicious_file.exe

# Check hash on VirusTotal before any local analysis
# Submit hash only (not the file itself) for initial check

# Strings analysis (safe, no execution)
strings suspicious_file.exe | grep -E "(http|ftp|smtp|password|key|token)"

# Only then: open in an isolated sandbox (AnyRun, Hybrid Analysis, or local Cuckoo)
```

---

## 5. Legal OPSEC

### What Is Legal (OSINT)
```
✓ Accessing publicly available information
✓ Using clearnet dark web monitoring services
✓ Searching indexed dark web content (Ahmia, IntelX, DarkSearch)
✓ Analyzing published breach data for defensive purposes
✓ Tracking ransomware groups through their public leak sites
✓ Researching threat actors using public reports and CTI feeds
✓ Accessing DDO Secrets / OCCRP ALEPH (public interest journalism)
```

### What Is NOT Legal (Do Not Do)
```
✗ Registering accounts on criminal forums
✗ Purchasing stolen data, tools, or credentials
✗ Accessing systems without authorization
✗ Re-publishing stolen personal data of individuals
✗ Attempting to take down or interfere with criminal infrastructure
✗ Interacting with threat actors to elicit information (entrapment risk)
✗ Downloading CSAM or other illegal content (even for research)
```

### Jurisdiction Reference
```
Indonesia  → UU ITE No.11/2008 & No.19/2016 (amended)
            → UU PDP No.27/2022 (Personal Data Protection)
USA        → Computer Fraud and Abuse Act (18 U.S.C. § 1030)
            → Electronic Communications Privacy Act
EU         → GDPR (data handling), Directive on Attacks Against Information Systems
Global     → ICCPR Article 17 (right to privacy)
```

---

## 6. Evidence Collection & Chain of Custody

When findings may be used in legal proceedings or incident reports:

```
# Capture with timestamp
date && screenshot

# Archive web pages with timestamp proof
https://archive.today                  → Submit URL → get archived link
https://web.archive.org/save/URL       → Wayback Machine save

# Hash all collected evidence
sha256sum evidence_file > evidence_file.sha256

# Maintain investigation log
[TIMESTAMP] [ACTION] [SOURCE] [FINDING] [HASH]

# Never alter original evidence files
# Store in encrypted container (VeraCrypt)
# Maintain chain of custody documentation
```

---

## 7. Operational Security Checklist

### Before Starting an Investigation
```
[ ] OSINT VM is up-to-date and snapshoted
[ ] VPN is connected and verified (no leaks)
[ ] Tor Browser is latest version (if needed)
[ ] Throwaway accounts ready
[ ] AV/firewall enabled in sandbox
[ ] Investigation scope and legal boundaries are clear
[ ] Evidence folder created with encrypted container
```

### During Investigation
```
[ ] No personal accounts used
[ ] All URLs previewed before clicking (urlscan.io)
[ ] Files scanned before analysis
[ ] Screenshots taken with timestamps
[ ] Sources documented as you go
[ ] No interaction with threat actors
```

### After Investigation
```
[ ] Evidence archived and hashed
[ ] Investigation log complete
[ ] VM snapshot taken (or reverted if sensitive)
[ ] VPN disconnected after session
[ ] Report drafted with source citations
```

---

## Tips

- **Tails OS** is the gold standard for leaving zero traces — use for most sensitive work
- **Qubes OS** provides the best compartmentalization if Tails is too limiting
- **Never combine** personal and OSINT activities in the same browser session
- **Document everything** as you go — memory is unreliable, investigations can take weeks
- Follow Jieyab89's golden rule: **"Use virtual machine, fake host or docker machine"**
- When in doubt about legality — **consult a lawyer before proceeding**, not after

---

*Safety guidance informed by [OSINT Cheat Sheet — Tips & Trick Safe Guide](https://github.com/Jieyab89/OSINT-Cheat-sheet) by [Jieyab89](https://github.com/Jieyab89).*
*His words: "Please use it wisely."*
