import os
import time
from playwright.sync_api import sync_playwright

temp_profile = os.path.join(os.environ.get('TEMP', ''), 'chrome_playwright_profile')

# Science 2024 (which downloaded directly before) vs Math 2024
sci_url = "https://www.selfstudys.com/books/bihar/state-books/class-10th/2024/science-112-set-i-2024/1103021"
math_url = "https://www.selfstudys.com/books/bihar/state-books/class-10th/2024/mathematics-110-set-j-2024/1103023"

with sync_playwright() as p:
    browser = p.chromium.launch_persistent_context(
        user_data_dir=temp_profile,
        headless=True,
        accept_downloads=True
    )
    page = browser.new_page()
    
    print("1. Inspecting Science 2024 page...")
    page.goto(sci_url, timeout=60000)
    time.sleep(3)
    sci_btns = page.evaluate("""() => {
        return Array.from(document.querySelectorAll('a, button')).map(el => ({
            text: el.innerText.trim(),
            href: el.getAttribute('href'),
            onclick: el.getAttribute('onclick'),
            className: el.className
        })).filter(x => x.text.includes('PDF') || (x.href && x.href.includes('pdf')));
    }""")
    print("Science Buttons:", sci_btns)
    
    print("\n2. Inspecting Math 2024 page...")
    page.goto(math_url, timeout=60000)
    time.sleep(3)
    math_btns = page.evaluate("""() => {
        return Array.from(document.querySelectorAll('a, button')).map(el => ({
            text: el.innerText.trim(),
            href: el.getAttribute('href'),
            onclick: el.getAttribute('onclick'),
            className: el.className
        })).filter(x => x.text.includes('PDF') || (x.href && x.href.includes('pdf')));
    }""")
    print("Math Buttons:", math_btns)
    
    browser.close()
