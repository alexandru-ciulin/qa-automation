import pytest

from pages.products_page import ProductsPage

def test_products_after_login(logged_in_page):
    products_page = ProductsPage(logged_in_page)

    assert products_page.is_products_title_visible

def test_product_backpack(logged_in_page):
    products_page = ProductsPage(logged_in_page)
    
    assert products_page.is_product_visible("Sauce Labs Backpack")

def test_product_count(logged_in_page):
    products_page = ProductsPage(logged_in_page)

    assert products_page.get_products_count() == 6

def test_select_product(logged_in_page):
    products_page = ProductsPage(logged_in_page)
    
    products_page.select_product("Sauce Labs Backpack")

    assert "inventory-item" in logged_in_page.url

def test_add_product_to_cart(products_page):
    products_page.add_product_to_cart("Sauce Labs Backpack")
    assert products_page.get_cart_badge_count() == '1'

def test_product_in_cart(products_page):
    products_page.add_product_to_cart("Sauce Labs Backpack")
    
    cart_page = products_page.open_cart()

    assert cart_page.is_product_in_cart("Sauce Labs Backpack")

def test_remove_product_from_cart(products_page):
    products_page.add_product_to_cart("Sauce Labs Backpack")

    cart_page = products_page.open_cart()
    
    cart_page.remove_product("Sauce Labs Backpack")

    assert not cart_page.is_product_in_cart("Sauce Labs Backpack")

def test_checkout_information(products_page):
    products_page.add_product_to_cart("Sauce Labs Backpack")

    cart_page = products_page.open_cart()

    checkout_page = cart_page.open_checkout()

    checkout_page.fill_customer_information("Alexandru", "Ciulin", "700715")

    assert checkout_page.is_overview_page_visible()

    assert "checkout-step-two" in checkout_page.page.url

def test_checkout_without_first_name(products_page):
    products_page.add_product_to_cart("Sauce Labs Backpack")

    cart_page = products_page.open_cart()

    checkout_page = cart_page.open_checkout()

    checkout_page.fill_customer_information("", "Ciulin", "700715")

    assert checkout_page.is_overview_page_visible()

    assert "checkout-step-two" in checkout_page.page.url
    
def test_complete_order(products_page):
    products_page.add_product_to_cart("Sauce Labs Backpack")

    cart_page = products_page.open_cart()

    checkout_page = cart_page.open_checkout()

    checkout_page.fill_customer_information("Alexandru", "Ciulin", "700715")

    checkout_page.finish_order()

    assert checkout_page.is_order_completed()

def test_checkout_without_first_name(products_page):
    products_page.add_product_to_cart("Sauce Labs Backpack")

    cart_page = products_page.open_cart()

    checkout_page = cart_page.open_checkout()

    checkout_page.fill_customer_information("", "Ciulin", "700715")

    assert (checkout_page.get_error_message() == "Error: First Name is required")

def test_checkout_without_last_name(products_page):
    products_page.add_product_to_cart("Sauce Labs Backpack")

    cart_page = products_page.open_cart()

    checkout_page = cart_page.open_checkout()

    checkout_page.fill_customer_information("Alexandru", "", "700715")

    assert (checkout_page.get_error_message() == "Error: Last Name is required")

def test_checkout_without_postal_code(products_page):
    products_page.add_product_to_cart("Sauce Labs Backpack")

    cart_page = products_page.open_cart()

    checkout_page = cart_page.open_checkout()

    checkout_page.fill_customer_information("Alexandru", "Ciulin", "")

    assert (checkout_page.get_error_message() == "Error: Postal Code is required")

@pytest.mark.parametrize(
    "first_name, last_name, postal_code, expected_error",
    [
        ("", "Ciulin", "700715", "Error: First Name is required"),
        ("Alexandru", "", "700715", "Error: Last Name is required"),
        ("Alexandru", "Ciulin", "", "Error: Postal Code is required"),
    ]
)

def test_checkout_negative_parametrized(checkout_page, first_name, last_name, postal_code, expected_error):
    checkout_page.fill_customer_information(
        first_name,
        last_name,
        postal_code
    )

    assert (checkout_page.get_error_message() == expected_error)
