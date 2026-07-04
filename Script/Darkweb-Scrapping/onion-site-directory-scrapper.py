#!/usr/bin/env python3
import time
import json
import requests
import signal
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from pathlib import Path
from datetime import datetime, timezone

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_FILE = (BASE_DIR / "output.json").resolve() # U can custom your relative path!

INTERVAL = 60 * 60 # U can custom the interval 
RUNNING = True

# =========================
# SIGNAL HANDLER
# =========================
def shutdown(signum, frame):
    global RUNNING
    RUNNING = False

# Only intercept SIGTERM. Let SIGINT raise KeyboardInterrupt for responsive Ctrl+C handling.
signal.signal(signal.SIGTERM, shutdown)

# =========================
# HELPERS
# =========================
def now():
    return datetime.now(timezone.utc).isoformat()  # FIX 1: UTC → timezone.utc

def onion_domain(url):
    try:
        return urlparse(url).netloc.lower()
    except:
        return None

def normalize_onion(url):
    try:
        p = urlparse(url)
        if ".onion" not in p.netloc:
            return None
        return f"{p.scheme}://{p.netloc}/"
    except:
        return None

# =========================
# LOAD / SAVE INDEX
# =========================
def load_index():
    if OUTPUT_FILE.exists():
        return json.loads(OUTPUT_FILE.read_text(encoding="utf-8"))
    return []

def save_index(data):
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

# ==================================
# TOR SESSION and CONFIG Global 
# ==================================
def tor_session():
    for port in (9150, 9050):
        try:
            s = requests.Session()
            s.proxies = {
                "http":  f"socks5h://127.0.0.1:{port}",  
                "https": f"socks5h://127.0.0.1:{port}",
            }
            s.headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36" # u can custom the user agent here
            print(f"[INFO] Trying Tor port {port}...")
            s.get("http://check.torproject.org", timeout=10)
            print(f"[+] Tor connected via port {port}")
            return s
        except Exception as e:
            print(f"[!] Port {port} failed: {e}")
            continue
    raise RuntimeError(
        "Tor is not available on port 9150 or 9050. "
        "Linux OS: Settings in /etc/proxychains4.conf and /etc/tor/torrc\n"
        "Windows OS: Start Tor Browser or Tor Expert Bundle."
    )        
    # raise RuntimeError("Tor is not available on port 9150 or 9050. Settings in /etc/proxychains4.con and /etc/tor/torrc\n" "Windows OS start Tor Browser or Tor Expert Bundle")

# =========================
# EXTRACTOR GLOBAL 
# =========================
def extract_onions(html, source):
    soup = BeautifulSoup(html, "html.parser")
    results = []
    seen = set()

    # FORMAT 1: dark.fail
    service_items = soup.find_all("div", class_="service-item")
    print(f"  [DEBUG] [{source}] Format1 found: {len(service_items)} service-item")

    for service in service_items:
        title_tag = service.find("a", class_="service-name")
        link_tag  = service.find("a", class_="link")

        if not title_tag or not link_tag:
            continue

        raw_url = link_tag.get("href", "")
        if ".onion" not in raw_url:
            continue

        url = normalize_onion(raw_url)
        if not url or url in seen:
            continue

        seen.add(url)
        results.append({
            "title": title_tag.get_text(strip=True)[:120],
            "link": url,
            "source": source
        })
        print(f"  [DEBUG] [{source}] Format1 OK - {title_tag.get_text(strip=True)[:40]} => {url}")

    # FORMAT 2: TorLinks style
    all_anchors = soup.find_all("a", href=True)
    print(f"  [DEBUG] [{source}] Format2 total anchors: {len(all_anchors)}")

    for a in all_anchors:
        href  = a["href"]
        title = a.get_text(strip=True)

        match = re.search(r'\((https?://[^)]+\.onion[^)]*)\)\s*$', href)
        if match:
            raw_url = match.group(1)
        elif ".onion" in href:
            raw_url = href
        else:
            continue

        url = normalize_onion(raw_url)
        if not url or url in seen:
            continue

        seen.add(url)
        results.append({
            "title": title[:120],
            "link": url,
            "source": source
        })
        print(f"  [DEBUG] [{source}] Format2 OK - {title[:40]} => {url}")

    # FORMAT 3: Deepdark-CTI
    md_matches = re.findall(r'\[([^\]]+)\]\((https?://[^\s\)]+\.onion[^\s\)]*)\)', html)
    print(f"  [DEBUG] [{source}] Format3 markdown matches: {len(md_matches)}")

    for title, raw_url in md_matches:
        url = normalize_onion(raw_url)
        if not url or url in seen:
            continue

        seen.add(url)
        results.append({
            "title": title.strip()[:120],
            "link": url,
            "source": source
        })
        print(f"  [DEBUG] [{source}] Format3 OK - {title.strip()[:40]} => {url}")

    print(f"  [DEBUG] [{source}] Total extracted: {len(results)} onions")
    return results

# ==================================================================
# COLLECTORS JIEYAB LOGEN.INT DARKWEB TRANSOFRM AND DATA SOURCE 
# ==================================================================
COLLECTORS = {
    # NOTES WILL UPDATE AS CAN WITH MY RESEARCH FOR DATA SOURCE "CHECK AT JIYEAB89 MAIN REPO FOR DARKWEB"
    # Clearnet directories (WAJIB)
    "dark.fail":        "https://dark.fail/",
    "ahmia":            "https://ahmia.fi/",
    "onionlinks":       "https://onionlinks.com/",
    "tordex-clearnet":  "https://www.tordex.app/",  

    # Onion — searchengines & directories (onion link lists)
    "torch66":          "http://tor66sewebgixwhcqfnp5inzp5x5uohhdy3kvtnyfxc2e5mxiuh34iid.onion/",
    "deepweblinks":     "http://darkwev6xtagl7742tqu24v2j4namr5ocfsfpha74a5nh4bwyp27a3ad.onion/",
    "onionland-search": "http://3bbad7fauom4d6sgppalyqddsqbf5u5p56b5k5uk2zxsy3d6ey2jobad.onion/",
    "torlinks":         "http://torlinksge6enmcyyuxjpjkoouw4oorgdgeo7ftnq3zodj7g2zxi3kyd.onion/",
    "deep-search":      "http://search7tdrcvri22rieiwgi5g46qnwsesvnubqav2xakhezv4hjzkkad.onion/",
    "excavator":        "http://2fd6cemt4gmccflhm6imvdfvli3nf7zn6rfrwpsy7uhxrgbypvwf5fad.onion/",
    "darksearch":       "http://darkzqtmbdeauwq5mzcmgeeuhet42fhfjj4p5wbak3ofx2yqgecoeqyd.onion/",
    "torwatch":         "http://xq5hcm32m7ipdqt2ydqj6cc7lpj3lw3iwqnxiak2juynysoevjmancad.onion/",
    "duckduckgo-onion": "https://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion/",
    "danex":            "http://danexio627wiswvlpt6ejyhpxl5gla5nt2tgvgm2apj2ofrgm44vbeyd.onion/",
    "grams":            "http://grams64rarzrk7rzdaz2fpb7lehcyi7zrrf5kd6w2uoamp7jw2aq6vyd.onion/",
    "torgle":           "http://iy3544gmoeclh5de6gez2256v6pjh4omhpqdh2wpeeppjtvqmjhkfwad.onion/",
    "tordex-onion":     "http://tordexu73joywapk2txdr54jed4imqledpcvcuf75qsas2gwdgksvnyd.onion/",  
    "freshonion":       "http://freshonifyfe4rmuh6qwpsexfhdrww7wnt5qmkoertwxmcuvm4woo4ad.onion/",

    # FIX: LOGEN.INT NAME TRANSFORM LOGEN.INT DATA SOURCE (WAJIB)
    "logen-1":          "http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/",
    "logen-2":          "http://3fzh7yuupdfyjhwt3ugzqqof6ulbcl27ecev33knxe3u7goi3vfn2qqd.onion",
    "logen-3":          "http://uquroyobsaquslaunwkz6bmc3wutpzvwe7mv62xeq64645a57bugnsyd.onion",
    "logen-4":          "http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/cgi-bin/omega/omega",

    "hidden-wiki-blog": "http://darkwebp7lyr44rpgqdtevalty2pk5oqmc6m2cnicnix7itelt3lp3id.onion/",
    "onionx":           "http://onionxpwovutq7bfv54ees3sfhcj32euy4bd555vvc4aufemxhkzvoyd.onion",
    "onionfind":        "http://ofinde3b67voi7xiq3qflof2mwriwngicd7glwvf3bclgdgcjfozlzqd.onion/",
    "searxng":          "http://searx3aolosaf3urwnhpynlhuokqsgz47si4pzz5hvb7uuzyjncl2tid.onion/",
    "4get":             "http://4getwebfrq5zr4sxugk6htxvawqehxtdgjrbcn2oslllcol2vepa23yd.onion",
    "deeplink":         "http://deepxfmkjlils3vd7bru5rrxy3x3lchjgmv3wsgycjfynktmuwgm64qd.onion",
    "breaking-bad-forums": "http://bbzzzsvqcrqtki6umym6itiixfhni37ybtt7mkbjyxn2pgllzxf2qgyd.onion",

    # LOGEN.INT GITHUB DATA SOURCES 
    "deepdarkcti-others":         "https://raw.githubusercontent.com/fastfire/deepdarkCTI/refs/heads/main/others.md",
    "deepdarkcti-ransomware":     "https://raw.githubusercontent.com/fastfire/deepdarkCTI/refs/heads/main/ransomware_gang.md",
    "deepdarkcti-rat":            "https://raw.githubusercontent.com/fastfire/deepdarkCTI/refs/heads/main/rat.md",
    "deepdarkcti-search-engines": "https://raw.githubusercontent.com/fastfire/deepdarkCTI/refs/heads/main/search_engines.md",
    "deepdarkcti-counterfeit":    "https://raw.githubusercontent.com/fastfire/deepdarkCTI/refs/heads/main/counterfeit_goods.md",
    "deepdarkcti-forum":          "https://raw.githubusercontent.com/fastfire/deepdarkCTI/refs/heads/main/forum.md",
    "deepdarkcti-maas":           "https://raw.githubusercontent.com/fastfire/deepdarkCTI/refs/heads/main/maas.md",
    "deepdarkcti-markets":        "https://raw.githubusercontent.com/fastfire/deepdarkCTI/refs/heads/main/markets.md",

    # Clearnet trackers (onion link lists)
    "darkwebdaily.net": "https://darkwebdaily.net/",
    "daunt.link":       "https://daunt.link/",
    "tor-taxi":         "https://tor.taxi/",
    "darkwebdaily":     "https://darkwebdaily.live/",
    "immuniweb":        "https://www.immuniweb.com/darkweb/",
    "ransomwatch":      "https://ransomwatch.telemetry.ltd/",
    "onionlive":        "https://onion.live/",
    "torlink":          "https://tor.link/",
    "onionland":        "https://onionland.io/",
    "dargle":           "https://www.dargle.net/domains",
    "torry":            "https://www.torry.io/",
    "onionlandse":      "https://onionlandsearchengine.net/",
    "torsearch":        "https://torsearch.com/",
    "onionlinkhub":     "https://www.onionlinkhub.com/",
}

# =========================
# MAIN DAEMON LOOP
# =========================
def main():
    print("[*] Onion directory daemon started")
    index_map = {}

    try:
        while RUNNING:
            try:
                session = tor_session() 
            except RuntimeError as e:
                print(f"[!] {e}")
                print(f"[!] Please check your TOR network....................")
                for _ in range(60):
                    if not RUNNING:
                        break
                    time.sleep(1)
                continue

            index     = load_index()
            index_map = {
                onion_domain(i["link"]): i
                for i in index
                if onion_domain(i.get("link"))
            }
            added = 0

            for source, url in COLLECTORS.items():
                if not RUNNING:
                    break
                try:
                    print(f"\n[INFO] Fetching [{source}] => {url}")
                    start = time.time()

                    r       = session.get(url, timeout=45)
                    elapsed = round(time.time() - start, 2)

                    print(f"[+] Response [{source}] status={r.status_code} size={len(r.text)} chars time={elapsed}s")

                    for item in extract_onions(r.text, source):
                        domain = onion_domain(item["link"])
                        if not domain:
                            continue

                        if domain in index_map:
                            # sudah ada, cuma update timestamp, gak perlu write ulang ke json
                            index_map[domain]["updated_date"] = now()
                        else:
                            item["stored_date"]   = now()
                            item["updated_date"]  = item["stored_date"]
                            index_map[domain]     = item
                            added += 1

                            # LANGSUNG SAVE begitu ketemu domain baru & unik
                            save_index(list(index_map.values()))
                            print(f"  [SAVE] +1 new unique domain saved => {domain} (total {len(index_map)})")        

                except requests.exceptions.Timeout:
                    print(f"[!] TIMEOUT [{source}]")
                except requests.exceptions.ConnectionError as e:
                    print(f"[!] CONNECTION ERROR [{source}]: {e}")
                except Exception as e:
                    print(f"[!] ERROR [{source}]: {type(e).__name__}: {e}")

            if added > 0:
                print(f"\n[+] Finished: +{added} new domains this cycle (total {len(index_map)})")
                added = 0
            else:
                print("\n[INFO] No new domains found")    

            print(f"[INFO] Sleeping {INTERVAL//60} minutes...")
            for _ in range(INTERVAL):
                if not RUNNING:
                    break
                time.sleep(1)

    except KeyboardInterrupt:
        print("\n[!] Process interrupted by user (Ctrl+C). Saving progress...")
        if index_map:
            save_index(list(index_map.values()))
            print(f"[+] Index saved to {OUTPUT_FILE} (total {len(index_map)} domains)")
        else:
            print("[-] Nothing to save.")

    print("[*] Daemon stopped cleanly")

if __name__ == "__main__":
    main()