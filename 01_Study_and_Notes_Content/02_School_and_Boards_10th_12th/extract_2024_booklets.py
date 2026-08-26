import urllib.request
import re
import json

headers = {'User-Agent': 'Mozilla/5.0'}

# 2024 Category ID 49958
url_2024 = "https://www.selfstudys.com/books/bihar/state-books/class-10th/2024/49958"
html = urllib.request.urlopen(urllib.request.Request(url_2024, headers=headers)).read().decode('utf-8', errors='ignore')

# Extract all links that lead to subject booklets (e.g. /science-112-set-i-2024/1103021)
booklet_links = re.findall(r'<a[^>]+href=["\'](/books/bihar/state-books/class-10th/2024/[^"\']+)["\'][^>]*>(.*?)</a>', html, re.DOTALL)

print(f"Total 2024 subject booklet links found: {len(booklet_links)}")
clean_2024 = []
for h, t in booklet_links:
    ct = re.sub(r'<[^>]+>', '', t).strip()
    if ct:
        clean_2024.append({"title": ct, "url": "https://www.selfstudys.com" + h})

with open(r"D:\01_Websites_and_Content\MMY_Website_Project\02_frankbase.com\01_Study_and_Notes_Content\02_School_and_Boards_10th_12th\bseb_2024_exact_booklet_links.json", "w", encoding="utf-8") as f:
    json.dump(clean_2024, f, ensure_ascii=False, indent=2)

for item in clean_2024[:15]:
    print(f" -> [{item['title']}] : {item['url']}")
