import time
import allure
from playwright.sync_api import Playwright
import pytest

from playwright_automation.lesson12.page_object_ex.atid_home_page import AtidHomePage
from playwright_automation.lesson12.page_object_ex.atid_login_page import AtidLoginPage




user_name = "atidUser"
password = "atidPass"
my_name = "Saed"
my_last_name = "Jaber"
my_country = "Israel"


class TestAtidForm:

    @pytest.fixture(scope="class",autouse=True)
    def setup(self,playwright:Playwright):
        global browser,context,page, login_page,home_page
        browser = playwright.chromium.launch(headless=False,channel="chrome", slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.set_default_timeout(10 * 1000)
        page.goto("https://atidcollege.co.il/Xamples/atid-form/")

        #Page Objects - Init
        login_page = AtidLoginPage(page)
        home_page = AtidHomePage(page)


        #Pre Conditions:
        login_page.sign_in(user_name,password)

        yield
        page.close()
        context.close()
        browser.close()

    @allure.title("Test01 - Verify Login")
    @allure.description("This test verify login is successful")
    def test01_verify_login(self):
        assert "Dark Side!" in home_page.get_header()

    @allure.step("Test02 - Verify Form")
    @allure.description("This test verify the generated message after submitting the form")
    def test02_verify_form(self):
        home_page.fill_form(my_name,my_last_name,my_country)
        expected_message = f"Hello, {my_name} {my_last_name}! You are from {my_country}."
        assert home_page.get_message() == expected_message
