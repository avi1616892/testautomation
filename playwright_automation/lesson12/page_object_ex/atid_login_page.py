import allure
from playwright.sync_api import Page

class AtidLoginPage:

    def __init__(self,page:Page):
        self.page = page
        self.user_name_field = self.page.locator("[id='username']")
        self.password_field = self.page.locator("[id='password']")
        self.submit_button = self.page.locator("[type='submit']")

    @allure.step("Sign in using provided username and password")
    def sign_in(self,user_name:str,password:str):
        self.user_name_field.fill(user_name)
        self.password_field.fill(password)
        self.submit_button.click()