class ProductsPage:
    def __init__(self, page):
        self.page = page
   
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
    
