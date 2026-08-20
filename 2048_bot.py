
from playwright.sync_api import sync_playwright
import random
import time
playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
page = browser.new_page()
page.goto("https://play2048.co/",wait_until="domcontentloaded")
arrows = ["ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight"]
try:
    print('Press Ctrl+C to exit')
    while True:
        if page.get_by_text('Play Again').is_visible():
            print(page.get_by_text('points scored').inner_text())
            page.get_by_text('Play Again').click()
            time.sleep(1)
            continue
        page.keyboard.press(random.choice(arrows))
        time.sleep(0.1)
except KeyboardInterrupt:
    print('Exiting...')


    
