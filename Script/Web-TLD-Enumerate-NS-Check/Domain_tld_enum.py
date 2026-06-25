#!/usr/bin/env python3
"""
Domain TLD Enumerator
======================
Example:
    python3 domain_tld_enum.py --name contohbrand
    python3 domain_tld_enum.py --name contohbrand --tlds com,id,su,st,cx
    python3 domain_tld_enum.py --name contohbrand --brute --brute-max-len 3
    python3 domain_tld_enum.py --name contohbrand --brute --no-common --brute-max-len 2
"""
import argparse
import concurrent.futures
import itertools
import json
import os
import re
import signal
import socket
import string
import sys
import time
import requests
import dns.resolver
try:
    from shutil import get_terminal_size
except ImportError:
    get_terminal_size = None
requests.packages.urllib3.disable_warnings()
DEFAULT_TIMEOUT = 6
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240"
class Colors:
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    BOLD = "\033[1m"
    RESET = "\033[0m"
    @staticmethod
    def disable():
        Colors.GREEN = Colors.RED = Colors.YELLOW = Colors.BOLD = Colors.RESET = ""
def green(text):
    return f"{Colors.GREEN}{text}{Colors.RESET}"
# Wordlist (TLD + ccTLD + gTLD + vanity)
COMMON_TLDS = [
    
    # All region
    "gov","mil","go.id","mil.id","gov.au","gov.br",
    "gov.cn","gov.hk","gov.in","gov.ir","gov.my","gov.pk",
    "gov.pl","gov.ro","gov.ru","gov.sg","gov.tr","gov.uk",
    "gob.ar","gob.bo","gob.cl","gob.ec","gob.es","gob.gt",
    "gob.hn","gob.mx","gob.ni","gob.pa","gob.pe","gob.sv",
    "gob.ve","govt.nz","gouv.fr","gc.ca","admin.ch","bund.de",
    "go.jp","go.kr","go.th","gov.ph","gov.vn","gov.za","gov.ng",
    "gov.eg","gov.il","gov.sa","gov.ae","gov.qa","gov.kw",
    "gov.om","gov.bh","gov.lk","gov.bd","gov.np","gov.mm",
    "gov.kh","gov.la","gov.tw","gov.mo","gov.fj","gov.ws",
    "gov.pg","gov.sb","gov.to","gov.vu","gov.mt","gov.cy",
    "gov.gr","gov.pt","gov.ie","gov.is","gov.no","gov.se",
    "gov.fi","gov.dk","gov.ee","gov.lv","gov.lt","gov.cz",
    "gov.sk","gov.hu","gov.si","gov.hr","gov.ba","gov.rs",
    "gov.me","gov.mk","gov.al","gov.bg","gov.md","gov.ua",
    "gov.by","gov.kz","gov.uz","gov.tm","gov.kg","gov.tj",
    "gov.mn","gov.ge","gov.am","gov.az",
    
    # int or secret 
    "int",
    
    # Core
    "com","net","org","info","biz","name","pro",
    
    # Startup
    "io","ai","app","dev","tech","cloud",
    "software","systems","digital","network",
    "security","email","tools",
    
    # Business
    "company","business","finance","capital",
    "ventures","partners","consulting",
    "solutions","services","support",
    
    # Content
    "blog","news","media","press",
    "wiki","community","forum",
    
    # Commerce
    "shop","store","market","shopping",
    "sale","deals",
    
    # Branding
    "xyz","online","site","website",
    "space","world","live","today",
    "agency","studio","design",
    "group","life","center","zone",
    
    # Indonesia
    "id","co.id","web.id","or.id",
    "ac.id","sch.id","my.id",
    
    # Southeast Asia
    "sg","my","th","vn","ph",
    "bn","kh","la","mm","cn",

    # East Asia 
    "jp","kr","tw","hk","mo",

    # South Asia
    "in","pk","bd","lk","np",

    # Europe
    "uk","co.uk","de","fr","nl",
    "it","es","pt","pl","ru",
    "se","no","fi","dk","ch",
    "at","be","cz","ro","hu",
    "sk","si","bg","ua","ie",
    "ee","lv","lt","lu","mt",
    "hr","rs","ba","al","mk",
    "gr","cy",
    
    # Americas
    "us","ca","mx","br","ar",
    
    # Millitary
    "mil","mil.id","mil.kr","mil.pk","mil.ru","mil.ng",
    "mil.za","mil.nz","mil.ph","mil.bd","mil.lk","mil.my",
    "mil.br","mil.ar","mil.pe","mil.bo","mil.py","mil.uy",
    "mil.ve","mil.ec","mil.co","mil.gt","mil.hn","mil.ni",
    "mil.sv","mil.pa","mil.do","mil.cu","mil.mx","mil.cl",
    
    # Oceania
    "au","nz",
    
    # Middle East
    "ae","sa","qa","tr",
    
    # Vanity
    "cc","tv","gg","vc","me",
    "fm","am","ws","to","sh",
    "is","ly","la","so","im",
    "bz","li","sc","ms","gd",
    "top","vip","icu","monster",
    "buzz","click","link","win",
    "fun","quest","su","st","cx",
    "ax","gd","im","as","pet","town",
    "sc","tk","ml","ga","cf","gq",
    "nu","cool","re","wf","tf",
    "pm","yt","nf","hn","moe","sx",
    "bf","co","pw","work","club",
    "one","ltd","sec","download",
    "rs","host","lol","ng","wtf","xxx",
    "ee","party","bot","ooo","cat","tx",
    "ovh","codes","trade","cfd","men","do",
    "best","ninja","pp.ua","ie","city",
    "rocks","bar","dog","run","red","ink",
    "service","services","family","works","work",
    "gay","buz","buzz","coffe","bio","toys",
    "money","cafe","love","fyi","pub","cash",
    "ne","page","domains","directory","tet",
    "tel","local","university","cheap","chruch",
    "inc","pizza","blue","legal","rentals","review",
    "taxi","casa","md","ma","rip","tours","capital",
    "recipes","audio","help","land","coach","guide",
    "foundation","er","watch","delivery","fund","gold",
    "cyou","computer","express","institute","reviews",
    "ventures","date","press","loan","ci","casino","band",
    "hg","ag","bet","ing","racing","game","kim","rest","vet",
    "af","tips","tax","wine","cv","cards","pink","earth","sex",
    "pics","cam","parts","part","fail","ge","ski","fe","mom",
    "eco","law","gy","baby","porn","vg","sucks","mc","duns",
    "srt","sbs","atas","zip","surf",
    
    # China
    "ren","shouji","tushu","wanggou","weibo","xihuan","xin",
    
    # Additional modern gTLD
    "team", "global", "care", "social",
    "video", "chat", "academy", "training",
    "events", "marketing", "exchange",
    "international", "technology","rock","art",
    "stream","games","sciene","ac","mobi","guru",
    "com.au","bid","travel","plus","systems","edu",
    "co.in","domain","photography","expert","tube",
    "arpa","abc",
    
]
def generate_brute_tlds(max_len=3, min_len=1):
    """
    Generate a-z string combinations with lengths ranging from min_len to max_len.
    WARNING:
    The number of combinations grows exponentially (26^n).
    Avoid setting max_len too high (>4) unless you are prepared for
    long execution times and possible DNS rate limiting.
    len 1  -> 26
    len 2  -> 676
    len 3  -> 17,576
    len 4  -> 456,976
    len 5  -> 11,881,376
    """
    letters = string.ascii_lowercase
    for length in range(min_len, max_len + 1):
        for combo in itertools.product(letters, repeat=length):
            yield "".join(combo)
def build_tld_list(args):
    """
    Build the TLD list according to the following priority order:
    1. Custom TLDs provided via --tlds (if specified)
    2. Common TLDs (unless --no-common is enabled)
    3. Brute-force generated a-z combinations (if --brute is enabled)
    The order is preserved to ensure that commonly used and
    high-value TLDs are processed first, followed by brute-force
    generated candidates.
    """
    tlds = []
    if args.tlds:
        tlds.extend([t.strip().lstrip(".") for t in args.tlds.split(",") if t.strip()])
    if not args.no_common:
        tlds.extend(COMMON_TLDS)
    if args.brute:
        brute_list = list(generate_brute_tlds(max_len=args.brute_max_len, min_len=args.brute_min_len))
        tlds.extend(brute_list)
    # dedupe, keep order (common tetap di depan, brute di belakang)
    seen = set()
    final = []
    for t in tlds:
        if t not in seen:
            seen.add(t)
            final.append(t)
    return final
def resolve_dns(domain):
    """Resolve A record. Return list IP or None"""
    try:
        answers = dns.resolver.resolve(domain, "A", lifetime=DEFAULT_TIMEOUT)
        return [str(r) for r in answers]
    except Exception:
        # fallback ke socket sebagai cadangan resolver
        try:
            ip = socket.gethostbyname(domain)
            return [ip]
        except Exception:
            return None
def resolve_ns(domain):
    """Resolve NS record. Return list nameserver or None."""
    try:
        answers = dns.resolver.resolve(domain, "NS", lifetime=DEFAULT_TIMEOUT)
        return [str(r).rstrip(".") for r in answers]
    except Exception:
        return None
def extract_title(html_text):
    if not html_text:
        return None
    match = re.search(r"<title[^>]*>(.*?)</title>", html_text, re.IGNORECASE | re.DOTALL)
    if match:
        title = re.sub(r"\s+", " ", match.group(1)).strip()
        return title[:200] if title else None
    return None
def check_http(url):
    """Request HTTP(S), return dict info"""
    try:
        resp = requests.get(
            url,
            timeout=DEFAULT_TIMEOUT,
            headers={"User-Agent": USER_AGENT},
            allow_redirects=True,
            verify=False,
        )
        return {
            "status_code": resp.status_code,
            "length": len(resp.content),
            "title": extract_title(resp.text),
            "server": resp.headers.get("Server"),
            "content_type": resp.headers.get("Content-Type"),
            "final_url": resp.url,
            "redirected": resp.url != url,
        }
    except requests.exceptions.SSLError:
        return {"error": "ssl_error"}
    except requests.exceptions.ConnectTimeout:
        return {"error": "connect_timeout"}
    except requests.exceptions.ConnectionError:
        return {"error": "connection_error"}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)[:120]}
def enumerate_one(name, tld):
    domain = f"{name}.{tld}"
    result = {
        "domain": domain,
        "tld": tld,
        "resolved": False,
        "ip": None,
        "ns": None,
        "http": None,
        "https": None,
    }
    ips = resolve_dns(domain)
    ns_records = resolve_ns(domain)
    result["ns"] = ns_records
    if ips or ns_records:
        result["resolved"] = True
        result["available_guess"] = False
    else:
        result["available_guess"] = True

    if not ips:
        return result
    result["ip"] = ips
    
    https_info = check_http(f"https://{domain}")
    result["https"] = https_info
    http_info = check_http(f"http://{domain}")
    result["http"] = http_info
    return result
def truncate(text, width):
    if text is None:
        return "-"
    text = str(text)
    if len(text) <= width:
        return text
    return text[: width - 1] + "…"
def get_combined_status(result):
    
    parts = []
    for scheme in ("https", "http"):
        info = result.get(scheme)
        if info is None:
            continue
        if "status_code" in info:
            parts.append(f"{scheme[0].upper()}:{info['status_code']}")
        elif "error" in info:
            parts.append(f"{scheme[0].upper()}:ERR")
    return ", ".join(parts) if parts else "-"
def get_combined_title(result):
    for scheme in ("https", "http"):
        info = result.get(scheme)
        if info and info.get("title"):
            return info["title"]
    return None
def get_combined_length(result):
    for scheme in ("https", "http"):
        info = result.get(scheme)
        if info and "length" in info:
            return info["length"]
    return None
def get_https_service(result):
    info = result.get("https")
    if info is None:
        return "-"
    if "status_code" in info:
        return f"yes ({info['status_code']})"
    if "error" in info:
        return f"no ({info['error']})"
    return "-"
def has_status_200(result):
    
    for scheme in ("https", "http"):
        info = result.get(scheme)
        if info and info.get("status_code") == 200:
            return True
    return False
def colorize_status(code_str, has_200):
    if has_200:
        return green(code_str)
    return code_str
def print_table_header(widths):
    headers = ["DOMAIN", "TLD", "HTTP/HTTPS CODE", "TITLE", "NS", "DNS", "HTTPS", "LENGTH"]
    def fmt_row(cells):
        return " | ".join(truncate(c, w).ljust(w) for c, w in zip(cells, widths))
    sep = "-+-".join("-" * w for w in widths)
    print(fmt_row(headers))
    print(sep)
TABLE_WIDTHS = [28, 8, 18, 26, 22, 8, 14, 8]
def format_table_row(r, widths=TABLE_WIDTHS, use_color=True):
    domain = r["domain"]
    tld = r["tld"]
    code = get_combined_status(r)
    title = get_combined_title(r)
    ns_list = r.get("ns")
    ns_str = ns_list[0] if ns_list else "-"
    if ns_list and len(ns_list) > 1:
        ns_str += f" (+{len(ns_list)-1})"
    is_up = r.get("resolved")
    dns_status = "UP" if is_up else "down"
    https_status = get_https_service(r)
    length = get_combined_length(r)
    has_200 = has_status_200(r)
    cells = [domain, tld, code, title, ns_str, dns_status, https_status, length]
    out = []
    for i, (c, w) in enumerate(zip(cells, widths)):
        text = truncate(c, w).ljust(w)
        if use_color:
            if i == 2 and has_200:  # HTTP/HTTPS CODE
                text = green(truncate(c, w)) + " " * (w - len(truncate(c, w)))
            elif i == 5 and is_up:  # DNS
                text = green(truncate(c, w)) + " " * (w - len(truncate(c, w)))
        out.append(text)
    return " | ".join(out)
def print_table(results, use_color=True):
    print_table_header(TABLE_WIDTHS)
    for r in results:
        print(format_table_row(r, use_color=use_color))
def state_path_for(output_path):
    base, _ = os.path.splitext(output_path)
    return f"{base}.state.json"
def load_state(state_file, name, planned_tlds):
    """Load checkpoint kalau cocok target_name dan TLD plan-nya sama. Return (results, done_tlds_set) atau (None, None) kalau tidak valid/tidak ada."""
    if not os.path.isfile(state_file):
        return None, None
    try:
        with open(state_file, "r", encoding="utf-8") as f:
            state = json.load(f)
    except Exception:
        return None, None
    if state.get("target_name") != name:
        return None, None
    if state.get("planned_tlds") != planned_tlds:
        return None, None
    results = state.get("results", [])
    done_tlds = {r["tld"] for r in results}
    return results, done_tlds
def save_state(state_file, name, planned_tlds, results):
    state = {
        "target_name": name,
        "planned_tlds": planned_tlds,
        "results": results,
    }
    tmp_file = f"{state_file}.tmp"
    with open(tmp_file, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False)
    os.replace(tmp_file, state_file)
def clear_state(state_file):
    try:
        os.remove(state_file)
    except FileNotFoundError:
        pass
def main():
    parser = argparse.ArgumentParser(
        description="Enumerate domain availability and metadata across multiple TLDs"
    )
    parser.add_argument(
        "--name",
        required=True,
        help="Domain name without TLD (e.g. examplebrand)"
    )
    parser.add_argument(
        "--tlds",
        help="Custom TLD list separated by commas (e.g. com,id,su,st,cx)"
    )
    parser.add_argument(
        "--no-common",
        action="store_true",
        help="Skip the built-in common TLD list"
    )
    parser.add_argument(
        "--brute",
        action="store_true",
        help="Enable brute-force generation of alphabetic TLD combinations (a-z)"
    )
    parser.add_argument(
        "--brute-min-len",
        type=int,
        default=1,
        help="Minimum brute-force TLD length (default: 1)"
    )
    parser.add_argument(
        "--brute-max-len",
        type=int,
        default=3,
        help=(
            "Maximum brute-force TLD length (default: 3). "
            "WARNING: combinations grow exponentially (26^n). "
            "len=3 -> 17,576 | len=4 -> 456,976 | "
            "len=5 -> 11.8 million. Recommended maximum: 3-4."
        ),
    )
    parser.add_argument(
        "--threads",
        type=int,
        default=30,
        help="Number of worker threads (default: 30)"
    )
    parser.add_argument(
        "--output",
        default="Results-tld-domain.json",
        help="Output JSON file path"
    )
    parser.add_argument(
        "--only-resolved",
        action="store_true",
        help="Only save domains that successfully resolve to an IP address"
    )
    parser.add_argument(
        "--only-200",
        action="store_true",
        help="Only save domains returning HTTP status 200"
    )
    parser.add_argument(
        "--no-color",
        action="store_true",
        help="Disable colored CLI output"
    )
    args = parser.parse_args()
    if args.no_color:
        Colors.disable()
    tlds = build_tld_list(args)
    if not tlds:
        print(
            "[!] No TLDs selected. Use --tlds or do not enable --no-common."
        )
        sys.exit(1)
    # Calculate how many TLDs come from the common list vs brute force
    n_common = 0 if args.no_common else len(COMMON_TLDS)
    n_brute = len(tlds) - n_common - (len(args.tlds.split(",")) if args.tlds else 0)
    print(f"[*] Target name: {args.name}")
    print(
        f"[*] Total TLDs to check: {len(tlds)} "
        f"(common: {n_common}, brute-force: {max(n_brute, 0)})"
    )
    print(f"[*] Worker threads: {args.threads}")
    print()
    if args.brute:
        print(
            f"[*] Brute-force TLD length range: "
            f"{args.brute_min_len}-{args.brute_max_len} characters"
        )
    results = []
    start = time.time()
    # IMPORTANT:
    # Process common TLDs first (DNS + HTTP + title + NS lookup),
    # then continue with brute-force generated TLDs.
    # This ensures high-value and commonly used TLDs are prioritized.
    common_set = set(COMMON_TLDS) if not args.no_common else set()
    ordered_tlds = sorted(
        tlds,
        key=lambda t: (t not in common_set, tlds.index(t))
    )
    state_file = state_path_for(args.output)
    prev_results, done_tlds = load_state(state_file, args.name, ordered_tlds)
    if prev_results:
        results = prev_results
        remaining_tlds = [t for t in ordered_tlds if t not in done_tlds]
        print(f"[*] Resuming from checkpoint: {len(done_tlds)} already checked, {len(remaining_tlds)} remaining")
        print()
    else:
        remaining_tlds = ordered_tlds
    print_table_header(TABLE_WIDTHS)
    for r in results:
        print(format_table_row(r, use_color=not args.no_color))
    pause_requested = {"flag": False}
    def handle_sigint(signum, frame):
        pause_requested["flag"] = True
    old_handler = signal.signal(signal.SIGINT, handle_sigint)
    aborted = False
    if remaining_tlds:
        try:
            with concurrent.futures.ThreadPoolExecutor(
                max_workers=args.threads
            ) as executor:
                futures = {
                    executor.submit(enumerate_one, args.name, tld): tld
                    for tld in remaining_tlds
                }
                for future in concurrent.futures.as_completed(futures):
                    tld = futures[future]
                    try:
                        res = future.result()
                    except Exception as e:
                        res = {
                            "domain": f"{args.name}.{tld}",
                            "tld": tld,
                            "resolved": False,
                            "error": str(e),
                        }
                    results.append(res)
                    print(format_table_row(res, use_color=not args.no_color))
                    if pause_requested["flag"]:
                        pause_requested["flag"] = False
                        signal.signal(signal.SIGINT, old_handler)
                        save_state(state_file, args.name, ordered_tlds, results)
                        choice = input(
                            f"\n[!] Paused. {len(results)}/{len(tlds)} checked, progress saved to {state_file}.\n"
                            f"    [c]ontinue / [a]bort: "
                        ).strip().lower()
                        if choice == "a":
                            aborted = True
                            for f in futures:
                                f.cancel()
                            break
                        signal.signal(signal.SIGINT, handle_sigint)
        except KeyboardInterrupt:
            save_state(state_file, args.name, ordered_tlds, results)
            aborted = True
            print(f"\n[!] Interrupted. {len(results)}/{len(tlds)} checked, progress saved to {state_file}.")
    signal.signal(signal.SIGINT, old_handler)
    if aborted:
        print(f"[*] Aborted. Resume later with the same --output to continue from {len(results)}/{len(tlds)}.")
        return
    clear_state(state_file)
    if args.only_resolved:
        results = [r for r in results if r.get("resolved")]
    if args.only_200:
        results = [r for r in results if has_status_200(r)]
    # Sort results:
    # 1. HTTP 200 domains first
    # 2. Resolved domains before unresolved ones
    # 3. Alphabetical by TLD
    results.sort(
        key=lambda r: (
            not has_status_200(r),
            not r.get("resolved"),
            r["tld"]
        )
    )
    
    print()
    output_data = {
        "target_name": args.name,
        "total_checked": len(tlds),
        "total_resolved": sum(
            1 for r in results if r.get("resolved")
        ),
        "total_status_200": sum(
            1 for r in results if has_status_200(r)
        ),
        "common_tlds_checked": n_common,
        "brute_force_checked": max(n_brute, 0),
        "elapsed_seconds": round(
            time.time() - start,
            2
        ),
        "results": results,
    }
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(
            output_data,
            f,
            indent=2,
            ensure_ascii=False
        )
    print(
        f"\n[+] Completed in "
        f"{output_data['elapsed_seconds']}s"
    )
    print(
        f"[+] {output_data['total_resolved']} / "
        f"{output_data['total_checked']} domains resolved"
    )
    print(
        f"[+] {output_data['total_status_200']} "
        f"domains returned HTTP 200"
    )
    print(
        f"[+] Results saved to: "
        f"{args.output}"
    )
    
if __name__ == "__main__":
    main()
