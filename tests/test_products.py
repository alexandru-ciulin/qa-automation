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


