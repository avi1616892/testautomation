#test_chuck_norries_ui_and_api.py
import json

import pytest
from playwright.sync_api import Playwright

BASE_URL="https://api.chucknorris.io/jokes/"
class TestChuckNorrisUIandAPI:
    @pytest.fixture(scope="class",autouse=True)
    def setup_request(self,playwright:Playwright):
        global request_context,page
        request_context=playwright.request.new_context(base_url=BASE_URL)

        browser=playwright.chromium.launch(headless=False,channel="chrome",slow_mo=2000)
        context=browser.new_context()
        page=context.new_page()

        yield
        request_context.dispose()
        context.close()
        browser.close()

    def test_ui_and_api_joke(self):
        api_endpoint="random"
        api_params=dict(category="movie")
        response=request_context.get(url=api_endpoint,params=api_params)
        joke_data=response.json()
        joke_url=joke_data["url"]
        joke_from_api=joke_data["value"]
        page.goto(joke_url)
        joke_from_web=page.locator("//p[@id='joke_value']").inner_text()
        print(f"\nJoke From WEB: {joke_from_web}")
        print(f"Joke From API: {joke_from_api}")
        assert  joke_from_web==joke_from_api