import csv
import time

import pytest
from playwright.sync_api import Playwright

def get_data_from_csv():
    data_list = []
    with open(r"playwright_automation\lesson11\vikipedia_data.csv", newline='') as f:
        reader = csv.reader(f)
        data_list = [tuple(row) for row in reader]
    return data_list

keys = "value", "expect_value"

class Test_Csv_Vikipedia:
    @pytest.fixture(scope="class",autouse=True)
    def setup(self,playwright:Playwright):
        global browser,context,page
        browser=playwright.chromium.launch(headless=False,channel="chrome",slow_mo=300)
        context=browser.new_context()
        page=context.new_page()
        page.set_default_timeout(10 * 1000)
        yield
        time.sleep(5)
        context.close()
        browser.close()

    @pytest.mark.parametrize(keys,get_data_from_csv())
    def test_vikipedia(self,value,expect_value):
        page.goto("https://www.wikipedia.org/")
        page.select_option("#searchLanguage", value="en")
        page.locator("input[id='searchInput']").fill(value)
        page.locator("//button[@type='submit']").click()
        text_value=page.locator("//h1[@id='firstHeading']").inner_text()
        assert expect_value==text_value


