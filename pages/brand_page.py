import allure
from playwright.sync_api import Page


class BrandPage:
    def __init__(self, page: Page):
        self.page = page
        self.URL = "https://automationexercise.com/brand_products/"

    @allure.step("Verify brand page for '{brand_name}' is displayed")
    def verify_brand_page_is_displayed(self, brand_name: str):
        expected_url = f"{self.URL}{brand_name}"
        expected_title = f"BRAND - {brand_name.upper()} PRODUCTS"
        self.page.wait_for_url(expected_url)
        title_locator = self.page.locator(f"h2:has-text('{expected_title}')")

        assert (
            title_locator.is_visible()
        ), f"Заголовок '{expected_title}' не знайдено на сторінці."
