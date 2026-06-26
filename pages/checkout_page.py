from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def fill_customer_information(
            self,
            first_name,
            last_name,
            postal_code
    ):
        self.page.get_by_placeholder("First Name").fill(first_name)
        self.page.get_by_placeholder("Last Name").fill(last_name)
        self.page.get_by_placeholder("Postal Code").fill(postal_code)

        self.page.get_by_role("button", name = "Continue").click()
    
    def is_overview_page_visible(self):
        return self.page.get_by_text("Checkout: Overview").is_visible()
    
    def finish_order(self):
        self.page.get_by_role("button", name="Finish").click()

    def is_order_completed(self):
        return self.page.get_by_text("Thank you for your order!").is_visible()
    
    def is_error_visible(self):
        return self.page.locator("[data-test='error']").is_visible()
    
    def get_error_message(self):
        return self.page.locator("[data-test='error']").inner_text()
    
    def is_checkout_step_one_visible(self):
        return self.page.get_by_text("Checkout: Your Information").is_visible()
    

