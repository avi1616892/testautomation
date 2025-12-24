import allure
from playwright.sync_api import Page


class AtidHomePage:

    def __init__(self,page:Page):
        self.page = page
        self.header = self.page.locator("//div[@class='home-container']/h2")
        self.name_field = self.page.locator("[id='name']")
        self.last_name = self.page.locator("[id='lastName']")
        self.country_selector = "[id='country']"
        self.submit_button = self.page.locator("[type='submit']")
        self.message = self.page.locator("[id='message-area']")


    @allure.step("Get Header Text:")
    def get_header(self):
        header_text = self.header.inner_text()
        print(f"\nHeader: {header_text}")
        return header_text
    
    @allure.step("Fill form with data:")
    def fill_form(self,name:str,last_name:str,country:str):
        self.name_field.fill(name)
        self.last_name.fill(last_name)
        self.page.select_option(self.country_selector,label=country)
        self.submit_button.click()

    @allure.step("Get Generated message:")
    def get_message(self):
        message_text = self.message.inner_text()
        print(f"\nThe message is:{message_text}")
        return message_text
