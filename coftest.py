import pytest
from playwright.sync_api import sync_playwright
from config.settings import BASE_URL, BROWSER, HEADLESS
from pytest_html import extras
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import base64

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p[BROWSER].launch(headless=HEADLESS)
        context = browser.new_context()
        page = context.new_page()
        page.goto(BASE_URL)
        yield page
        browser.close()


#Function tự động chụp màn hình khi có lỗi
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        page = item.funcargs.get("page")

        if report.failed and page:
            os.makedirs("screenshots", exist_ok=True)
            file_name = f"screenshots/{item.name}.png"
            page.screenshot(path=file_name)
            extra = getattr(report, "extra", [])
            
            with open(file_name, "rb") as image_file:
                encoded = base64.b64encode(image_file.read()).decode("utf-8")
            
            extra.append(extras.image(encoded, mime_type="image/png"))
            report.extra = extra