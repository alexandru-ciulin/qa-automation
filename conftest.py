import pytest

from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

@pytest.fixture
def logged_in_page(page, valid_credentials):
    login_page = LoginPage(page)

    login_page.login(valid_credentials["username"], valid_credentials["password"])

    return page

@pytest.fixture
def valid_credentials():
    return {
        "username":"standard_user",
        "password":"secret_sauce"
    }

@pytest.fixture
def invalid_credentials():
    return {
        "username":"standard_user",
        "password":"secret_saucee"
    }

@pytest.fixture
def products_page(logged_in_page):
    return ProductsPage(logged_in_page)

@pytest.fixture
def cart_page(logged_in_page):
    return CartPage(logged_in_page)

@pytest.fixture
def checkout_page(logged_in_page):
    return CheckoutPage(logged_in_page)