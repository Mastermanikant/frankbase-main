import os
import time
from playwright.sync_api import sync_playwright

temp_profile = os.path.join(os.environ.get('TEMP', ''), 'chrome_playwright_profile')

with sync_playwright() as p:
    browser = p.chromium.launch_persistent_context(
        user_data_dir=temp_profile,
        headless=True
    )
    page = browser.new_page()
    url = "https://www.selfstudys.com/books/bihar/state-books/class-10th/2024/mathematics-110-set-j-2024/1103023"
    page.goto(url, timeout=60000)
    time.sleep(3)
    
    # Inspect all scripts and attached event listeners on downloadPdfBtn
    script_info = page.evaluate("""() => {
        const scripts = Array.from(document.querySelectorAll('script')).map(s => s.innerText || s.src);
        const btn = document.querySelector('.downloadPdfBtn');
        return {
            scripts: scripts.filter(s => s.includes('downloadPdfBtn') || s.includes('sitepdfs') || s.includes('sendEmail') || s.includes('pdf')),
            btnOuter: btn ? btn.outerHTML : 'none'
        };
    }""")
    
    print("Button HTML:", script_info['btnOuter'])
    print("\nRelevant Scripts:")
    for s in script_info['scripts']:
        print("--- SCRIPT ---")
        print(s[:1000])
        
    browser.close()
