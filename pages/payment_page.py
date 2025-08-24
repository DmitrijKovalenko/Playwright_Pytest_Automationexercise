import allure
from pages.base_page import BasePage


class PaymentPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.URL = "https://automationexercise.com/payment"

    @allure.step("Fill in name on card: '{name}'")
    def fill_name_on_card(self, name: str):
        self.fill_field('input[data-qa="name-on-card"]', name)

    @allure.step("Fill in card number")
    def fill_card_number(self, card_number: str):
        self.fill_field('input[data-qa="card-number"]', card_number)

    @allure.step("Fill in CVC: '{cvc}'")
    def fill_cvc(self, cvc: str):
        self.fill_field('input[data-qa="cvc"]', cvc)

    @allure.step("Fill in expiry month: '{month}'")
    def fill_expiry_month(self, month: str):
        self.fill_field('input[data-qa="expiry-month"]', month)

    @allure.step("Fill in expiry year: '{year}'")
    def fill_expiry_year(self, year: str):
        self.fill_field('input[data-qa="expiry-year"]', year)

    @property
    def pay_and_confirm_button(self):
        return self.page.locator('button[data-qa="pay-button"]')

    @allure.step("Click 'Pay and Confirm' button")
    def click_pay_and_confirm_button(self):
        self.pay_and_confirm_button.click()

    @property
    def order_placed_succesfull_message(self):
        return self.page.locator(".col-md-12.form-group.hide")

    @allure.step("Verify 'Order Placed Successfully' message is visible")
    def is_visible_order_placed_succesfull_message(self):
        return self.order_placed_succesfull_message.is_visible()

    @property
    def download_invoice(self):
        return self.page.locator('//a[text()="Download Invoice"]')

    @allure.step("Click 'Download Invoice' link")
    def click_download_invoice(self):
        self.download_invoice.click()

    @property
    def continue_button(self):
        return self.page.locator('a[data-qa="continue-button"]')

    @allure.step("Click 'Continue' button")
    def click_continue_button(self):
        self.continue_button.click()