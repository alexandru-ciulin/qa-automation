class CartPage:
    def __init__(self, page):
        self.page = page

    def is_product_in_cart(self, product_name):
        return self.page.get_by_text(product_name).is_visible()
