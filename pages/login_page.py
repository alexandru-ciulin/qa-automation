from pages.base_page import BasePage
import allure

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def open(self):
        self.page.goto("https://www.saucedemo.com")


    def login(self, username, password):
        with allure.step("Open login page"):
            self.open()

        with allure.step("Enter username"):
            self.page.get_by_placeholder("Username").fill(username)

        with allure.step("Enter password"):
            self.page.get_by_placeholder("Password").fill(password)

        with allure.step("Click login button"):
            self.page.get_by_role("button", name="Login").click()

    def is_error_message_visible(self):
        with allure.step("Verify login error message is displayed"):
            return self.page.get_by_text("Epic sadface: Username and password do not match any user in this service").is_visible()