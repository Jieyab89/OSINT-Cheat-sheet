import requests
import json
import os
from bs4 import BeautifulSoup

# Arr URLs
urls = {
    "readme": "https://raw.githubusercontent.com/Jieyab89/OSINT-Cheat-sheet/refs/heads/main/README.md",
    "wiki": "https://github.com/Jieyab89/OSINT-Cheat-sheet/wiki",
    "articles": "https://raw.githubusercontent.com/Jieyab89/OSINT-Cheat-sheet/main/awesome-article.md"
}

json_file = os.path.join(os.pardir, "osint_data.json")

if os.path.exists(json_file):
    with open(json_file, "r", encoding="utf-8") as f:
        try:
            existing_data = json.load(f)
        except json.JSONDecodeError:
            existing_data = []
else:
    existing_data = []

existing_categories = {cat["category"]: cat for cat in existing_data}
new_categories = {}
current_category = None

def parse_markdown_md(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"[-] Failed to fetch: {url}")
        return {}

    parsed = {}
    current_cat = None

    for line in response.text.split("\n"):
        line = line.strip()

        if line.startswith("# "):
            current_cat = line[2:].strip()
            parsed[current_cat] = {"category": current_cat, "items": []}

        elif line.startswith("- [") and "](" in line:
            parts = line.split("[", 1)[1].split("](")
            name = parts[0].strip()
            link = parts[1].split(")")[0].strip()
            if current_cat:
                parsed[current_cat]["items"].append({"name": name, "url": link})

    return parsed

def parse_github_wiki(url):
    wiki_items = []
    response = requests.get(url)
    if response.status_code != 200:
        print(f"[-] Failed to fetch: {url}")
        return {}

    soup = BeautifulSoup(response.text, "html.parser")
    for link in soup.select(".wiki-pages-box a"):
        title = link.text.strip()
        page_url = "https://github.com" + link["href"]
        wiki_items.append({"name": title, "url": page_url})

    if wiki_items:
        return {"Jieyab89 Wiki Pages": {"category": "Jieyab89 Wiki Pages", "items": wiki_items}}
    return {}

new_categories.update(parse_markdown_md(urls["readme"]))
new_categories.update(parse_markdown_md(urls["articles"]))
new_categories.update(parse_github_wiki(urls["wiki"]))

for category, new_data in new_categories.items():
    if category in existing_categories:
        existing_items = {item["name"] for item in existing_categories[category]["items"]}
        for new_item in new_data["items"]:
            if new_item["name"] not in existing_items:
                existing_categories[category]["items"].append(new_item)
    else:
        existing_categories[category] = new_data

with open(json_file, "w", encoding="utf-8") as f:
    json.dump(list(existing_categories.values()), f, indent=4, ensure_ascii=False)

print(f"[+] Data updated: {json_file}")
