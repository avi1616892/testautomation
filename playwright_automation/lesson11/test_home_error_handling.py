#test_home_error_handling

import time

import pytest
from playwright.sync_api import Playwright,expect


class Test_Home_Errors:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(headless=False, channel="chrome", slow_mo=300)
        context = browser.new_context()
        page = context.new_page()
        page.set_default_timeout(10*1000)
        page.goto("https://atidcollege.co.il/Xamples/ex_synchronization.html")
        yield
        time.sleep(5)
        context.close()
        browser.close()

    def test_error_01(self):
        try:
            page.locator("button[id='btn']").click()
            time.sleep(5)
            page.locator("input[id='checkbox']").click()
            print("Test fail you hava visibilty of chekbox")
        except Exception as e:
            print(f"Playwright could not find the element but nevertheless test did not fail{e}")
   
   
    def test_2_no_try_catch(self):
        page.reload()
        page.locator("[id='btn']").click()
        time.sleep(5)
        if (page.locator("[id='checkbox']")).count() > 0:
            print("Element exists on screen")
        else:
            print("Element does NOT exist on screen")


