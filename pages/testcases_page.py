import allure
from pages.base_page import BasePage


class TestCasePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.URL = "https://automationexercise.com/test_cases"

    @allure.step("Verify user is on the Test Cases page")
    def verify_on_test_page(self):
        assert (
            self.page.url == self.URL
        ), f"Not on the test case page. Current URL: {self.page.url}"