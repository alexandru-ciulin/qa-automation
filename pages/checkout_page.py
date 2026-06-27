from pages.base_page import BasePage
import allure

class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def fill_customer_information(
            self,
            first_name,
            last_name,
            postal_code
    ):
        with allure.step("Enter first name"):
            self.page.get_by_placeholder("First Name").fill(first_name)

        with allure.step("Enter last name"):
            self.page.get_by_placeholder("Last Name").fill(last_name)

        with allure.step("Enter postal code"):
            self.page.get_by_placeholder("Postal Code").fill(postal_code)

        with allure.step("Proceed to checkout overview"):
            self.page.get_by_role("button", name = "Continue").click()
    
    def is_overview_page_visible(self):
        with allure.step("Display Checkout: Overview page"):
            return self.page.get_by_text("Checkout: Overview").is_visible()
    
    def finish_order(self):
        with allure.step("Finish order"):
            self.page.get_by_role("button", name="Finish").click()

    def is_order_completed(self):
        with allure.step("Display order completion message"):
            return self.page.get_by_text("Thank you for your order!").is_visible()
    
    def is_error_visible(self):
        with allure.step("Check for error message"):
            return self.page.locator("[data-test='error']").is_visible()
    
    def get_error_message(self):
        with allure.step("Get error message"):
            return self.page.locator("[data-test='error']").inner_text()
    
    def is_checkout_step_one_visible(self):
        with allure.step("Verify checkout step one is displayed"):
            return self.page.get_by_text("Checkout: Your Information").is_visible()
    

