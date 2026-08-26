import os
import sys
import time
import re
import html
import urllib.request
from playwright.sync_api import sync_playwright

# Force UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

temp_profile = os.path.join(os.environ.get('TEMP', ''), 'chrome_playwright_profile')
base_repo_dir = r"D:\01_Websites_and_Content\MMY_Website_Project\02_frankbase.com\01_Study_and_Notes_Content\02_School_and_Boards_10th_12th\BSEB_PDF_Repository"

headers = {'User-Agent': 'Mozilla/5.0'}

# Probe categories to find all Bihar Board Class 12 pages
class12_bseb_endpoints = []
for cat_id in range(49950, 49995):
    u = f"https://www.selfstudys.com/books/bihar/state-books/class-12th/2024/{cat_id}"
    try:
        req = urllib.request.Request(u, headers=headers)
        html_data = urllib.request.urlopen(req, timeout=5).read().decode('utf-8', errors='ignore')
        if "bihar" in html_data.lower() and "12th" in html_data.lower():
            # Check if booklets exist
            booklets = re.findall(r'<a[^>]+href=["\'](/books/bihar/state-books/class-12th/[^"\']+)["\'][^>]*>(.*?)</a>', html_data, re.DOTALL)
            if len(booklets) > 0:
                print(f"Found BSEB 12th Category ID {cat_id} with {len(booklets)} booklets.")
                class12_bseb_endpoints.append((cat_id, u))
    except Exception as e:
        pass

def clean_filename(text):
    text = html.unescape(text)
    text = text.replace("&nbsp;", " ")
    text = re.sub(r'[^a-zA-Z0-9_\-]', '_', text)
    text = re.sub(r'_+', '_', text).strip('_')
    return text[:50]

def match_12th_subject(subj_title):
    t = subj_title.lower()
    if "physics" in t or "117" in t or "217" in t or "भौतिकी" in t:
        return "01_Science_Stream/01_Physics"
    elif "chemistry" in t or "118" in t or "218" in t or "रसायन" in t:
        return "01_Science_Stream/02_Chemistry"
    elif "math" in t or "121" in t or "221" in t or "327" in t or "गणित" in t:
        return "01_Science_Stream/03_Mathematics"
    elif "biology" in t or "119" in t or "219" in t or "जीव" in t:
        return "01_Science_Stream/04_Biology"
    elif "hindi" in t or "106" in t or "206" in t or "306" in t:
        return "04_Languages/01_Hindi_100M"
    elif "english" in t or "105" in t or "205" in t or "305" in t:
        return "04_Languages/02_English_100M"
    elif "history" in t or "321" in t or "इतिहास" in t:
        return "02_Arts_Stream/01_History"
    elif "political" in t or "322" in t or "राजनीति" in t:
        return "02_Arts_Stream/02_Political_Science"
    elif "geography" in t or "323" in t or "भूगोल" in t:
        return "02_Arts_Stream/03_Geography"
    elif "economics" in t or "324" in t or "220" in t or "अर्थशास्त्र" in t:
        return "02_Arts_Stream/04_Economics"
    elif "accountancy" in t or "217" in t or "लेखाशास्त्र" in t:
        return "03_Commerce_Stream/01_Accountancy"
    elif "business" in t or "218" in t:
        return "03_Commerce_Stream/02_Business_Studies"
    elif "entrepreneurship" in t or "219" in t:
        return "03_Commerce_Stream/03_Entrepreneurship"
    return "00_General"

def match_shift(subj_title):
    if re.search(r'\b(117|118|121|119|105|106|321|322|1st|shift-1|shift 1)\b', subj_title.lower()):
        return "Shift_1"
    elif re.search(r'\b(217|218|221|219|205|206|323|324|2nd|shift-2|shift 2)\b', subj_title.lower()):
        return "Shift_2"
    return "Shift_1"

with sync_playwright() as p:
    try:
        browser = p.chromium.launch_persistent_context(
            user_data_dir=temp_profile,
            headless=True
        )
        page = browser.new_page()

        for cat_id, cat_url in class12_bseb_endpoints:
            print(f"\n==================================================")
            print(f">>> [PROCESSING CLASS 12TH - ID {cat_id}] -> {cat_url}")
            print(f"==================================================")

            try:
                html_data = urllib.request.urlopen(urllib.request.Request(cat_url, headers=headers), timeout=10).read().decode('utf-8', errors='ignore')
            except Exception as e:
                continue

            booklet_matches = re.findall(r'<a[^>]+href=["\'](/books/bihar/state-books/class-12th/[^"\']+)["\'][^>]*>(.*?)</a>', html_data, re.DOTALL)
            clean_booklets = []
            for href, title_html in booklet_matches:
                t = re.sub(r'<[^>]+>', '', title_html).strip()
                if t and not href.endswith(f"/{cat_id}"):
                    full_url = "https://www.selfstudys.com" + href
                    clean_booklets.append((t, full_url))

            unique_booklets = list({b[1]: b for b in clean_booklets}.values())
            print(f"Found {len(unique_booklets)} Class 12th papers for ID {cat_id}")

            for title, purl in unique_booklets:
                subj_folder = match_12th_subject(title)
                shift_folder = match_shift(title)
                save_dir = os.path.join(base_repo_dir, "Class_12th", subj_folder, shift_folder)
                
                win_save_dir = "\\\\?\\" + os.path.abspath(save_dir)
                os.makedirs(win_save_dir, exist_ok=True)

                safe_name = f"BSEB_12th_2024_{clean_filename(title)}_Original.pdf"
                final_pdf_path = os.path.join(save_dir, safe_name)
                win_pdf_path = "\\\\?\\" + os.path.abspath(final_pdf_path)

                if os.path.exists(win_pdf_path) and os.path.getsize(win_pdf_path) > 300000:
                    print(f" -> Already Exists: {safe_name} ({os.path.getsize(win_pdf_path)/(1024*1024):.2f} MB)")
                    continue

                print(f"\n[FETCHING 12TH DIRECT PDF] {safe_name}")
                try:
                    page.goto(purl, timeout=45000)
                    time.sleep(2)

                    pdf_source = page.evaluate("""() => {
                        if (window.option_PDFF && window.option_PDFF.source) {
                            return window.option_PDFF.source;
                        }
                        const scripts = Array.from(document.querySelectorAll('script')).map(s => s.innerText);
                        for (let s of scripts) {
                            let m = s.match(/https:\\/\\/www\\.selfstudys\\.com\\/sitepdfs\\/[a-zA-Z0-9_-]+/);
                            if (m) return m[0];
                        }
                        return null;
                    }""")

                    if pdf_source:
                        print(f" -> Downloading Token: {pdf_source}")
                        req = urllib.request.Request(pdf_source, headers=headers)
                        with urllib.request.urlopen(req, timeout=30) as resp, open(win_pdf_path, 'wb') as f:
                            f.write(resp.read())
                        
                        size_mb = os.path.getsize(win_pdf_path) / (1024*1024)
                        print(f" -> SUCCESS: Saved 100% Real 12th PDF ({size_mb:.2f} MB)")
                    else:
                        print(f" -> Could not extract source on {purl}")
                except Exception as de:
                    print(f" -> Error downloading: {de}")

        browser.close()
        print("\n==================================================")
        print("ALL CLASS 12TH DIRECT DOWNLOADS COMPLETED!")
        print("==================================================")
    except Exception as e:
        print(f"Script batch error: {e}")
