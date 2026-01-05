import json

import pytest
from playwright.sync_api import Playwright
from smart_assertions import soft_assert, verify_expectations

from playwright_automation.lesson13_api_full.chuck_utils import ChuckUtils
from playwright_automation.lesson13_api_full.common_ops import CommonOps


CHUCK_API_BASE_URL="https://api.chucknorris.io/jokes/"
expected_total_categories=16
class Test_ChuckNorrisApiBasic:
    @pytest.fixture(scope="class",autouse=True)
    def setup_playwright_context(self,playwright:Playwright):
        global request_context,chuck_utils
        request_context=playwright.request.new_context(base_url=CHUCK_API_BASE_URL)
        chuck_utils=ChuckUtils(request_context)
        yield
        request_context.dispose()

    def test_get_chuck_norries_categories(self):
        categories=chuck_utils.get_categories()
        chuck_utils.print_categories(categories)
        print(f"Total categories: {len(categories)}")
        assert len(categories)==expected_total_categories

    def test_compare_jokes_count(self):
        obama_total_jokes=chuck_utils.get_total_jokes_count("Barack Obama")
        charlie_total_jokes = chuck_utils.get_total_jokes_count("Charlie Sheen")
        assert charlie_total_jokes>obama_total_jokes

    def test_print_random_jokes(self):
        print("\nRandom Chuck Norris Jokes:")
        jokes_data=[]
        for i in range(10):
            data=chuck_utils.get_jokes_data()
            jokes_data.append([data["url"],data["value"]])
            print(f"Joke[{i+1}] - Joke's URL: {data["url"]} , Joke's Value {data["value"]}")
            soft_assert(data["status"]==200,"Status code is not as expected")
        headers=["URL","Value"]
        CommonOps.generate_csv_from_list(headers,jokes_data,"jokes.csv")
        verify_expectations()
