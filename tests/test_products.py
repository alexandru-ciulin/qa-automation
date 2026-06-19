from pages.products_page import ProductsPage
from pages.cart_page import CartPage


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
