# 🖼️ ExamTopics Scraper & PDF Generator

This script automates the process of:

1. Navigating through the [ExamTopics ITILFND v4](https://www.examtopics.com/exams/itil/itilfnd-v4/view/) exam page.
2. Clicking the **Reveal** button on each question.
3. Capturing full-page screenshots.
4. Moving to the **Next** page until all questions are captured.
5. Saving all screenshots to a folder.
6. Converting the screenshots into a single PDF file.

---

## 📦 Dependencies

* Python 3.7+
* [Playwright](https://playwright.dev/python/)
* [Pillow (PIL)](https://pypi.org/project/Pillow/)

### Install Requirements

```bash
pip install playwright pillow
playwright install chromium
```

---

## 🚀 Usage

```bash
python main.py
```

> Optional: Modify `skip_pages` inside `main.py` to start from a later page (e.g., page 3).

---

## 🧠 Features

* Automatically clicks all "Reveal" buttons before screenshotting.
* Navigates through paginated content using the "Next" button.
* Handles potential captchas by pausing and waiting for manual intervention.
* Randomized delay to reduce bot detection.
* Outputs all screenshots in the `examtopics_screenshots` folder.
* Converts images to `output.pdf` using `turn_it_into_pdf.py`.

---

## 🛠️ File Structure

* `main.py` — The core automation script using Playwright.
* `turn_it_into_pdf.py` — Helper module to convert a folder of images into a single PDF.
* `examtopics_screenshots/` — Folder where screenshots are saved (auto-created).

---

## 🔐 Captcha Handling

If a CAPTCHA appears, the script will wait **30 seconds** for manual resolution. You’ll see:

```bash
Captcha detected, please solve it manually.
```

---

## 📝 Notes

* The script uses **Chrome** with `--disable-blink-features=AutomationControlled` to reduce bot detection.
* Make sure you're using it responsibly and ethically, especially considering the source site's terms of service.
