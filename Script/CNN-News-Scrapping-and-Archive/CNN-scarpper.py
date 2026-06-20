import asyncio
import json
import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from playwright.async_api import async_playwright

SITEMAP_URL = "https://www.cnnindonesia.com/nasional/sitemap_web.xml"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240"
}


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
    except:
        pass


# =========================
# GET SITEMAP
# =========================
def get_urls():
    res = requests.get(SITEMAP_URL, headers=HEADERS)
    soup = BeautifulSoup(res.text, "xml")
    urls = [loc.text for loc in soup.find_all("loc")]
    return urls[:5]


# =========================
# SCRAPE + ARCHIVE
# =========================
async def scrape_article(page, url):
    try:
        await page.goto(url, timeout=60000)
        await page.wait_for_selector("h1")

        html = await page.content()
        soup = BeautifulSoup(html, "html.parser")

        title = soup.select_one("h1").get_text(strip=True)
        slug = safe_filename(title)

        base_dir = f"output/{slug}"
        img_dir = f"{base_dir}/images"

        os.makedirs(img_dir, exist_ok=True)

        # =========================
        # DOWNLOAD IMAGES
        # =========================
        images = soup.find_all("img")

        for i, img in enumerate(images):
            src = img.get("src")

            if not src:
                continue

            full_url = urljoin(url, src)

            # filter hanya gambar
            if not any(ext in full_url.lower() for ext in [".jpg", ".jpeg", ".png"]):
                continue

            filename = f"img_{i}.jpg"
            filepath = os.path.join(img_dir, filename)

            download_file(full_url, filepath)

            # rewrite path di HTML
            img["src"] = f"images/{filename}"

        # =========================
        # SAVE HTML
        # =========================
        with open(f"{base_dir}/index.html", "w", encoding="utf-8") as f:
            f.write(str(soup))

        # =========================
        # EXTRACT TEXT
        # =========================
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
            "saved_path": base_dir
        }

    except Exception as e:
        print(f"Error: {url} -> {e}")
        return None


# =========================
# MAIN
# =========================
async def main():
    urls = get_urls()
    results = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        for url in urls:
            print("[SCRAPE]", url)

            data = await scrape_article(page, url)

            if data:
                results.append(data)

            await asyncio.sleep(2)

        await browser.close()

    with open("cnn_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

    print("[DONE] Archive + JSON selesai")


if __name__ == "__main__":
    asyncio.run(main())
