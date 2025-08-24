import allure
from pages.base_page import BasePage


class ViewCartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.URL = "https://automationexercise.com/view_cart"

    @allure.step("Verify product with ID '{product_id}' is visible in cart")
    def is_product_visible_in_cart(self, product_id: int) -> bool:
        selector = f"#cart_items #product-{product_id}"
        locator = self.page.locator(selector)
        return locator.is_visible()

    @allure.step("Get product price for product with ID '{product_id}'")
    def get_product_price(self, product_id: int):
        return self.page.locator(f"#product-{product_id} .cart_price p")

    @allure.step("Get product quantity for product with ID '{product_id}'")
    def get_product_quantity(self, product_id: int):
        return self.page.locator(f"#product-{product_id} .cart_quantity button")

    @allure.step("Get total price for product with ID '{product_id}'")
    def get_product_total_price(self, product_id: int):
        return self.page.locator(f"#product-{product_id} .cart_total p")

    @property
    def proceed_checkout(self):
        return self.page.locator(".btn.btn-default.check_out")

    @allure.step("Click 'Proceed To Checkout' button")
    def click_proceed_checkout(self):
        self.proceed_checkout.click()

    @allure.step("Verify the cart page is displayed")
    def is_cart_page_displayed(self) -> bool:
        if self.page.url != self.URL:
            return False
        return (
            self.page.locator(".breadcrumbs .breadcrumb").text_content()
            == "Shopping Cart"
        )

    @allure.step("Delete product with ID '{product_id}' from the cart")
    def delete_product_by_id(self, product_id: int):
        delete_button_locator = self.page.locator(
            f'a.cart_quantity_delete[data-product-id="{product_id}"]'
        )
        delete_button_locator.click()
        product_locator = self.page.locator(f"#cart_items #product-{product_id}")
        product_locator.wait_for(state="hidden")

    @allure.step("Verify product with ID '{product_id}' is not visible in cart")
    def is_product_not_visible_in_cart(self, product_id: int) -> bool:
        selector = f"#cart_items #product-{product_id}"
        locator = self.page.locator(selector)
        return locator.is_hidden()

    @property
    def title_empty_cart(self):
        return self.page.locator("#empty_cart")

    @allure.step("Verify 'Cart is empty' title is visible")
    def is_visible_title_empty_cart(self):
        return self.title_empty_cart.is_visible()