import requests
import json
import os

# Arr URL'S
urls = [
    "https://raw.githubusercontent.com/Jieyab89/OSINT-Cheat-sheet/refs/heads/main/README.md",
    "https://github.com/Jieyab89/OSINT-Cheat-sheet/wiki"
]

response = requests.get(urls[0])
data = response.text

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

for line in data.split("\n"):
    line = line.strip()

    if line.startswith("# "):  
        current_category = line[2:].strip()
        if current_category not in new_categories:
            new_categories[current_category] = {"category": current_category, "items": []}

    elif line.startswith("- [") and "](" in line:  
        parts = line.split("[", 1)[1].split("](")
        name = parts[0].strip()
        link = parts[1].split(")")[0].strip()

        if current_category:
            new_categories[current_category]["items"].append({"name": name, "url": link})

wiki_category = "Jieyab89 Wiki Pages"
wiki_items = []

wiki_response = requests.get(urls[1])
if wiki_response.status_code == 200:
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(wiki_response.text, "html.parser")
    
    for link in soup.select(".wiki-pages-box a"):  
        title = link.text.strip()
        page_url = "https://github.com" + link["href"]
        wiki_items.append({"name": title, "url": page_url})

if wiki_items:
    new_categories[wiki_category] = {"category": wiki_category, "items": wiki_items}

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
