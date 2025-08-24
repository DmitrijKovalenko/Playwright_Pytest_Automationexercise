import allure
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.URL = "https://automationexercise.com/contact_us"

    @allure.step("Get delivery address details")
    def get_delivery_address_details(self):
        return self.page.locator("#address_delivery")

    @allure.step("Get billing address details")
    def get_billing_address_details(self):
        return self.page.locator("#address_invoice")

    @allure.step("Verify that address contains all necessary parts")
    def verify_address_contains_all_parts(self, address_locator, address_parts: list):
        actual_text_cleaned = " ".join(address_locator.inner_text().split()).strip()
        for part in address_parts:
            expected_part_cleaned = " ".join(part.split()).strip()
            assert (
                expected_part_cleaned in actual_text_cleaned
            ), f"Expected part '{part}' not found in address text."

    @property
    def message_field(self):
        return self.page.locator('.form-control[name="message"]')

    @allure.step("Enter a comment: '{comment}'")
    def enter_comment(self, comment: str):
        self.message_field.fill(comment)

    @property
    def place_order_button(self):
        return self.page.locator('a[href="/payment"]')

    @allure.step("Click 'Place Order' button")
    def click_place_order(self):
        self.place_order_button.click()