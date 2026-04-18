# Cryptocurrency Transaction Tracing

> *Tools sourced from [OSINT Cheat Sheet](https://github.com/Jieyab89/OSINT-Cheat-sheet) by [Jieyab89](https://github.com/Jieyab89)*

## Objective
Trace cryptocurrency payments associated with ransomware, dark web markets,
extortion, and other illicit activity — using public blockchain explorers,
graph analysis tools, and exchange intelligence.

> **Note**: All tools listed here use publicly available blockchain data.
> Blockchain transactions are fully public — tracing is legal OSINT.
> Do not attempt to seize, redirect, or interfere with any funds.

---

## 1. Blockchain Explorers (Per Chain)

### Bitcoin (BTC)
```
https://www.blockchain.com/explorer     → General purpose BTC explorer
https://explorer.btc.com                → BTC explorer
https://mempool.space                   → Mempool + UTXO explorer (very detailed)
https://blockchair.com/bitcoin          → Multi-chain explorer with analytics
https://btcscan.org                     → Clean BTC scanner

# Search by: wallet address, TXID, block number
```

### Ethereum (ETH) & ERC-20
```
https://etherscan.io                    → Standard ETH explorer
https://etherscam.com                   → Known scam addresses
https://blocksec.com                    → Blockchain security analytics
```

### Monero (XMR) — Privacy Coin (Limited Tracing)
```
https://xmrchain.net                    → Monero explorer (limited, privacy-focused)
# Note: Monero is designed for privacy — tracing is very limited
# Ring signatures and stealth addresses obscure sender/receiver
```

### USDT / Tron (TRC-20)
```
https://tronscan.org                    → TRON/USDT TRC-20 explorer
# Popular in ransomware payments and dark web markets
```

### Other Chains
```
https://blockchair.com                  → Multi-chain: BTC, ETH, BCH, LTC, etc.
https://www.coingecko.com               → Market data + contract addresses
```

---

## 2. Crypto Intelligence Platforms

### Arkham Intelligence
```
# From Jieyab89's OSINT Cheat Sheet tips
https://platform.arkhamintelligence.com

# Features:
# - Wallet entity labeling (exchange, mixer, ransomware group, etc.)
# - Transaction graph visualization
# - Portfolio tracking
# - On-chain intelligence with AI entity identification
# - Links wallets to known entities (Binance, Coinbase, dark web markets)
```

### Breadcrumbs
```
https://breadcrumbs.app
# Free crypto investigation tool
# Visual graph: trace funds through multiple hops
# Label known entities (exchanges, mixing services)
# Export graph for reports

# How to use:
# 1. Input wallet address
# 2. Click "Investigate"
# 3. Expand transaction nodes
# 4. Look for connections to labeled entities (exchanges = on/off ramps)
```

### Crystal Blockchain (Commercial)
```
https://crystalblockchain.com
# Professional-grade crypto tracing
# Used by law enforcement and compliance teams
# Risk scoring for wallet addresses
```

### Chainalysis (Commercial, Free Tools Available)
```
https://www.chainalysis.com
# Industry standard for crypto compliance and investigations
# Free tool: https://www.chainalysis.com/free-cryptocurrency-sanctions-screening-tools/
```

---

## 3. Ransomware Wallet Tracking

Known ransomware wallets are often publicly documented:

```
# Ransomwhere — ransomware payment tracker
https://ransomwhe.re
https://ransomwhe.re/browse           → Browse reported ransomware payments

# From Jieyab89's Dataset list:
# "Browse ransomware data" → https://ransomwhe.re/#report

# Features:
# - Known ransomware payment addresses
# - Total amounts paid per group
# - Timeline of payments
# - Submit newly discovered wallets
```

### Searching Ransomware Wallets
```python
import requests

def check_ransomwhere(address):
    """Check if a Bitcoin address appears in ransomwhere.re"""
    url = f"https://api.ransomwhe.re/export"
    resp = requests.get(url)
    data = resp.json()
    for entry in data.get("result", []):
        if address in entry.get("address", ""):
            return entry
    return None

# Usage
result = check_ransomwhere("1BitcoinAddressHere")
if result:
    print(f"Ransomware family: {result.get('family')}")
    print(f"Total received: {result.get('balance')} BTC")
```

---

## 4. Blockchain Analytics Techniques

### Address Clustering
Multiple addresses controlled by same entity are often linked through:
- Common-input ownership (UTXO model)
- Change address patterns
- Timing correlation
- Dust attacks

```
# Blockchair supports basic clustering
https://blockchair.com/bitcoin/address/ADDRESS#cluster

# OXT — Bitcoin UTXO analytics
https://oxt.me/address/BITCOIN_ADDRESS
# Shows: cluster, related addresses, entity if known
```

### Following the Money (Step-by-Step)
```
1. Get starting address (from ransom note, report, payment screenshot)
2. Open in mempool.space or blockchain.com
3. Trace outgoing transactions
4. Look for consolidation points (many inputs → one output = aggregation wallet)
5. Check if final destination is a labeled exchange
6. Large exchange deposit → potential KYC record exists
7. Check Arkham/Breadcrumbs for entity labels
8. Cross-reference with known ransomware wallet databases
```

### Mixer / Tumbler Detection
```
Indicators of mixing services:
- Many equal-value outputs (e.g., 10x 0.1 BTC)
- Coinjoin transactions (many inputs, many outputs, equal amounts)
- Wasabi Wallet patterns
- Known mixer addresses:

# Sanction screening (OFAC SDN list)
https://sanctionssearch.ofac.treas.gov
# Check if wallet is under US Treasury sanctions (many ransomware wallets are)

# Chainalysis free screening
https://www.chainalysis.com/free-cryptocurrency-sanctions-screening-tools/
```

---

## 5. OFAC Sanctioned Crypto Addresses

Many ransomware operators have sanctioned wallets:

```
https://sanctionssearch.ofac.treas.gov
# US Treasury Office of Foreign Assets Control
# Search: individual name, entity name, or cryptocurrency address

# Also check:
https://home.treasury.gov/policy-issues/financial-sanctions/recent-actions
# Latest sanction actions — often includes crypto wallet addresses

# Blockchain analytics APIs that include OFAC checks:
https://www.chainalysis.com
https://crystalblockchain.com
```

---

## 6. Exchange Intelligence

When funds reach an exchange, there may be a KYC record:

```
# Identify exchange from address
https://www.blockchain.com/explorer    → Tagged addresses
https://blockchair.com                  → Entity labels
https://arkhamintelligence.com         → Exchange identification

# Known exchange deposit address patterns:
# - Binance: cluster of many deposit addresses pointing to hot wallet
# - Coinbase: tagged in blockchain.com
# - Kraken: similar clustering patterns

# If you identify an exchange:
# → Law enforcement can subpoena KYC records
# → Document the evidence trail before reporting
```

---

## Tips

- **Breadcrumbs** is the best free visual tool for quick crypto tracing
- **Arkham** is most powerful for entity identification — often labels wallets automatically
- **Mempool.space** gives the deepest BTC UTXO analysis for free
- **Ransomwhe.re** is the definitive database of known ransomware payment addresses
- **Always document** wallet addresses, transaction IDs, and block heights for evidence
- **Monero** tracing is severely limited by design — pivot to any BTC payments instead
- **OFAC sanctions list** is essential for identifying if a wallet is already flagged by US Treasury
- Blockchain analysis is a specialized field — for serious investigations, use **Chainalysis** or **Crystal**

---

*Reference: [OSINT Cheat Sheet — tips on crypto tracking & Collection Dataset sections](https://github.com/Jieyab89/OSINT-Cheat-sheet) by [Jieyab89](https://github.com/Jieyab89)*
