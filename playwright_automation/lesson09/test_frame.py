import pytest
from playwright.sync_api import Playwright, expect


class TestFrame:

    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(headless=False, channel="chrome",slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://the-internet.herokuapp.com/iframe")
        yield
        page.close()
        context.close()
        browser.close()

    def test_01(self):
        ifrm=page.frame_locator("iframe[id='mce_0_ifr']")    
        assert ifrm.locator("//body[@id='tinymce']//p").inner_text() == "Your content goes here."

    
        


        
