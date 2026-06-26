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

def test_sort_products_a_to_z(products_page):
    products_page.sort_products("az")
    
    names = products_page.get_product_names()

    assert names == sorted(names)

def test_sort_products_z_to_a(products_page):
    products_page.sort_products("za")

    names = products_page.get_product_names()
    
    assert names == sorted(names, reverse=True)

def test_sort_products_price_low_to_high(products_page):
    products_page.sort_products("lohi")
    
    products_price = products_page.get_product_prices()

    assert products_price == sorted(products_price)

def test_sort_products_price_high_to_low(products_page):
    products_page.sort_products("hilo")
    
    products_price = products_page.get_product_prices()
    
    assert products_price == sorted(products_price, reverse=True)

