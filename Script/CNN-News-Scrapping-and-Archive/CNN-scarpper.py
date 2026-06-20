import asyncio
import json
import os
import re
import signal
from datetime import datetime, UTC

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from playwright.async_api import async_playwright

SITEMAP_URLS = [
    "https://www.cnnindonesia.com/nasional/sitemap_web.xml",
    "https://www.cnnindonesia.com/internasional/sitemap_web.xml",
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240"
}

OUTPUT_DIR = "output"
RESULTS_FILE = "cnn_results.json"
STATE_FILE = "scraped_urls.json"

ARTICLE_DELAY = 3       # seconds, delay between articles so we don't hammer the server
CYCLE_SLEEP = 300       # seconds, pause between scraping cycles (5 minutes)
REQUEST_TIMEOUT = 60000 # ms, playwright goto timeout

# =========================
# GRACEFUL SHUTDOWN
# =========================
shutdown_event = asyncio.Event()


def handle_shutdown(sig, frame):
    print("\n[STOP] Shutdown signal received, finishing current task...")
    shutdown_event.set()


# =========================
# UTILS
# =========================
def safe_filename(text):
    return re.sub(r'[^a-zA-Z0-9]', '_', text)[:100]


def download_file(url, path):
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        if r.status_code == 200:
            with open(path, "wb") as f:
                f.write(r.content)
    except Exception:
        pass


def load_json_safe(path, default):
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return default
    return default


def load_scraped_urls():
    data = load_json_safe(STATE_FILE, [])
    return set(data)


def save_scraped_urls(urls_set):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(list(urls_set), f, ensure_ascii=False, indent=2)


def append_result(result):
    results = load_json_safe(RESULTS_FILE, [])
    results.append(result)
    with open(RESULTS_FILE, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=4)


# =========================================================
# GET SITEMAPS (unlimited, multiple sources)
# =========================================================
def get_urls():
    all_urls = []
    for sitemap_url in SITEMAP_URLS:
        try:
            res = requests.get(sitemap_url, headers=HEADERS, timeout=15)
            res.raise_for_status()
            soup = BeautifulSoup(res.text, "xml")
            urls = [loc.text.strip() for loc in soup.find_all("loc") if loc.text.strip()]
            print(f"[SITEMAP] {sitemap_url} -> {len(urls)} URLs")
            all_urls.extend(urls)
        except Exception as e:
            print(f"[ERROR] Failed to fetch sitemap {sitemap_url}: {e}")

    # dedupe while preserving order
    seen = set()
    deduped = []
    for u in all_urls:
        if u not in seen:
            seen.add(u)
            deduped.append(u)
    return deduped


# =========================
# SCRAPE + ARCHIVE
# =========================
async def scrape_article(page, url):
    try:
        await page.goto(url, timeout=REQUEST_TIMEOUT)
        await page.wait_for_selector("h1", timeout=15000)
        html = await page.content()
        soup = BeautifulSoup(html, "html.parser")

        h1 = soup.select_one("h1")
        if not h1:
            print(f"[SKIP] No title found: {url}")
            return None
        title = h1.get_text(strip=True)
        slug = safe_filename(title)
        base_dir = f"{OUTPUT_DIR}/{slug}"
        img_dir = f"{base_dir}/images"
        os.makedirs(img_dir, exist_ok=True)

        # DOWNLOAD IMAGES
        images = soup.find_all("img")
        for i, img in enumerate(images):
            src = img.get("src")
            if not src:
                continue
            full_url = urljoin(url, src)
            if not any(ext in full_url.lower() for ext in [".jpg", ".jpeg", ".png"]):
                continue
            filename = f"img_{i}.jpg"
            filepath = os.path.join(img_dir, filename)
            download_file(full_url, filepath)
            img["src"] = f"images/{filename}"

        # SAVE HTML
        with open(f"{base_dir}/index.html", "w", encoding="utf-8") as f:
            f.write(str(soup))

        # EXTRACT TEXT
        paragraphs = soup.select("div.detail-text p")
        content = "\n".join([p.get_text(strip=True) for p in paragraphs])

        date = ""
        date_el = soup.select_one("div.text-cnn_grey")
        if date_el:
            date = date_el.get_text(strip=True)

        return {
            "url": url,
            "title": title,
            "date": date,
            "content": content,
            "saved_path": base_dir,
            "scraped_at": datetime.now(UTC).isoformat(),
        }
    except Exception as e:
        print(f"[ERROR] {url} -> {e}")
        return None


# =========================
# SINGLE SCRAPE CYCLE
# =========================
async def run_cycle(browser, scraped_urls):
    all_urls = get_urls()
    new_urls = [u for u in all_urls if u not in scraped_urls]

    if not new_urls:
        print("[INFO] No new articles this cycle.")
        return

    print(f"[INFO] {len(new_urls)} new articles found out of {len(all_urls)} total sitemap URLs.")
    page = await browser.new_page()

    try:
        for url in new_urls:
            if shutdown_event.is_set():
                print("[STOP] Stopping mid-cycle due to shutdown.")
                break

            print("[SCRAPE]", url)
            data = await scrape_article(page, url)
            if data:
                append_result(data)
                scraped_urls.add(url)
                save_scraped_urls(scraped_urls)
            else:
                # mark as seen anyway so we don't keep retrying it every cycle
                scraped_urls.add(url)
                save_scraped_urls(scraped_urls)

            # delay between articles, interruptible by shutdown
            try:
                await asyncio.wait_for(shutdown_event.wait(), timeout=ARTICLE_DELAY)
            except asyncio.TimeoutError:
                pass
    finally:
        await page.close()


# =========================
# MAIN DAEMON LOOP
# =========================
async def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    scraped_urls = load_scraped_urls()
    print(f"[INIT] {len(scraped_urls)} URLs already recorded from previous runs.")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        try:
            while not shutdown_event.is_set():
                print(f"\n[CYCLE] Starting scrape cycle - {datetime.now(UTC).isoformat()}")
                await run_cycle(browser, scraped_urls)

                if shutdown_event.is_set():
                    break

                print(f"[SLEEP] Sleeping {CYCLE_SLEEP}s before next cycle...")
                try:
                    await asyncio.wait_for(shutdown_event.wait(), timeout=CYCLE_SLEEP)
                except asyncio.TimeoutError:
                    pass
        finally:
            print("[CLEANUP] Closing browser...")
            await browser.close()

    print("[DONE] Daemon stopped cleanly.")


if __name__ == "__main__":
    signal.signal(signal.SIGINT, handle_shutdown)
    signal.signal(signal.SIGTERM, handle_shutdown)
    asyncio.run(main())
