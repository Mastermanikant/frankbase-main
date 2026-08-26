import os
import time
import json
import re
from playwright.sync_api import sync_playwright

temp_profile = os.path.join(os.environ.get('TEMP', ''), 'chrome_playwright_profile')
download_dir = r"D:\01_Websites_and_Content\MMY_Website_Project\02_frankbase.com\01_Study_and_Notes_Content\02_School_and_Boards_10th_12th"

# HD PDF Viewer URL
hd_viewer_url = "https://www.selfstudys.com/advance-pdf-viewer/bihar/state-books/class-10th/2024/mathematics-110-set-j-2024/1103023"

with sync_playwright() as p:
    browser = p.chromium.launch_persistent_context(
        user_data_dir=temp_profile,
        headless=True,
        accept_downloads=True
    )
    page = browser.new_page()
    
    # Intercept all network requests to catch the exact .pdf URL
    pdf_urls_caught = []
    def handle_request(req):
        if ".pdf" in req.url.lower() or "sitepdfs" in req.url.lower() or "blob:" in req.url.lower() or "pdf" in req.url.lower():
            pdf_urls_caught.append(req.url)
            
    page.on("request", handle_request)
    
    print(f"Navigating to HD PDF Viewer: {hd_viewer_url}...")
    page.goto(hd_viewer_url, timeout=60000)
    time.sleep(5)
    
    # Take screenshot of HD PDF viewer
    page.screenshot(path=os.path.join(download_dir, "hd_viewer_screenshot.png"))
    print("Screenshot of HD Viewer saved.")
    
    # Check iframe or viewer elements
    iframes = page.query_selector_all("iframe")
    print(f"Iframes on page: {len(iframes)}")
    for ifr in iframes:
        src = ifr.get_attribute("src") or ""
        print(f" -> Iframe src: {src}")
        
    # Check all scripts or variables containing PDF url
    content = page.content()
    pdf_matches = re.findall(r'https?://[^\s"\'<>]+\.pdf[^\s"\'<>]*', content, re.IGNORECASE)
    print(f"Direct PDF URLs found in HTML: {len(pdf_matches)}")
    for m in pdf_matches:
        print(f" -> {m}")
        
    print(f"Network requests intercepted: {len(pdf_urls_caught)}")
    for req_url in pdf_urls_caught[:10]:
        print(f" -> Net: {req_url}")
        
    # Check for direct download button inside HD viewer
    d_btns = page.query_selector_all("button, a, .download, #download, [title*='Download']")
    for b in d_btns:
        t = b.inner_text().strip()
        h = b.get_attribute("href") or ""
        tit = b.get_attribute("title") or ""
        print(f"Viewer button: text='{t}', href='{h}', title='{tit}'")
        
    browser.close()
