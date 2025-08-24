import allure
from pages.base_page import BasePage


class ProductDetailsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.URL_PREFIX = "https://automationexercise.com/product_details/"

    @allure.step("Verify user is on the product details page")
    def verify_on_product_details_page(self):
        assert self.page.url.startswith(
            self.URL_PREFIX
        ), f"Not on the product details page. Current URL: {self.page.url}"

    @property
    def product_name(self):
        return self.page.locator('//span[text()="Blue Top"]')

    @allure.step("Verify product name is visible")
    def is_visible_product_name(self):
        return self.product_name.is_visible()

    @property
    def category(self):
        return self.page.locator('//p[text()="Category: Women > Tops"]')

    @allure.step("Verify product category is visible")
    def is_visible_category(self):
        return self.category.is_visible()

    @property
    def price(self):
        return self.page.locator("//span[text()='Rs. 500']")

    @allure.step("Verify product price is visible")
    def is_visible_price(self):
        return self.price.is_visible()

    @property
    def availability(self):
        return self.page.locator("//p/b[text()='Availability:']")

    @allure.step("Verify product availability is visible")
    def is_visible_availability(self):
        return self.availability.is_visible()

    @property
    def condition(self):
        return self.page.locator("//p/b[text()='Condition:']")

    @allure.step("Verify product condition is visible")
    def is_visible_condition(self):
        return self.condition.is_visible()

    @property
    def brand(self):
        return self.page.locator("//p/b[text()='Brand:']")

    @allure.step("Verify product brand is visible")
    def is_visible_brand(self):
        return self.brand.is_visible()

    @allure.step("Get product detail for label: '{label}'")
    def get_product_detail_row(self, label: str):
        return self.page.locator(f"//p/b[text()='{label}:']")

    @allure.step("Verify product detail for label '{label}' is visible")
    def is_product_detail_visible(self, label: str) -> bool:
        return self.get_product_detail_row(label).is_visible()

    @property
    def quantity_input(self):
        return self.page.locator("#quantity")

    @allure.step("Set product quantity to {quantity}")
    def set_quantity(self, quantity: int):
        self.quantity_input.fill(str(quantity))

    @property
    def add_to_cart(self):
        return self.page.locator(".btn.btn-default.cart")

    @allure.step("Click 'Add to Cart' button")
    def click_add_to_cart(self):
        return self.add_to_cart.click()

    @property
    def review(self):
        return self.page.locator("#review-form #review")

    @allure.step("Verify 'Review' section is visible")
    def is_visible_review(self):
        return self.review.is_visible()

    @allure.step("Fill in review name: '{name}'")
    def fill_name(self, name: str):
        self.fill_field("#review-form #name", name)

    @allure.step("Fill in review email: '{email}'")
    def fill_email(self, email: str):
        self.fill_field("#review-form #email", email)

    @allure.step("Fill in review text: '{review}'")
    def fill_review(self, review: str):
        self.fill_field("#review-form #review", review)

    @property
    def submit_review_button(self):
        return self.page.locator("#button-review")

    @allure.step("Click 'Submit' button for review")
    def click_submit_review_button(self):
        return self.submit_review_button.click()

    @property
    def thanks_submit_message(self):
        return self.page.locator('//span[text()="Thank you for your review."]')

    @allure.step("Verify 'Thank you for your review.' message is visible")
    def is_visible_thanks_submit_message(self):
        return self.thanks_submit_message.is_visible()
    
    def wait_for_review_form(self):
        self.page.wait_for_selector("#review-form", state="visible", timeout=60000)