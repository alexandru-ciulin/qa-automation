from pages.checkout_page import CheckoutPage

class CartPage:
    def __init__(self, page):
        self.page = page

    def is_product_in_cart(self, product_name):
        return self.page.get_by_text(product_name).is_visible()
    
    def remove_product(self, product_name):
        product = self.page.locator(".cart_item", has_text = product_name)
        product.get_by_role("button", name="Remove").click()

    def open_checkout(self):
        self.page.get_by_role("button", name="Checkout").click()

        return CheckoutPage(self.page)
    
    def get_cart_items(self):
        return self.page.locator(".inventory_item_name").all_inner_texts()
    
    def continue_shopping(self):
        self.page.get_by_role("button", name="Continue Shopping").click()