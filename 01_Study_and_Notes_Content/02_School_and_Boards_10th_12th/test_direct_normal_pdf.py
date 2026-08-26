import os
import time
from playwright.sync_api import sync_playwright

temp_profile = os.path.join(os.environ.get('TEMP', ''), 'chrome_playwright_profile')
download_dir = r"D:\01_Websites_and_Content\MMY_Website_Project\02_frankbase.com\01_Study_and_Notes_Content\02_School_and_Boards_10th_12th"

test_url = "https://www.selfstudys.com/books/bihar/state-books/class-10th/2024/mathematics-110-set-j-2024/1103023"

with sync_playwright() as p:
    browser = p.chromium.launch_persistent_context(
        user_data_dir=temp_profile,
        headless=True,
        accept_downloads=True
    )
    page = browser.new_page()
    page.goto(test_url, timeout=60000)
    time.sleep(3)
    page.evaluate("window.scrollTo(0, 500)")
    time.sleep(2)
    
    # Check all elements with text Normal PDF or HD PDF
    buttons = page.query_selector_all("a, button, .btn")
    print(f"Total buttons found: {len(buttons)}")
    for b in buttons:
        t = b.inner_text().strip()
        h = b.get_attribute("href") or ""
        oc = b.get_attribute("onclick") or ""
        if any(k in t.lower() for k in ["normal", "hd", "download", "pdf"]):
            print(f" -> Text: '{t}' | Href: '{h}' | Onclick: '{oc}'")
            
    # Try clicking the "Normal PDF" button or whatever direct download button exists
    norm_btn = page.query_selector("a:has-text('Normal PDF'), button:has-text('Normal PDF')")
    if norm_btn:
        print("Found Normal PDF button! Clicking...")
        try:
            with page.expect_download(timeout=15000) as d_info:
                norm_btn.click()
            d = d_info.value
            dest = os.path.join(download_dir, "DIRECT_NORMAL_PDF_TEST.pdf")
            d.save_as(dest)
            print(f"🎉 SUCCESS! Normal PDF Downloaded directly: {dest} (Size: {os.path.getsize(dest)} bytes)")
        except Exception as e:
            print(f"Normal PDF click notice: {e}")
            time.sleep(2)
            page.screenshot(path=os.path.join(download_dir, "after_normal_pdf_click.png"))
            
    browser.close()
