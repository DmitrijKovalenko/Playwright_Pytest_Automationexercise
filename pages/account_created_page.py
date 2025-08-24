import allure
from playwright.sync_api import Page


class AccountCreatedPage:
    def __init__(self, page: Page):
        self.page = page
        self.URL = "https://www.automationexercise.com/account_created"

    @property
    def title_account_created(self):
        return self.page.locator('h2[data-qa="account-created"]')

    @allure.step("Verify 'Account Created' title is visible")
    def is_visible_title_account_created(self):
        return self.title_account_created.is_visible()

    @property
    def continue_button(self):
        return self.page.locator(".btn.btn-primary")

    @allure.step("Click 'Continue' button")
    def click_continue_button(self):
        return self.continue_button.click()
