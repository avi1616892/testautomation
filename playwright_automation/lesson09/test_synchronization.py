# test_synchronization.py

import time
from playwright.sync_api import Playwright
import pytest


class TestSynchronization:

    @pytest.fixture(scope="class",autouse=True)
    def setup(self,playwright:Playwright):
        global browser,context,page 
        browser = playwright.chromium.launch(headless=False,channel="chrome", slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.set_default_timeout(10 * 1000)
        page.goto("https://atidcollege.co.il/Xamples/ex_synchronization.html")
        yield
        time.sleep(3)
        page.close()
        context.close()
        browser.close()

    def test01_verify_remove(self):
        page.locator("[id='btn']").click()
        actual_message = page.locator("[id='message']").inner_text()
        print(f"\nActual Message is: {actual_message}")
        expected_message = "It's gone!"
        assert actual_message == expected_message

    def test02_verify_hidden(self):
        page.locator("[id='hidden']").click()
        page.locator("[id='loading1']").wait_for(state="hidden",timeout=5*1000)
        assert page.locator("[id='loading1']").is_hidden()

    def test03_verify_rendered(self):
        page.locator("[id='rendered']").click()
        actual_output = page.locator("//div[@id='finish2']/h4").inner_text()
        print(f"Actual Output:{actual_output}")
        expected_output = "My Rendered Element After Fact!"
        assert actual_output == expected_output
        
        
        
