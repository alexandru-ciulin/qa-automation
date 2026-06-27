from pages.login_page import LoginPage
from pages.products_page import ProductsPage
import allure

@allure.feature("Authentication")
@allure.story("Login functionality")
@allure.title("Valid user can login successfully")
def test_login_success(page, valid_credentials):
    login_page = LoginPage(page)

    login_page.login(valid_credentials["username"], valid_credentials["password"])

    products_page = ProductsPage(page)

    assert products_page.is_products_title_visible()

@allure.feature("Authentication")
@allure.story("Login functionality")
@allure.title("Login with invalid credentials fails")
def test_login_fail(page, invalid_credentials):
    login_page = LoginPage(page)

    login_page.login(invalid_credentials["username"], invalid_credentials["password"])

    assert login_page.is_error_message_visible()

