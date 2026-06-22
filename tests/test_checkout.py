import pytest

def test_checkout_information(checkout_page):
    checkout_page.fill_customer_information("Alexandru", "Ciulin", "700715")

    assert checkout_page.is_overview_page_visible()

    assert "checkout-step-two" in checkout_page.page.url

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

def test_cart_to_checkout_flow(products_page):
    products_page.add_product_to_cart("Sauce Labs Backpack")
    products_page.add_product_to_cart("Sauce Labs Bike Light")

    cart_page = products_page.open_cart()

    items = cart_page.get_cart_items()

    expected_items = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]

    assert items == expected_items

    checkout_page = cart_page.open_checkout()

    assert checkout_page.is_checkout_step_one_visible()

def test_complete_checkout_flow(products_page):
    products_page.add_product_to_cart("Sauce Labs Backpack")
    products_page.add_product_to_cart("Sauce Labs Bike Light")

    cart_page = products_page.open_cart()

    items = cart_page.get_cart_items()

    expected_items = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]

    assert items == expected_items

    checkout_page = cart_page.open_checkout()

    assert checkout_page.is_checkout_step_one_visible()

    checkout_page.fill_customer_information(
        "Alexandru",
        "Ciulin",
        "700715"
    )

    assert checkout_page.is_overview_page_visible()

    checkout_page.finish_order()

    assert checkout_page.is_order_completed()