import allure
from playwright.sync_api import Page


class ModalPage:
    def __init__(self, page: Page):
        self.page = page

    @property
    def continue_shopping_button(self):
        return self.page.locator('button[data-dismiss="modal"]')

    @allure.step("Click 'Continue Shopping' button")
    def click_continue_shopping(self):
        self.continue_shopping_button.click()

    @property
    def view_cart_button(self):
        return self.page.locator('.text-center a[href="/view_cart"]')

    @allure.step("Click 'View Cart' button")
    def click_view_cart(self):
        self.view_cart_button.click()

    @property
    def register_login_button(self):
        return self.page.locator('//u[text()="Register / Login"]')

    @allure.step("Click 'Register / Login' button")
    def click_register_login_button(self):
        self.register_login_button.click()