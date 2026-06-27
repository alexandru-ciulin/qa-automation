from pages.checkout_page import CheckoutPage
from pages.base_page import BasePage
import allure

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def is_product_in_cart(self, product_name):
        with allure.step("Verify product is present in cart"):
            return self.page.get_by_text(product_name).is_visible()
    
    def remove_product(self, product_name):
        with allure.step("Remove product from cart"):
            product = self.page.locator(".cart_item", has_text = product_name)
            product.get_by_role("button", name="Remove").click()

    def open_checkout(self):
        with allure.step("Open checkout"):
            self.page.get_by_role("button", name="Checkout").click()

            return CheckoutPage(self.page)
    
    def get_cart_items(self):
        with allure.step("Get products name from cart"):
            return self.page.locator(".inventory_item_name").all_inner_texts()
    
    def continue_shopping(self):
        with allure.step("Continue shopping"):
            self.page.get_by_role("button", name="Continue Shopping").click()
            
            return self.page

    def _clean_price(self, price):
        return float(price.replace("$", ""))

    def get_cart_prices(self):
        with allure.step("Retrieve cart product prices"):
            prices = self.page.locator(".inventory_item_price").all_inner_texts()
            
            return [self._clean_price(price) for price in prices]