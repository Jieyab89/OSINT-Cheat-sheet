#!/usr/bin/env python3
import time
import json
import requests
import signal
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent

OUTPUT_FILE = (BASE_DIR / "output.json").resolve() # Conf w your path!

INTERVAL = 60 * 60  # 1 hour for scrapper and daemon
RUNNING = True

# =========================
# SIGNAL HANDLER
# =========================
def shutdown(signum, frame):
    global RUNNING
    RUNNING = False

signal.signal(signal.SIGINT, shutdown)
signal.signal(signal.SIGTERM, shutdown)

# =========================
# HELPERS
# =========================
def now():
    return datetime.now(UTC).isoformat()

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

# =========================
# TOR SESSION AND CONF
# =========================
def tor_session():
    for port in (9150, 9050):
        try:
            s = requests.Session()
            s.proxies = {
                # Windows 
                # "http": f"socks5h://127.0.0.1:{port}",
                # "https": f"socks5h://127.0.0.1:{port}",
                # Linux 
                "http": f"socks4://127.0.0.1:{port}",
                "https": f"socks4://127.0.0.1:{port}",
            }
            s.headers["User-Agent"] = "Mozilla/5.0 (Tor; OnionDirectoryIndexer)"
            s.get("http://check.torproject.org", timeout=10)
            return s
        except:
            continue
    raise RuntimeError("Tor not available")

# =========================
# EXTRACTOR
# =========================
def extract_onions(html, source):
    soup = BeautifulSoup(html, "html.parser")
    results = []

    for a in soup.find_all("a", href=True):
        href = a["href"]
        if ".onion" not in href:
            continue

        url = normalize_onion(href)
        if not url:
            continue

        results.append({
            "title": a.get_text(strip=True)[:120],
            "link": url,
            "source": source
        })

    return results

# =========================
# SAFE DIRECTORY SOURCES
# =========================
COLLECTORS = {

    # ======================================
    # ADDED THE ONION LIST DIRECTORY SITE
    # ======================================

    # === CORE DARKWEB DIRECTORIES (WAJIB) ===
    "dark.fail": "https://dark.fail/",
    "ahmia": "https://ahmia.fi/",
    "onionlinks": "https://onionlinks.com/",
    "tordex": "https://www.tordex.app/",

    # Onion / Tor
    "torch66": "http://tor66sewebgixwhcqfnp5inzp5x5uohhdy3kvtnyfxc2e5mxiuh34iid.onion/",
    "deepweblinks": "http://darkwev6xtagl7742tqu24v2j4namr5ocfsfpha74a5nh4bwyp27a3ad.onion/",
    "onionland-search": "http://3bbad7fauom4d6sgppalyqddsqbf5u5p56b5k5uk2zxsy3d6ey2jobad.onion/",
    "torlinks": "http://torlinksge6enmcyyuxjpjkoouw4oorgdgeo7ftnq3zodj7g2zxi3kyd.onion/",
    "deep-search": "http://search7tdrcvri22rieiwgi5g46qnwsesvnubqav2xakhezv4hjzkkad.onion/",
    "excavator": "http://2fd6cemt4gmccflhm6imvdfvli3nf7zn6rfrwpsy7uhxrgbypvwf5fad.onion/",
    "darksearch": "http://darkzqtmbdeauwq5mzcmgeeuhet42fhfjj4p5wbak3ofx2yqgecoeqyd.onion/",
    "torwatch": "http://xq5hcm32m7ipdqt2ydqj6cc7lpj3lw3iwqnxiak2juynysoevjmancad.onion/",
    "duckduckgo": "https://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion/",
    "danex": "http://danexio627wiswvlpt6ejyhpxl5gla5nt2tgvgm2apj2ofrgm44vbeyd.onion/",
    "grams": "http://grams64rarzrk7rzdaz2fpb7lehcyi7zrrf5kd6w2uoamp7jw2aq6vyd.onion/",
    "torgle": "http://iy3544gmoeclh5de6gez2256v6pjh4omhpqdh2wpeeppjtvqmjhkfwad.onion/",
    "tordex": "http://tordexu73joywapk2txdr54jed4imqledpcvcuf75qsas2gwdgksvnyd.onion/",
    "freshonion": "http://freshonifyfe4rmuh6qwpsexfhdrww7wnt5qmkoertwxmcuvm4woo4ad.onion/",
    "Logen.int": "http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/",
    "Logen.int": "http://3fzh7yuupdfyjhwt3ugzqqof6ulbcl27ecev33knxe3u7goi3vfn2qqd.onion",
    "Logen.int": "http://uquroyobsaquslaunwkz6bmc3wutpzvwe7mv62xeq64645a57bugnsyd.onion",
    "Logen.int": "http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/cgi-bin/omega/omega",
    "Hidden Wiki blog": "http://darkwebp7lyr44rpgqdtevalty2pk5oqmc6m2cnicnix7itelt3lp3id.onion/",
    "Onionx": "http://onionxpwovutq7bfv54ees3sfhcj32euy4bd555vvc4aufemxhkzvoyd.onion", 
    "Darksearch": "http://darkzqtmbdeauwq5mzcmgeeuhet42fhfjj4p5wbak3ofx2yqgecoeqyd.onion", 
    "OnionFind": "http://ofinde3b67voi7xiq3qflof2mwriwngicd7glwvf3bclgdgcjfozlzqd.onion/", 
    "SearchXNG": "http://searx3aolosaf3urwnhpynlhuokqsgz47si4pzz5hvb7uuzyjncl2tid.onion/", 
    "4GET": "http://4getwebfrq5zr4sxugk6htxvawqehxtdgjrbcn2oslllcol2vepa23yd.onion",
    "DeepLink": "http://deepxfmkjlils3vd7bru5rrxy3x3lchjgmv3wsgycjfynktmuwgm64qd.onion",
    "breaking bad forums" : "http://bbzzzsvqcrqtki6umym6itiixfhni37ybtt7mkbjyxn2pgllzxf2qgyd.onion",

    # Clearnet (darkweb directory / tracker)
    "darkwebdaily.net": "https://darkwebdaily.net/",
    "daut.link": "https://daunt.link/",
    "tor taxi": "https://tor.taxi/",
    "darkwebdaily": "https://darkwebdaily.live/",
    "immuniweb": "https://www.immuniweb.com/darkweb/",
    "ransomwatch": "https://ransomwatch.telemetry.ltd/",
    "watchguard": "https://www.watchguard.com/wgrd-security-hub/ransomware-tracker",
    "onionlive": "https://onion.live/",
    "torlink": "https://tor.link/",
    "onionland": "https://onionland.io/",
    "dargle": "https://www.dargle.net/domains",
    "torry": "https://www.torry.io/",
    "onionlandse": "https://onionlandsearchengine.net/",
    "torsearch": "https://torsearch.com/",
    "onionlinkhub": "https://www.onionlinkhub.com/",
}

# =========================
# MAIN DAEMON LOOP
# =========================
def main():
    print("[*] Onion directory daemon started")

    while RUNNING:
        try:
            session = tor_session()
            index = load_index()

            index_map = {
                onion_domain(i["link"]): i
                for i in index
                if onion_domain(i.get("link"))
            }

            added = 0

            for source, url in COLLECTORS.items():
                try:
                    r = session.get(url, timeout=45)
                    for item in extract_onions(r.text, source):
                        domain = onion_domain(item["link"])
                        if not domain:
                            continue

                        if domain in index_map:
                            index_map[domain]["updated_date"] = now()
                        else:
                            item["stored_date"] = now()
                            item["updated_date"] = item["stored_date"]
                            index_map[domain] = item
                            added += 1
                except:
                    continue

            if added > 0:
                save_index(list(index_map.values()))
                print(f"[+] Added {added} new domains (total {len(index_map)})")
            else:
                print("[=] No new domains found")

        except Exception as e:
            print("[!] Error:", e)

        # Sleep with graceful stop
        for _ in range(INTERVAL):
            if not RUNNING:
                break
            time.sleep(1)

    print("[*] Onion directory daemon stopped cleanly")

if __name__ == "__main__":
    main()
