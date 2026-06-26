from pages.cart_page import CartPage
from pages.base_page import BasePage

class ProductsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
   
    def is_products_title_visible(self):
        return self.page.get_by_text("Products").is_visible()
    
    def is_product_visible(self, product_name):
        return self.page.get_by_text(product_name).is_visible()
    
    def select_product(self, product_name):
        self.page.get_by_text(product_name).click()

    def get_products_count(self):
        return self.page.get_by_role("button", name="Add to cart").count()
    
    def is_product_details_page(self):
        return "inventory-item" in self.page.url
    
    def add_product_to_cart(self, product_name):
        product = self.page.locator(".inventory_item", has_text=product_name)

        product.get_by_role("button", name="Add to cart").click()
    
    def open_cart(self):
        self.page.locator(".shopping_cart_link").click()

        return CartPage(self.page)

    def get_cart_badge_count(self):
        cart_badge_count =  self.page.locator(".shopping_cart_badge").inner_text()
        return int(cart_badge_count)
    
    def get_product_names(self):
        return self.page.locator(".inventory_item_name").all_inner_texts()
    
    def sort_products(self, option):
        self.page.locator(".product_sort_container").select_option(option)

    def get_product_prices(self):
        products_price = self.page.locator(".inventory_item_price").all_inner_texts()
        clean_prices = []
        for price in products_price:
            price = price.replace("$", "")
            clean_prices.append(float(price))
        return clean_prices
    
    def get_products_as_dict(self):
        product_names = self.get_product_names()
        product_prices = self.get_product_prices()

        return dict(zip(product_names, product_prices))

