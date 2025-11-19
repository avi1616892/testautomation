import pytest
from playwright.sync_api import Playwright, expect

verifyTrueConnection = "Welcome to the Dark Side!"

class TestLocatorsBasicExample:

    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(headless=False, channel="chrome")
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://atidcollege.co.il/Xamples/atid-form/")
        yield
        page.close()
        context.close()
        browser.close()

    def test01_verify_connection(self):
        expect(page.locator("//h2[text()='Login']")).to_be_visible()

        page.locator("#username").fill("atidUser")
        page.locator("#password").fill("atidPass")
        page.locator("//button[@type='submit']").click()

        expect(page.locator("text=Welcome to the Dark Side!")).to_be_visible()

        assert page.locator("text=Welcome to the Dark Side!").inner_text() == verifyTrueConnection
