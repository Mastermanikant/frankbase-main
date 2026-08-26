import urllib.request
import re
import json

headers = {'User-Agent': 'Mozilla/5.0'}

# Probe Class 12 landing page
url_12th = "https://www.selfstudys.com/page/bihar-board-class-12-previous-year-paper"
req = urllib.request.Request(url_12th, headers=headers)
html_12 = urllib.request.urlopen(req, timeout=15).read().decode('utf-8', errors='ignore')

# Find all links to class 12th books
links_12 = re.findall(r'<a[^>]+href=["\'](/books/bihar/state-books/class-12th/[^"\']+)["\'][^>]*>(.*?)</a>', html_12, re.DOTALL)
print(f"Total Class 12th year/subject links found: {len(links_12)}")

clean_12th = []
for h, t in links_12:
    ct = re.sub(r'<[^>]+>', '', t).strip()
    clean_12th.append({"title": ct, "url": "https://www.selfstudys.com" + h})

with open(r"D:\01_Websites_and_Content\MMY_Website_Project\02_frankbase.com\01_Study_and_Notes_Content\02_School_and_Boards_10th_12th\class12_links_catalog.json", "w", encoding="utf-8") as f:
    json.dump(clean_12th, f, ensure_ascii=False, indent=2)

for it in clean_12th[:15]:
    print(f" -> [{it['title']}] : {it['url']}")
