class CheckoutPage:
    def __init__(self, page):
        self.page = page

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