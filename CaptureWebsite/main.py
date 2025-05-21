import os
import asyncio
from playwright.sync_api import sync_playwright, Page
from turn_it_into_pdf import images_to_pdf
import random
OUTPUT_FOLDER = 'examtopics_screenshots'
URL = "https://www.examtopics.com/exams/itil/itilfnd-v4/view/"
HEADLESS = False
REVEAL_TEXT = "Reveal"
NEXT_TEXT = "Next"
REVEAL_CLICK_DELAY_MS = 5500 
PAGE_WAIT_DELAY_MS = 5500

def bypass_captcha(page: Page) -> None:
    # This function is a placeholder for any captcha bypass logic.
    # Implement your captcha bypass logic here if needed.
    print("Captcha detected, please solve it manually.")
    page.wait_for_timeout(30000)  # Wait for 30 seconds to allow manual solving
    print("Continuing after captcha resolution.")

def setup_output_folder(path: str) -> None:
    os.makedirs(path, exist_ok=True)

def reveal_all_answers(page: Page) -> None:
    reveals = page.locator(f"text={REVEAL_TEXT}")
    if reveals.count() == 0:
        bypass_captcha(page)
    for i in range(reveals.count()):
        try:
            reveals.nth(i).click()
            page.wait_for_timeout(REVEAL_CLICK_DELAY_MS+random.randint(0, 1000))
        except Exception:
            continue

def save_screenshot(page: Page, page_num: int) -> None:
    file_path = f"{OUTPUT_FOLDER}/page_{page_num}.png"
    page.screenshot(path=file_path, full_page=True)
    print(f"Saved {file_path}")

def click_next_if_available(page: Page) -> bool:
    next_button = page.locator(f"text={NEXT_TEXT}")
    if next_button.is_disabled():
        return False
    next_button.click()
    return True

def capture_exam_pages(skip_pages: int) -> None:
    URL = f"https://www.examtopics.com/exams/itil/itilfnd-v4/view/?page={skip_pages+1}"
    print(f"Capturing pages starting from {URL}")
    setup_output_folder(OUTPUT_FOLDER)

    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=HEADLESS, args=[
            '--disable-blink-features=AutomationControlled',
            '--disable-infobars',
            '--no-sandbox',
            '--disable-dev-shm-usage'
        ])
        context = browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
        page = browser.new_page()
        page.goto(URL)

        page_number = 1

        while True:
            page.wait_for_timeout(PAGE_WAIT_DELAY_MS+random.randint(0, 1000))
            reveal_all_answers(page)
            save_screenshot(page, page_number)

            if not click_next_if_available(page):
                break

            page_number += 1

        browser.close()

if __name__ == "__main__":
    #skip number of pages from args 
    # if len(sys.argv) > 1:
    #     skip_pages = int(sys.argv[1])
    # else:
    skip_pages = 0
    if skip_pages > 0:
        print(f"Skipping {skip_pages} pages.")
    capture_exam_pages(skip_pages)
    path=images_to_pdf(OUTPUT_FOLDER)
    print(f"PDF saved at {path}")
