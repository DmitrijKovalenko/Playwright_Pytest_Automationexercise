import allure
from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def fill_field(self, locator: str, value: str):
        self.page.wait_for_timeout(1000)
        self.page.locator(locator).fill(value)
