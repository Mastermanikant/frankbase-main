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
    
    # Inspect definition of downloadFile, sendEmailToDownloadPDF, pdfflip, etc.
    fns = page.evaluate("""() => {
        return {
            downloadFile: window.downloadFile ? window.downloadFile.toString() : 'none',
            sendEmailToDownloadPDF: window.sendEmailToDownloadPDF ? window.sendEmailToDownloadPDF.toString() : 'none',
            option_PDFF: window.option_PDFF ? JSON.stringify(window.option_PDFF) : 'none'
        };
    }""")
    
    print("downloadFile:\n", fns['downloadFile'])
    print("\nsendEmailToDownloadPDF:\n", fns['sendEmailToDownloadPDF'])
    print("\noption_PDFF:\n", fns['option_PDFF'])
    
    browser.close()
