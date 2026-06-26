def test_products_have_correct_prices(products_page):
    products = products_page.get_products_as_dict()

    assert products["Sauce Labs Backpack"] == 29.99
    assert products["Sauce Labs Bike Light"] == 9.99

def test_product_price_is_correct(products_page):
    products = products_page.get_products_as_dict()

    assert products["Test.allTheThings() T-Shirt (Red)"] == 15.99