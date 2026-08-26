import urllib.request
import re
import json

headers = {'User-Agent': 'Mozilla/5.0'}

url_12th = "https://www.selfstudys.com/page/bihar-board-class-12-previous-year-paper"
req = urllib.request.Request(url_12th, headers=headers)
html_12 = urllib.request.urlopen(req, timeout=15).read().decode('utf-8', errors='ignore')

all_links = re.findall(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', html_12, re.DOTALL)
bihar_links = []
for h, t in all_links:
    ct = re.sub(r'<[^>]+>', '', t).strip()
    if any(k in h.lower() or k in ct.lower() for k in ['bihar', '12', 'inter', 'class-12', 'state-books']):
        bihar_links.append({"title": ct, "url": h})

print(f"Total matched links on Class 12th page: {len(bihar_links)}")
for it in bihar_links[:20]:
    print(f" -> [{it['title']}] : {it['url']}")
