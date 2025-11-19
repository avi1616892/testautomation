import pytest
from playwright.sync_api import Playwright, expect


class TestAdavenceLocatorsExample:

    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(headless=False, channel="chrome",slow_mo=300)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://atidcollege.co.il/Xamples/practice-form.html")
        yield
        page.close()
        context.close()
        browser.close()

    def test_verify_connection(self):
        expect(page.locator("//h2[text()='Plan Your Dream Vacation']")).to_be_visible()
        page.locator("//input[@id='not-random']").fill("Avi")
        page.locator("(//input[@type='text'])[2]").fill("Gavrilov")
        page.select_option("//select[@id='destinationType']", value="beach")
        page.check("//input[@name='travelBuddy']")
        page.check("//input[@value='discounts']")
        page.locator("//button[@type='submit']").click()
        expect(page.locator("//h3[text()='Enjoy your vacation, Avi Gavrilov!']")).to_be_visible()
        page.locator("//button[@id='reset-btn']").click()

