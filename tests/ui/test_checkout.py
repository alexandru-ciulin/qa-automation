import pytest
import allure

@allure.feature("Checkout")
@allure.story("Valid customer information")
@allure.title("Checkout overview is displayed after valid customer information")
def test_checkout_information(checkout_page):
    checkout_page.fill_customer_information("Alexandru", "Ciulin", "700715")

    assert checkout_page.is_overview_page_visible()

@pytest.mark.parametrize(
    "first_name, last_name, postal_code, expected_error",
    [
        ("", "Ciulin", "700715", "Error: First Name is required"),
        ("Alexandru", "", "700715", "Error: Last Name is required"),
        ("Alexandru", "Ciulin", "", "Error: Postal Code is required"),
    ]
)

@allure.feature("Checkout")
@allure.story("Invalid customer information")
@allure.title("Error message is displayed after invalid customer information")
def test_checkout_negative_parametrized(checkout_page, first_name, last_name, postal_code, expected_error):
    checkout_page.fill_customer_information(
        first_name,
        last_name,
        postal_code
    )

    assert (checkout_page.get_error_message() == expected_error)

@allure.feature("Checkout")
@allure.story("Full checkout process flow")
@allure.title("Order is completed successfully")
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

    