import time
import allure
from playwright.sync_api import Playwright
import pytest


my_weight = "90"
my_height = "170"
expected_bmi = "31"

class TestReportingEx:

    @pytest.fixture(scope="class",autouse=True)
    def setup(self,playwright:Playwright):
        global browser,context,page 
        browser = playwright.chromium.launch(headless=False,channel="chrome", slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://atidcollege.co.il/Xamples/bmi/")
        yield
        time.sleep(3)
        page.close()
        context.close()
        browser.close()




    @allure.title("Test01 - Verify BMI")
    @allure.description("This test verify bmi after prompting weight and height")
    def test01_verify_bmi(self):
        try:
            self.calculate_bmi(my_weight,my_height)
            self.verify_bmi(expected_bmi+"kuku")# Fail test to get screenshot inside the report
        except Exception as e:
            self.attach_file()
            pytest.fail("Test Failed! see details:",e)
        

    
    #Steps:
    @allure.step(f"Calculate BMI using weight: {my_weight} and  height:{my_height}")
    def calculate_bmi(self,weight:str,height:str):
        page.locator("[id='weight']").fill(weight)
        page.locator("[id='hight']").fill(height)
        page.locator("[id='calculate_data']").click()

    @allure.step(f"Verify the actual bmi is equal to {expected_bmi}")
    def verify_bmi(self,expected:str):
        actual_bmi = page.locator("[id='bmi_result']").input_value()
        print(f"\nThe actual bmi is: {actual_bmi}")
        assert actual_bmi == expected
    
    def attach_file(self):
        #screen-shots folder must be created beforehand
        image_path="playwright_automation\screen-shots\screen.png"
        page.screenshot(path=image_path,full_page=True)
        allure.attach.file(image_path,attachment_type=allure.attachment_type.PNG)



    