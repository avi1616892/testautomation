import time
from playwright.sync_api import Playwright
import pytest

first_name="Avi"
last_name="Gavrilov"
dialog_text = ""

class TestExframesPractice:

    @pytest.fixture(scope="class",autouse=True)
    def setup(self,playwright:Playwright):
        global browser,context,page 
        browser = playwright.chromium.launch(headless=False,channel="chrome", slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.set_default_timeout(10000)
        page.goto("https://atidcollege.co.il/Xamples/ex_frames_practice.html")
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

       page.locator("//button[@id='button1']").click()
       text = page.locator("//div[@id='message-box']").inner_text()
       coupon  = text.split("is:")[1].strip()
       print(coupon)
      

       ifrm=page.frame_locator("[id='frame_a']")
       ifrm.locator("//input[@id='first_name']").fill(first_name)
       ifrm.locator("//input[@id='last_name']").fill(last_name)
       ifrm.locator("//input[@id='coupon']").fill(coupon )

       page.once("dialog",lambda dialog:self.handle_alert(dialog))
       ifrm.locator("//button[text()='Show Receipt!']").click()

       expected_result = f"{first_name} {last_name} {coupon}"
       print(expected_result)

       assert expected_result==self.dialog_text


       


       

        


    