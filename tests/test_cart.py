def test_product_in_cart(products_page):
    products_page.add_product_to_cart("Sauce Labs Backpack")
    
    cart_page = products_page.open_cart()

    assert cart_page.is_product_in_cart("Sauce Labs Backpack")

def test_remove_product_from_cart(products_page):
    products_page.add_product_to_cart("Sauce Labs Backpack")

    cart_page = products_page.open_cart()
    
    cart_page.remove_product("Sauce Labs Backpack")

    assert not cart_page.is_product_in_cart("Sauce Labs Backpack")

def test_add_multiple_products_to_cart(products_page):
    products_page.add_product_to_cart("Sauce Labs Backpack")
    products_page.add_product_to_cart("Sauce Labs Bike Light")

    cart_page = products_page.open_cart()

    items = cart_page.get_cart_items()

    assert "Sauce Labs Backpack" in items
    assert "Sauce Labs Bike Light" in items

    assert items == ["Sauce Labs Backpack", "Sauce Labs Bike Light"]