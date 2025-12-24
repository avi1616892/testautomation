import allure
from playwright.sync_api import Playwright
import pytest
import time
from playwright_automation.lesson12.confest_ex import base



@pytest.fixture(scope="class",autouse=False)
def init_page(playwright:Playwright):
        browser = playwright.chromium.launch(headless=False,channel="chrome", slow_mo=1000)
        context = browser.new_context()
        base.page = context.new_page()
        base.page.goto("https://atidcollege.co.il/Xamples/bmi/")
        yield
        time.sleep(3)
        base.page.close()
        context.close()
        browser.close()

def pytest_exception_interact(node,call,report):
        if report.failed:
            #screen-shots folder must be created beforehand
            image_path=r"playwright_automation\screen-shots\screen.png"
            base.page.screenshot(path=image_path,full_page=True)
            allure.attach.file(image_path,attachment_type=allure.attachment_type.PNG)

