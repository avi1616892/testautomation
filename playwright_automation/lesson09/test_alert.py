import pytest
from playwright.sync_api import Playwright, expect


class TestAlert:

    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(headless=False, channel="chrome",slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://playground.atidcollege.co.il/alert-handling/index.html")
        yield
        page.close()
        context.close()
        browser.close()

    def handle_alert(self, dialog):
        print("Alert text is: " + dialog.message)
        dialog.accept()

    def handle_prompt(self, dialog, text):
        print("Prompt text is: " + dialog.message)
        # A text to enter in prompt. Does not cause any effects if the dialog's type is not prompt.
        dialog.accept(text)

    def handle_confirm_box(self, dialog, status):
        print("Confirm Box text is: " + dialog.message)
        if status == "accept":
            dialog.accept()
        else:
            print("Confirm Box text is: " + dialog.message)
            dialog.dismiss()



    def test_01(self):
        page.once("dialog", lambda dialog: self.handle_alert(dialog))
        page.locator("//button[@onclick='showSimpleAlert()']").click()
        assert page.locator("//p[@class='text-gray-800']").inner_text() == "Simple alert was shown and confirmed."

    def test_02(self):
        page.once("dialog", lambda dialog: self.handle_confirm_box(dialog, "accept"))
        page.locator("//button[@onclick='showConfirmAlert()']").click()
        assert page.locator("//p[@class='text-gray-800']").inner_text() == "You clicked OK! Action will proceed."

    def test_03(self):
        page.once("dialog", lambda dialog: self.handle_prompt(dialog, "Playwright"))
        page.locator("//button[@onclick='showPromptAlert()']").click()
        assert page.locator("//p[@class='text-gray-800']").inner_text() == "Hello, Playwright! Welcome to our website."


        


        
