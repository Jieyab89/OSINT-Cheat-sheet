import requests
import json
import os

url = "https://raw.githubusercontent.com/Jieyab89/OSINT-Cheat-sheet/refs/heads/main/README.md"
# URL (add another soon)

response = requests.get(url)
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

print(f"Data updated: {json_file}")
