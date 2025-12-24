from playwright_automation.lesson12.confest_ex import base
import allure
from playwright.sync_api import Playwright
import pytest



@pytest.mark.usefixtures("init_page")
class TestConftestExample:
    
    @allure.title("Test01 - Verify BMI")
    @allure.description("This test verify bmi after prompting weight and height")
    def test01_verify_bmi(self):
        self.calculate_bmi(base.my_weight,base.my_height)
        self.verify_bmi(base.expected_bmi+"kuku")# Fail test to get screenshot inside the report
       
        
    #Steps:
    @allure.step(f"Calculate BMI using weight: {base.my_weight} and  height:{base.my_height}")
    def calculate_bmi(self,weight:str,height:str):
        base.page.locator("[id='weight']").fill(weight)
        base.page.locator("[id='hight']").fill(height)
        base.page.locator("[id='calculate_data']").click()

    @allure.step(f"Verify the actual bmi is equal to {base.expected_bmi}")
    def verify_bmi(self,expected:str):
        actual_bmi = base.page.locator("[id='bmi_result']").input_value()
        print(f"\nThe actual bmi is: {actual_bmi}")
        assert actual_bmi == expected
    
  

    