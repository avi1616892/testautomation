import pytest
from playwright.sync_api import Playwright, expect


class TestControllers:

    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(headless=False, channel="chrome",slow_mo=300)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://playground.atidcollege.co.il/checkout-flow/index.html")
        yield
        page.close()
        context.close()
        browser.close()

    def test_print_thinks(self):
        things = page.locator("//h3[@class='font-medium text-lg mb-2']")
        count = things.count()

        for i in range(count):
            text = things.nth(i).inner_text()
            print(text)

    def test_verification(self):
        page.locator("//button[@data-product-id='3']").click()
        page.locator("(//button[@class='next-step bg-indigo-600 text-white py-2 px-6 rounded-md hover:bg-indigo-700 transition-colors'])[1]").click()
        page.locator("(//button[@class='next-step bg-indigo-600 text-white py-2 px-6 rounded-md hover:bg-indigo-700 transition-colors'])[2]").click()

        page.locator("//input[@id='firstName']").fill("Avi")
        page.locator("//input[@id='lastName']").fill("Gavrilov")
        page.locator("//input[@id='email']").fill("Avi1234@gmail.com")
        page.locator("//input[@id='phone']").fill("035987864")
        page.locator("//input[@id='address']").fill("address")
        page.locator("//input[@id='city']").fill("Tel-Aviv")
        page.locator("//input[@id='zip']").fill("123456")

        page.locator("(//button[@class='next-step bg-indigo-600 text-white py-2 px-6 rounded-md hover:bg-indigo-700 transition-colors'])[3]").click()

        assert page.locator("(//h2[@class='text-2xl font-bold text-gray-800 mb-6'])[4]").inner_text() == "Payment Method"

