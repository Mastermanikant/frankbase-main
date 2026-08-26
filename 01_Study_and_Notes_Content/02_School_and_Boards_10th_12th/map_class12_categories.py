import urllib.request
import re
import json

headers = {'User-Agent': 'Mozilla/5.0'}

id_map = {}
for cat_id in range(49960, 49995):
    url = f"https://www.selfstudys.com/books/bihar/state-books/class-12th/2024/{cat_id}"
    try:
        req = urllib.request.Request(url, headers=headers)
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
        
        # Extract title of the page or breadcrumb
        title_m = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE)
        page_title = title_m.group(1) if title_m else ""
        
        booklets = re.findall(r'<a[^>]+href=["\'](/books/bihar/state-books/class-12th/[^"\']+)["\'][^>]*>(.*?)</a>', html, re.DOTALL)
        if len(booklets) > 0:
            clean_b = []
            for h, t in booklets:
                ct = re.sub(r'<[^>]+>', '', t).strip()
                clean_b.append({"title": ct, "href": "https://www.selfstudys.com" + h})
            id_map[cat_id] = {"title": page_title, "count": len(clean_b), "booklets": clean_b}
            print(f"ID {cat_id} -> {page_title[:60]} | Booklets: {len(clean_b)}")
    except Exception as e:
        pass

with open(r"D:\01_Websites_and_Content\MMY_Website_Project\02_frankbase.com\01_Study_and_Notes_Content\02_School_and_Boards_10th_12th\class12_verified_categories.json", "w", encoding="utf-8") as f:
    json.dump(id_map, f, ensure_ascii=False, indent=2)
