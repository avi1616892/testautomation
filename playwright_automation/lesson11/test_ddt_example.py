import time
from playwright.sync_api import Playwright
import pytest


keys = "url,expected_title"
data  = [
                ("https://www.google.com","Google"),
                ("https://www.imdb.com","IMDb: Ratings, Reviews, and Where to Watch the Best Movies & TV Shows"),
                ("https://www.bing.com","חיפוש - Microsoft Bing"),
                ("https://www.instagram.com","Instagram")

            ]

class TestReportingEx:

    @pytest.fixture(scope="class",autouse=True)
    def setup(self,playwright:Playwright):
        global browser,context,page 
        browser = playwright.chromium.launch(headless=False,channel="chrome", slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        yield
        time.sleep(3)
        page.close()
        context.close()
        browser.close()

    @pytest.mark.parametrize(keys,data)
    def test_verify_navigation(self,url,expected_title):
        page.goto(url)
        actual_title = page.title()
        print(f"\nThe actual title is: {actual_title}")
        assert actual_title == expected_title
