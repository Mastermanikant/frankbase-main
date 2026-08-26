import os
import time
from playwright.sync_api import sync_playwright

temp_profile = os.path.join(os.environ.get('TEMP', ''), 'chrome_playwright_profile')

# Test Mathematics 2024 booklet URL
test_url = "https://www.selfstudys.com/books/bihar/state-books/class-10th/2024/mathematics-110-set-j-2024/1103023"

with sync_playwright() as p:
    browser = p.chromium.launch_persistent_context(
        user_data_dir=temp_profile,
        headless=True,
        accept_downloads=True
    )
    page = browser.new_page()
    print(f"Navigating to {test_url}...")
    page.goto(test_url, timeout=60000)
    time.sleep(3)
    
    # Take screenshot of booklet page
    screenshot_p = r"D:\01_Websites_and_Content\MMY_Website_Project\02_frankbase.com\01_Study_and_Notes_Content\02_School_and_Boards_10th_12th\math_booklet_debug.png"
    page.screenshot(path=screenshot_p)
    print("Screenshot saved to math_booklet_debug.png")
    
    # Inspect all clickable download buttons
    btns = page.query_selector_all("button, a")
    print(f"Total elements: {len(btns)}")
    for idx, b in enumerate(btns):
        txt = b.inner_text().strip()
        h = b.get_attribute("href") or ""
        cls = b.get_attribute("class") or ""
        if "download" in txt.lower() or "pdf" in txt.lower() or "download" in h.lower() or "btn" in cls.lower():
            print(f" -> Element {idx}: Text='{txt}', Class='{cls}', href='{h}'")
            
    browser.close()
