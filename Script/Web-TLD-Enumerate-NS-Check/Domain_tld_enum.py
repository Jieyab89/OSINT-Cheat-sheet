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
import re
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
    "ac.id","sch.id","go.id","my.id",
    
    # Asia
    "sg","my","th","vn","ph","in",
    "jp","kr","cn","tw","hk",
    
    # Europe
    "uk","co.uk","de","fr","nl",
    "it","es","pt","pl","ru",
    "se","no","fi","dk","ch",
    "at","be","cz","ro","hu",
    "sk","si","bg","ua",
    
    # Americas
    "us","ca","mx","br","ar",
    
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
    "ax","gd","im","li","as","bz",
    "sc","tk","ml","ga","cf","gq",
    "nu","so","ms","re","wf","tf",
    "pm","yt","nf","hn",
    
    # Additional modern gTLD
    "team", "global", "care", "social",
    "video", "chat", "academy", "training",
    "events", "marketing", "exchange",
    "international", "technology",
    
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
def print_table(results, use_color=True):
    
    headers = ["ID", "DOMAIN", "TLD", "HTTP/HTTPS CODE", "TITLE", "NS", "DNS", "HTTPS", "LENGTH"]
    widths = [4, 28, 8, 18, 26, 22, 8, 14, 8]
    def fmt_row(cells, colors=None):
        out = []
        for i, (c, w) in enumerate(zip(cells, widths)):
            text = truncate(c, w).ljust(w)
            if colors and colors.get(i):
                # pad dulu baru kasih warna, supaya alignment tetap rapi
                text = colors[i](truncate(c, w)) + " " * (w - len(truncate(c, w)))
            out.append(text)
        return " | ".join(out)
    sep = "-+-".join("-" * w for w in widths)
    print(fmt_row(headers))
    print(sep)
    for idx, r in enumerate(results, start=1):
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
        if use_color:
            colors = {}
            if has_200:
                colors[3] = green  # HTTP/HTTPS CODE
            if is_up:
                colors[6] = green  # DNS
            print(fmt_row([str(idx), domain, tld, code, title, ns_str, dns_status, https_status, length], colors))
        else:
            print(fmt_row([str(idx), domain, tld, code, title, ns_str, dns_status, https_status, length]))
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
    with concurrent.futures.ThreadPoolExecutor(
        max_workers=args.threads
    ) as executor:
        futures = {
            executor.submit(enumerate_one, args.name, tld): tld
            for tld in ordered_tlds
        }
        done_count = 0
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
            done_count += 1
            if res.get("resolved"):
                tag = green("RESOLVED")
                if has_status_200(res):
                    tag = green("RESOLVED + HTTP 200")
            else:
                tag = "NO RESOLUTION"
            origin = "common" if tld in common_set else "brute"
            print(
                f"[{done_count}/{len(tlds)}] "
                f"({origin:6}) "
                f"{res['domain']:<32} {tag}"
            )
            results.append(res)
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
    print("===========TABLE VIEW==============")
    print_table(results, use_color=not args.no_color)
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
