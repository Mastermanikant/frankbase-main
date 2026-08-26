import urllib.request
import re
import json

headers = {'User-Agent': 'Mozilla/5.0'}

# Probe years 2023, 2022, 2021, 2020 on class 10th
years = [2023, 2022, 2021, 2020]
discovered_urls = {}

for yr in years:
    landing = f"https://www.selfstudys.com/page/bihar-board-class-10-previous-year-paper"
    req = urllib.request.Request(landing, headers=headers)
    html = urllib.request.urlopen(req, timeout=15).read().decode('utf-8', errors='ignore')
    
    # Find all links on landing that mention the year
    matches = re.findall(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', html, re.DOTALL)
    yr_links = []
    for h, t in matches:
        ct = re.sub(r'<[^>]+>', '', t).strip()
        if str(yr) in ct or str(yr) in h:
            if not h.startswith("http"):
                h = "https://www.selfstudys.com" + h
            yr_links.append({"text": ct, "url": h})
            
    discovered_urls[yr] = yr_links
    print(f"Year {yr} matches found: {len(yr_links)}")
    for item in yr_links[:4]:
        print(f" -> [{item['text']}] : {item['url']}")

with open(r"D:\01_Websites_and_Content\MMY_Website_Project\02_frankbase.com\01_Study_and_Notes_Content\02_School_and_Boards_10th_12th\discovered_older_years.json", "w", encoding="utf-8") as f:
    json.dump(discovered_urls, f, ensure_ascii=False, indent=2)
