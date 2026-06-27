import allure

@allure.feature("Cart")
@allure.story("Product in cart")
@allure.title("Check product in cart after addition")
def test_product_in_cart(products_page):
    products_page.add_product_to_cart("Sauce Labs Backpack")
    
    cart_page = products_page.open_cart()

    assert cart_page.is_product_in_cart("Sauce Labs Backpack")

@allure.feature("Cart")
@allure.story("Product not in cart")
@allure.title("Check product not in cart after removal")
def test_remove_product_from_cart(products_page):
    products_page.add_product_to_cart("Sauce Labs Backpack")

    cart_page = products_page.open_cart()
    
    cart_page.remove_product("Sauce Labs Backpack")

    assert not cart_page.is_product_in_cart("Sauce Labs Backpack")

@allure.feature("Cart")
@allure.story("Products in cart")
@allure.title("Check products in cart after addition")
def test_add_multiple_products_to_cart(products_page):
    products_page.add_product_to_cart("Sauce Labs Backpack")
    products_page.add_product_to_cart("Sauce Labs Bike Light")

    cart_page = products_page.open_cart()

    items = cart_page.get_cart_items()

    assert "Sauce Labs Backpack" in items
    assert "Sauce Labs Bike Light" in items

    assert items == ["Sauce Labs Backpack", "Sauce Labs Bike Light"]

@allure.feature("Cart")
@allure.story("Cart badge update")
@allure.title("Check cart badge updating after products addition")
def test_cart_badge_consistency(products_page):
    products_page.add_product_to_cart("Sauce Labs Backpack")
    products_page.add_product_to_cart("Sauce Labs Bike Light")

    assert products_page.get_cart_badge_count() == 2

    cart_page = products_page.open_cart()

    items = cart_page.get_cart_items()

    expected_items = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]

    assert items == expected_items

@allure.feature("Cart")
@allure.story("Cart badge update")
@allure.title("Check cart badge updating after products removal")
def test_remove_product_updates_cart_state(products_page):
    products_page.add_product_to_cart("Sauce Labs Backpack")
    products_page.add_product_to_cart("Sauce Labs Bike Light")

    assert products_page.get_cart_badge_count() == 2

    cart_page = products_page.open_cart()

    cart_page.remove_product("Sauce Labs Bike Light")

    assert not cart_page.is_product_in_cart("Sauce Labs Bike Light")

    cart_page.continue_shopping()

    from pages.products_page import ProductsPage
    products_page = ProductsPage(cart_page.page)

    assert products_page.get_cart_badge_count() == 1

@allure.feature("Cart")
@allure.story("Cart total price")
@allure.title("Check total price for order")
def test_cart_total_price(products_page):
    products_page.add_product_to_cart("Sauce Labs Backpack")
    products_page.add_product_to_cart("Sauce Labs Bike Light")

    cart_page = products_page.open_cart()

    prices = cart_page.get_cart_prices()

    assert sum(prices) == 39.98



