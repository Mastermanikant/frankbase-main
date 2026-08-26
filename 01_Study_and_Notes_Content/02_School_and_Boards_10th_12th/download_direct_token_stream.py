import os
import time
import re
import html
import urllib.request
from playwright.sync_api import sync_playwright

temp_profile = os.path.join(os.environ.get('TEMP', ''), 'chrome_playwright_profile')
base_repo_dir = r"D:\01_Websites_and_Content\MMY_Website_Project\02_frankbase.com\01_Study_and_Notes_Content\02_School_and_Boards_10th_12th\BSEB_PDF_Repository"

class10_category_endpoints = [
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
    if "math" in t or "गणित" in t or "110" in t or "210" in t:
        return "01_Math"
    elif "science" in t and "social" not in t and ("112" in t or "212" in t or "विज्ञान" in t):
        return "02_Science"
    elif "social" in t or "सामाजिक" in t or "111" in t or "211" in t:
        return "03_Social_Science"
    elif "english" in t or "अंग्रेजी" in t or "113" in t or "213" in t:
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
            headless=True
        )
        page = browser.new_page()

        for yr, cat_url in class10_category_endpoints:
            print(f"\n==================================================")
            print(f">>> [PROCESSING CLASS 10TH - YEAR {yr}] -> {cat_url}")
            print(f"==================================================")

            try:
                html_data = urllib.request.urlopen(urllib.request.Request(cat_url, headers=headers), timeout=10).read().decode('utf-8', errors='ignore')
            except Exception as e:
                print(f"Notice: Year {yr} category unreachable ({e}).")
                continue

            booklet_matches = re.findall(r'<a[^>]+href=["\'](/books/bihar/state-books/class-10th/' + str(yr) + r'/[^"\']+/\d+)["\'][^>]*>(.*?)</a>', html_data, re.DOTALL)
            
            clean_booklets = []
            for href, title_html in booklet_matches:
                t = re.sub(r'<[^>]+>', '', title_html).strip()
                if t:
                    full_url = "https://www.selfstudys.com" + href
                    clean_booklets.append((t, full_url))

            unique_booklets = list({b[1]: b for b in clean_booklets}.values())
            print(f"Found {len(unique_booklets)} genuine subject booklets for {yr}")

            for title, purl in unique_booklets:
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

                print(f"\n[FETCHING DIRECT PDF] {title} ({yr})")
                try:
                    page.goto(purl, timeout=45000)
                    time.sleep(2)

                    # Extract the direct /sitepdfs/<token> source from option_PDFF
                    pdf_source = page.evaluate("""() => {
                        if (window.option_PDFF && window.option_PDFF.source) {
                            return window.option_PDFF.source;
                        }
                        // Search in script tags
                        const scripts = Array.from(document.querySelectorAll('script')).map(s => s.innerText);
                        for (let s of scripts) {
                            let m = s.match(/https:\\/\\/www\\.selfstudys\\.com\\/sitepdfs\\/[a-zA-Z0-9_-]+/);
                            if (m) return m[0];
                        }
                        return null;
                    }""")

                    if pdf_source:
                        print(f" -> Found Direct Source Token: {pdf_source}")
                        # Direct HTTP stream download
                        req = urllib.request.Request(pdf_source, headers=headers)
                        with urllib.request.urlopen(req, timeout=30) as resp, open(win_pdf_path, 'wb') as f:
                            f.write(resp.read())
                        
                        size_mb = os.path.getsize(win_pdf_path) / (1024*1024)
                        print(f" -> 🎉 SUCCESS! Saved 100% Genuine PDF: {safe_name} ({size_mb:.2f} MB)")
                    else:
                        print(f" -> Could not extract option_PDFF.source on {purl}")
                except Exception as de:
                    print(f" -> Download error for {title}: {de}")

        browser.close()
        print("\n==================================================")
        print("ALL CLASS 10TH PAPERS DIRECTLY DOWNLOADED!")
        print("==================================================")
    except Exception as e:
        print(f"Script batch error: {e}")
