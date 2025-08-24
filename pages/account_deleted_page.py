import allure
from playwright.sync_api import Page

class AccountDeletedPage:

    def __init__(self, page: Page):
        self.page = page
        self.URL = "https://www.automationexercise.com/delete_account"

    @property
    def title_account_deleted(self):
        return self.page.locator('h2[data-qa="account-deleted"]')

    @allure.step("Verify 'Account Deleted' title is visible")
    def is_visible_title_account_deletedd(self):
        return self.title_account_deleted.is_visible()