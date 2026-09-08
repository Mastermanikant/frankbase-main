# -*- coding: utf-8 -*-
import os, re, json
from pathlib import Path

src = Path(r"D:\01_Websites_and_Content\MMY_Website_Project\02_frankbase.com\01_Website_Code\src")
pages = []

for root, dirs, files in os.walk(src):
    for f in files:
        if f.endswith(".njk") and not f.startswith("_") and f != "sitemap.njk":
            fp = Path(root) / f
            rel = fp.relative_to(src)
            content = fp.read_text(encoding="utf-8", errors="ignore")
            
            robots = "noindex, follow (default base.njk)"
            title = "No Title"
            url = "/" + str(rel).replace("\\", "/").replace(".njk", "")
            if url.endswith("/index"):
                url = url[:-5]
            if url == "":
                url = "/"
            
            fm_match = re.search(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
            if fm_match:
                fm = fm_match.group(1)
                r_match = re.search(r"robots:\s*[\"']?(.*?)[\"']?\s*$", fm, re.MULTILINE)
                if r_match:
                    robots = r_match.group(1).strip()
                t_match = re.search(r"title:\s*[\"']?(.*?)[\"']?\s*$", fm, re.MULTILINE)
                if t_match:
                    title = t_match.group(1).strip()
                p_match = re.search(r"permalink:\s*[\"']?(.*?)[\"']?\s*$", fm, re.MULTILINE)
                if p_match:
                    url = p_match.group(1).strip()

            is_indexed = "index" in robots and "noindex" not in robots
            pages.append({
                "file": str(rel).replace("\\", "/"),
                "url": url,
                "title": title,
                "robots": robots,
                "is_indexed": is_indexed
            })

report = {
    "total_pages": len(pages),
    "indexed_pages_count": sum(1 for p in pages if p["is_indexed"]),
    "noindex_pages_count": sum(1 for p in pages if not p["is_indexed"]),
    "pages": sorted(pages, key=lambda x: (not x["is_indexed"], x["url"]))
}

out_file = Path(r"D:\01_Websites_and_Content\MMY_Website_Project\02_frankbase.com\FRANKBASE_PAGES_AND_SEO_AUDIT.json")
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(report, f, ensure_ascii=False, indent=2)

print(f"Total Pages: {report['total_pages']}")
print(f"SEO ON (Indexed): {report['indexed_pages_count']}")
print(f"SEO OFF (Noindex): {report['noindex_pages_count']}")
print("-" * 80)
for p in report["pages"]:
    status = "[INDEXED - ON] " if p["is_indexed"] else "[NOINDEX - OFF]"
    print(f"{status:<16} | {p['url']:<40} | {p['robots']:<25} | {p['file']}")
