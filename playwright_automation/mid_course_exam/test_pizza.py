import time
from playwright.sync_api import Playwright
import pytest

expected_starting_price="$7.50"
first_name="Avi"
last_name="Gavrilov"
expected_price_with_delivery="$10.50"
dialog_text= ""

class TestExframesPractice:

    @pytest.fixture(scope="class",autouse=True)
    def setup(self,playwright:Playwright):
        global browser,context,page 
        browser = playwright.chromium.launch(headless=False,channel="chrome", slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.set_default_timeout(10000)
        page.goto("https://atidcollege.co.il/Xamples/pizza/")
        yield
        time.sleep(3)
        page.close()
        context.close()
        browser.close()

    def handle_alert(self,dialog):
        self.dialog_text = dialog.message
        print("Alert Text is: ", self.dialog_text)
        dialog.accept()

    def test_01(self):
        starting_price=page.locator("//span[@class='ginput_total ginput_total_5']").inner_text()
        assert starting_price==expected_starting_price

    def test_02(self):
         page.locator("//input[@name='input_22.3']").fill(first_name)
         page.locator("//input[@name='input_22.6']").fill(last_name)
         page.select_option("[name='input_21']", value="Delivery|3")
         price_with_delivery=page.locator("//span[@class='ginput_total ginput_total_5']").inner_text()
         assert price_with_delivery==expected_price_with_delivery

    def test_03(self):
        ifrm=page.frame_locator("//iframe[@src='coupon.html']")
        discount_coupon=ifrm.locator("//div[@id='coupon_Number']").inner_text().strip()
        print(discount_coupon)
        page.locator("//textarea[@name='input_20']").fill(discount_coupon)

        page.once("dialog",lambda dialog:self.handle_alert(dialog))
        page.locator("//input[@value='Submit Your Order']").click()

        expected_result = f"{first_name} {last_name} {discount_coupon}"
        print(expected_result)
        assert expected_result==self.dialog_text
