import os
import time
from playwright.sync_api import sync_playwright

temp_profile = os.path.join(os.environ.get('TEMP', ''), 'chrome_playwright_profile')
save_dir = r"D:\01_Websites_and_Content\MMY_Website_Project\02_frankbase.com\01_Study_and_Notes_Content\02_School_and_Boards_10th_12th\BSEB_PDF_Repository\Class_10th\01_Math\Shift_1"
os.makedirs(save_dir, exist_ok=True)

test_url = "https://www.selfstudys.com/books/bihar/state-books/class-10th/2024/mathematics-110-set-j-2024/1103023"
dest_pdf = os.path.join(save_dir, "BSEB_10th_2024_Mathematics_110_Set-J_Original.pdf")

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
    
    # Remove 'hideThis' class via JavaScript and click
    print("Unhiding download button and triggering direct click...")
    page.evaluate("""() => {
        const btn = document.querySelector('.downloadPdfBtn');
        if (btn) {
            btn.classList.remove('hideThis');
            btn.style.display = 'inline-block';
            btn.click();
        }
    }""")
    
    try:
        with page.expect_download(timeout=25000) as d_info:
            page.evaluate("document.querySelector('.downloadPdfBtn').click()")
        d = d_info.value
        d.save_as(dest_pdf)
        print(f"🎉 SUCCESS! Mathematics 2024 Downloaded: {dest_pdf}")
        print(f"File Size: {os.path.getsize(dest_pdf)/(1024*1024):.2f} MB")
    except Exception as e:
        print(f"Direct click notice: {e}")
        # Check if modal or prompt appeared
        time.sleep(2)
        page.screenshot(path=r"D:\01_Websites_and_Content\MMY_Website_Project\02_frankbase.com\01_Study_and_Notes_Content\02_School_and_Boards_10th_12th\unhide_click_debug.png")
        
    browser.close()
