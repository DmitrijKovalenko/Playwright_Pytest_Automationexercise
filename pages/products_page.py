import allure
from pages.base_page import BasePage


class ProductsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.URL = "https://automationexercise.com/products"

    @property
    def title_all_products(self):
        return self.page.locator(".features_items .title.text-center")

    @allure.step("Verify 'ALL PRODUCTS' title is visible")
    def is_visible_title_all_products(self):
        return self.title_all_products.is_visible()

    @property
    def list_products(self):
        return self.page.locator(".features_items")

    @allure.step("Verify product list is visible")
    def is_visible_list_products(self):
        return self.list_products.is_visible()

    @allure.step("Click 'View Product' for product with ID '{product_id}'")
    def click_view_product_by_id(self, product_id: int):
        locator = self.page.locator(f'a[href="/product_details/{product_id}"]')
        locator.click()

    @allure.step("Fill in search field with: '{name}'")
    def fill_search_product(self, name: str):
        self.fill_field('input[placeholder="Search Product"]', name)

    @property
    def search_button(self):
        return self.page.locator("#submit_search")

    @allure.step("Click 'Search' button")
    def click_search_button(self):
        return self.search_button.click()

    @property
    def title_searched_products(self):
        return self.page.locator("//h2[text()='Searched Products']")

    @allure.step("Verify 'SEARCHED PRODUCTS' title is visible")
    def is_visible_title_searched_products(self):
        return self.title_searched_products.is_visible()

    @property
    def green_tshirt_name(self):
        return self.page.get_by_text("Green Side Placket Detail T-Shirt")

    @allure.step("Verify 'Green Side Placket Detail T-Shirt' is visible")
    def verify_green_tshirt_is_visible(self):
        assert self.green_tshirt_name.is_visible()

    @allure.step("Click 'View Product' for the first searched item")
    def click_view_product_for_searched_item(self):
        product_container = self.page.locator(
            ".features_items .product-image-wrapper"
        ).first
        view_product_link = product_container.locator('a:has-text("View Product")')
        view_product_link.click()

    @allure.step("Get product container for product with ID '{product_id}'")
    def get_product_container(self, product_id: int):
        return self.page.locator(f'div.col-sm-4:has(a[data-product-id="{product_id}"])')

    @allure.step("Click 'View Product' for product with ID '{product_id}'")
    def click_view_product_by_id(self, product_id: int):
        product_container = self.get_product_container(product_id)
        view_product_link = product_container.locator(
            f'a[href="/product_details/{product_id}"]'
        )
        view_product_link.click()

    @property
    def first_product(self):
        return self.page.locator(
            ".features_items .product-image-wrapper", has_text="Blue Top"
        )

    @allure.step("Add product with ID '{product_id}' to cart by hovering")
    def add_product_to_cart_by_id_on_hover(self, product_id: int):
        product_container = self.page.locator(
            f'.features_items div.col-sm-4:has(a[data-product-id="{product_id}"])'
        )
        product_container.wait_for(state='visible')
        product_container.hover()
        add_to_cart_button = product_container.locator(
            f'a[data-product-id="{product_id}"]'
        ).first
        add_to_cart_button.click()