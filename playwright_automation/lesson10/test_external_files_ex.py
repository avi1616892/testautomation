import time
from playwright.sync_api import Playwright,expect
import pytest
import xml.etree.ElementTree as ET


def get_data_from_xml(node_name):
    root = ET.parse(r"playwright_automation\lesson10\bmi_data.xml").getroot()
    return root.find(".//" + node_name).text          

my_weight = get_data_from_xml("MY_WEIGHT")
my_height = get_data_from_xml("MY_HEIGHT")
expected_bmi = get_data_from_xml("EXPECTED_BMI")

class TestExternalFilesEx:

    @pytest.fixture(scope="class",autouse=True)
    def setup(self,playwright:Playwright):
        global browser,context,page 
        browser = playwright.chromium.launch(headless=False,channel="chrome", slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.goto(get_data_from_xml("URL"))
        yield
        time.sleep(3)
        page.close()
        context.close()
        browser.close()
    
    def test01_verify_bmi(self):
        page.locator("[id='weight']").fill(my_weight)
        page.locator("[id='hight']").fill(my_height)
        page.locator("[id='calculate_data']").click()
        actual_bmi = page.locator("[id='bmi_result']").input_value()
        print(f"\nActual Bmi: {actual_bmi}")
        assert actual_bmi == expected_bmi #Option 1 - Using assert
        #expect(page.locator("[id='bmi_result']")).to_have_value(expected_bmi) # option 2 using expect