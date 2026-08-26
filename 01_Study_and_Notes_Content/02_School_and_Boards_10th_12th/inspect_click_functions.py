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
    
    # Check click handler on .downloadPdfBtn
    res = page.evaluate("""() => {
        // Inspect jQuery click events or inline functions
        const events = $._data($('.downloadPdfBtn')[0], 'events');
        return {
            events: events ? Object.keys(events) : null,
            downloadBtnClick: $('.downloadPdfBtn').attr('onclick') || 'none',
            allFunctions: Object.keys(window).filter(k => k.toLowerCase().includes('download') || k.toLowerCase().includes('pdf'))
        };
    }""")
    
    print("Event info:", res)
    
    # Check what function gets called when .downloadPdfBtn is clicked
    click_code = page.evaluate("""() => {
        let code = '';
        if (window.sendDownloadEmail) code += 'sendDownloadEmail: ' + window.sendDownloadEmail.toString() + '\\n';
        if (window.downloadPdf) code += 'downloadPdf: ' + window.downloadPdf.toString() + '\\n';
        if (window.downloadBookPdf) code += 'downloadBookPdf: ' + window.downloadBookPdf.toString() + '\\n';
        return code;
    }""")
    print("Click functions:\n", click_code)
    
    browser.close()
