import urllib.request
import re
import json

headers = {'User-Agent': 'Mozilla/5.0'}

test_12_urls = [
    # Class 12th PYQ landing
    "https://www.selfstudys.com/books/bihar/state-books/class-12th",
    "https://www.selfstudys.com/books/bihar/state-books/class-12th/2024",
    "https://www.selfstudys.com/books/bihar/state-books/class-12th/2023",
    "https://www.selfstudys.com/books/bihar/state-books/class-12th/2024/49968",
    "https://www.selfstudys.com/books/bihar/state-books/class-12th/2024/49969",
    "https://www.selfstudys.com/books/bihar/state-books/class-12th/2024/49970",
    "https://www.selfstudys.com/books/bihar/state-books/class-12th/2024/49971",
    "https://www.selfstudys.com/books/bihar/state-books/class-12th/2024/49972"
]

res = {}
for u in test_12_urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
        # Check if papers exist
        booklets = re.findall(r'<a[^>]+href=["\'](/books/bihar/state-books/class-12th/[^"\']+)["\'][^>]*>(.*?)</a>', html, re.DOTALL)
        res[u] = {"status": "SUCCESS", "booklets_count": len(booklets)}
        print(f"OK: {u} -> Booklets: {len(booklets)}")
    except Exception as e:
        res[u] = {"status": "FAILED", "error": str(e)}
        print(f"FAIL: {u} -> {e}")
