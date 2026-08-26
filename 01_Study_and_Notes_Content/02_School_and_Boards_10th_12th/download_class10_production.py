import os
import time
import re
import html
import urllib.request
from playwright.sync_api import sync_playwright

temp_profile = os.path.join(os.environ.get('TEMP', ''), 'chrome_playwright_profile')
base_repo_dir = r"D:\01_Websites_and_Content\MMY_Website_Project\02_frankbase.com\01_Study_and_Notes_Content\02_School_and_Boards_10th_12th\BSEB_PDF_Repository"

# Exact year URLs on SelfStudys
class10_year_endpoints = [
    (2024, "https://www.selfstudys.com/books/bihar/state-books/class-10th/2024/49958"),
    (2023, "https://www.selfstudys.com/books/bihar/state-books/class-10th/2023/49957"),
    (2022, "https://www.selfstudys.com/books/bihar/state-books/class-10th/2022/49956"),
    (2021, "https://www.selfstudys.com/books/bihar/state-books/class-10th/2021/49955"),
    (2020, "https://www.selfstudys.com/books/bihar/state-books/class-10th/2020/49954")
]

def clean_filename(text):
    text = html.unescape(text)
    text = text.replace("&nbsp;", " ")
    text = re.sub(r'[\\/*?:"<>|]', "", text)
    text = re.sub(r'\s+', '_', text).strip('_')
    return text[:60]

def match_subject_folder(subj_title):
    t = subj_title.lower()
    if "math" in t or "गणित" in t or "110" in t or "210" in t or "121" in t:
        return "01_Math"
    elif "science" in t and "social" not in t and ("112" in t or "212" in t or "विज्ञान" in t or "science" in t):
        return "02_Science"
    elif "social" in t or "सामाजिक" in t or "111" in t or "211" in t:
        return "03_Social_Science"
    elif "english" in t or "अंग्रेजी" in t or "113" in t or "213" in t or "105" in t or "305" in t:
        return "04_English"
    elif "hindi" in t or "हिंदी" in t or "101" in t or "201" in t:
        return "05_Hindi"
    elif "sanskrit" in t or "संस्कृत" in t or "105" in t or "205" in t:
        return "06_Sanskrit"
    return "00_General"

def match_shift(subj_title):
    if re.search(r'\b(110|111|112|113|101|105|1st|shift-1|shift 1)\b', subj_title.lower()):
        return "Shift_1"
    elif re.search(r'\b(210|211|212|213|201|205|2nd|shift-2|shift 2)\b', subj_title.lower()):
        return "Shift_2"
    return "Shift_1"

headers = {'User-Agent': 'Mozilla/5.0'}

with sync_playwright() as p:
    try:
        browser = p.chromium.launch_persistent_context(
            user_data_dir=temp_profile,
            headless=True,
            accept_downloads=True
        )
        page = browser.new_page()

        for yr, yr_url in class10_year_endpoints:
            print(f"\n==================================================")
            print(f">>> [PROCESSING CLASS 10TH - YEAR {yr}] -> {yr_url}")
            print(f"==================================================")

            try:
                html_content = urllib.request.urlopen(urllib.request.Request(yr_url, headers=headers), timeout=10).read().decode('utf-8', errors='ignore')
            except Exception as ue:
                print(f"Notice: Year {yr} endpoint unreachable ({ue}).")
                continue

            rows = re.findall(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', html_content, re.DOTALL)
            clean_papers = []
            for h, t in rows:
                ct = re.sub(r'<[^>]+>', '', t).strip()
                if any(s in ct.lower() for s in ['math', 'science', 'english', 'hindi', 'sanskrit', 'social']):
                    if not h.startswith("http"):
                        h = "https://www.selfstudys.com" + h
                    clean_papers.append((ct, h))

            unique_papers = list({p[1]: p for p in clean_papers}.values())
            print(f"Found {len(unique_papers)} genuine papers queued for Year {yr}")

            for title, purl in unique_papers:
                subj_folder = match_subject_folder(title)
                shift_folder = match_shift(title)
                save_dir = os.path.join(base_repo_dir, "Class_10th", subj_folder, shift_folder)
                
                win_save_dir = "\\\\?\\" + os.path.abspath(save_dir)
                os.makedirs(win_save_dir, exist_ok=True)

                safe_name = f"BSEB_10th_{yr}_{clean_filename(title)}_Original.pdf"
                final_pdf_path = os.path.join(save_dir, safe_name)
                win_pdf_path = "\\\\?\\" + os.path.abspath(final_pdf_path)

                if os.path.exists(win_pdf_path) and os.path.getsize(win_pdf_path) > 300000:
                    print(f" -> Already Exists: {safe_name} ({os.path.getsize(win_pdf_path)/(1024*1024):.2f} MB)")
                    continue

                print(f"\n[DOWNLOADING] {title} ({yr})")
                try:
                    page.goto(purl, timeout=45000)
                    time.sleep(2)

                    # Look for the download button using multiple selectors
                    d_btn = page.query_selector("a:has-text('DOWNLOAD PDF'), button:has-text('DOWNLOAD PDF'), .btn-danger:has-text('DOWNLOAD PDF'), a.btn-download")
                    
                    if not d_btn:
                        # Scroll down slightly to make button visible
                        page.evaluate("window.scrollTo(0, 400)")
                        time.sleep(1)
                        d_btn = page.query_selector("a:has-text('DOWNLOAD PDF'), button:has-text('DOWNLOAD PDF'), .btn-danger:has-text('DOWNLOAD PDF')")

                    if d_btn:
                        # Use dispatch_event or click
                        with page.expect_download(timeout=25000) as d_info:
                            d_btn.dispatch_event('click')
                        d = d_info.value
                        d.save_as(win_pdf_path)
                        size_mb = os.path.getsize(win_pdf_path) / (1024*1024)
                        print(f" -> 🎉 SUCCESS! Saved: {safe_name} ({size_mb:.2f} MB)")
                    else:
                        print(f" -> Download button not found on {purl}")
                except Exception as de:
                    print(f" -> Error downloading {title}: {de}")

        browser.close()
        print("\n==================================================")
        print("CLASS 10TH REVERSE DOWNLOAD COMPLETED SUCCESSFULLY!")
        print("==================================================")
    except Exception as e:
        print(f"Browser batch error: {e}")
