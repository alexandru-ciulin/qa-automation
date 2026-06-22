from pages.products_page import ProductsPage

def test_products_after_login(products_page):
    assert products_page.is_products_title_visible()

def test_product_backpack(products_page):    
    assert products_page.is_product_visible("Sauce Labs Backpack")

def test_product_count(products_page):
    assert products_page.get_products_count() == 6

def test_add_product_to_cart(products_page):
    products_page.add_product_to_cart("Sauce Labs Backpack")
    assert products_page.get_cart_badge_count() == 1

def test_cart_badge_updates(products_page):
    products_page.add_product_to_cart("Sauce Labs Backpack")

    assert products_page.get_cart_badge_count() == 1

    products_page.add_product_to_cart("Sauce Labs Bike Light")

    assert products_page.get_cart_badge_count() == 2

    cart_page = products_page.open_cart()

    cart_page.remove_product("Sauce Labs Backpack")

    products_page = cart_page.continue_shopping()

    assert products_page.get_cart_badge_count() == 1


