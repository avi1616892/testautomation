import pytest
from playwright.sync_api import Playwright


class TestJenkinsExample:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(headless=False, channel="chrome")
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.jenkins.io/")
        yield
        page.close()

    def test01_verify_connection(self):
        actual_title = page.title()
        print(f"\nActual Title is: {actual_title}")
