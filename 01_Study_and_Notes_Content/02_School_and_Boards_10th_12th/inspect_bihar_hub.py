import urllib.request
import re
import json

headers = {'User-Agent': 'Mozilla/5.0'}

url = "https://www.selfstudys.com/state-wise/bihar"
req = urllib.request.Request(url, headers=headers)
html = urllib.request.urlopen(req, timeout=15).read().decode('utf-8', errors='ignore')

all_links = re.findall(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', html, re.DOTALL)
clean = []
for h, t in all_links:
    ct = re.sub(r'<[^>]+>', '', t).strip()
    if any(k in h.lower() or k in ct.lower() for k in ['12', '10', 'previous', 'paper', 'model', 'question']):
        clean.append({"title": ct, "url": h})

print(f"Total matched links on Bihar hub: {len(clean)}")
for it in clean[:25]:
    print(f" -> [{it['title']}] : {it['url']}")
