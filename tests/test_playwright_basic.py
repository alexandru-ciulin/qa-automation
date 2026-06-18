from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

def test_login_valid(page):
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    assert "inventory" in page.url

def test_login_invalid(page):
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_saucee")

    assert page.get_by_text("Epic sadface: Username and password do not match any user in this service")

def test_products_after_login(page):
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    locator = page.get_by_text("Products")

    assert locator.is_visible()

def test_product_backpack(page):
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    assert page.get_by_text("Sauce Labs Backpack").is_visible()

def test_product_count(page):
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    product_count = page.get_by_role("button", name="Add to cart").count()

    assert product_count == 6
    # Negative check: test should fail if the expected products count is incorrect

def test_select_product(page):
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    page.get_by_text("Sauce Labs Backpack").click()
    assert "inventory-item" in page.url
    assert page.get_by_role("button", name="Add to cart").is_visible()


