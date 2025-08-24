import allure
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.URL = "https://automationexercise.com/"

    @allure.step("Navigate to the home page")
    def navigate(self):
        self.page.goto(self.URL)

    @property
    def login_signup_button(self):
        return self.page.locator(".shop-menu.pull-right ul li:nth-child(4)")

    @allure.step("Click 'Login / Signup' button")
    def click_login_signup_button(self):
        self.login_signup_button.click()

    @allure.step("Verify home page is visible")
    def verify_home_page_is_visible(self):
        assert self.page.url == self.URL, f"Incorrect URL: {self.page.url}"

    @property
    def logged_in_as(self):
        return self.page.locator("div ul li:last-child .fa.fa-user")

    @allure.step("Verify 'Logged in as' is visible")
    def is_visible_logged_in_as(self):
        return self.logged_in_as.is_visible()

    @property
    def delete_account(self):
        return self.page.locator(".shop-menu.pull-right ul li:nth-child(5)")

    @allure.step("Click 'Delete Account' button")
    def click_delete_account(self):
        return self.delete_account.click()

    @property
    def logout_button(self):
        return self.page.locator(".shop-menu.pull-right ul li:nth-child(4)")

    @allure.step("Click 'Logout' button")
    def click_logout_button(self):
        return self.logout_button.click()

    @property
    def contact_us_button(self):
        return self.page.locator('a[href="/contact_us"]')

    @allure.step("Click 'Contact Us' button")
    def click_contact_us_button(self):
        return self.contact_us_button.click()

    @property
    def home_button(self):
        return self.page.locator("div ul li:first-child .fa")

    @allure.step("Click 'Home' button")
    def click_home_button(self):
        return self.home_button.click()

    @property
    def test_cases_button(self):
        return self.page.locator(".shop-menu.pull-right ul li:nth-child(5)")

    @allure.step("Click 'Test Cases' button")
    def click_test_cases_button(self):
        return self.test_cases_button.click()

    @property
    def products_button(self):
        return self.page.locator(".shop-menu.pull-right ul li:nth-child(2)")

    @allure.step("Click 'Products' button")
    def click_products_button(self):
        return self.products_button.click()

    @property
    def footer(self):
        return self.page.locator("#footer .footer-widget")

    @allure.step("Scroll to footer")
    def scroll_to_footer(self):
        self.footer.scroll_into_view_if_needed()

    @property
    def subscription(self):
        return self.page.locator('//h2[text()="Subscription"]')

    @allure.step("Verify 'Subscription' title is visible")
    def is_visible_subscription(self):
        return self.subscription.is_visible()

    @allure.step("Fill in subscription email: '{name}'")
    def fill_subscribe_email(self, name: str):
        self.fill_field("#susbscribe_email", name)

    @property
    def subscribe_button(self):
        return self.page.locator("#subscribe")

    @allure.step("Click 'Subscribe' button")
    def click_subscribe_button(self):
        return self.subscribe_button.click()

    @property
    def succesfull_subscribe_message(self):
        return self.page.locator('.alert-success.alert')

    @allure.step("Verify successful subscription message is visible")
    def is_visible_succesfull_subscribe_message(self):
        return self.succesfull_subscribe_message.is_visible()

    @property
    def cart_button(self):
        return self.page.locator(".shop-menu.pull-right ul li:nth-child(3)")

    @allure.step("Click 'Cart' button")
    def click_cart_button(self):
        return self.cart_button.click()

    @property
    def woman_catagory(self):
        return self.page.locator('a[href="#Women"]')

    @allure.step("Click 'Woman' category")
    def click_woman_catagory(self):
        return self.woman_catagory.click()

    @property
    def left_sidebar(self):
        return self.page.locator(".left-sidebar")

    @allure.step("Verify left sidebar is visible")
    def is_visible_left_sidebar(self):
        return self.left_sidebar.is_visible()

    @property
    def dress(self):
        return self.page.locator('a[href="/category_products/1"]')

    @allure.step("Click 'Dress' sub-category")
    def click_dress(self):
        return self.dress.click()

    @property
    def title_woman_products(self):
        return self.page.locator('//h2[text()="Women - Dress Products"]')

    @allure.step("Verify 'Women - Dress Products' title is visible")
    def is_visible_title_woman_products(self):
        return self.title_woman_products.is_visible()

    @property
    def men_catagory(self):
        return self.page.locator('a[href="#Men"]')

    @allure.step("Click 'Men' category")
    def click_men_catagory(self):
        return self.men_catagory.click()

    @property
    def t_shirt(self):
        return self.page.locator('a[href="/category_products/3"]')

    @allure.step("Click 'T-Shirt' sub-category")
    def click_t_shirt(self):
        return self.t_shirt.click()

    @property
    def title_men_products(self):
        return self.page.locator('//h2[text()="Men - Tshirts Products"]')

    @allure.step("Verify 'Men - Tshirts Products' title is visible")
    def is_visible_title_men_products(self):
        return self.title_men_products.is_visible()

    @property
    def brands(self):
        return self.page.locator('//h2[text()="Brands"]')

    @allure.step("Verify 'Brands' section is visible")
    def is_visible_brands(self):
        return self.brands.is_visible()

    @property
    def polo(self):
        return self.page.locator('a[href="/brand_products/Polo"]')

    @allure.step("Click 'Polo' brand link")
    def click_polo(self):
        return self.polo.click()

    @allure.step("Click '{brand_name}' brand link")
    def click_brand_link(self, brand_name: str):
        brand_link_locator = self.page.locator(f"a[href='/brand_products/{brand_name}']")
        brand_link_locator.click()

    @property
    def recommended_items(self):
        return self.page.locator('//h2[text()="recommended items"]')

    @allure.step("Verify 'Recommended Items' section is visible")
    def is_visible_recommended_items(self):
        return self.recommended_items.is_visible()

    @property
    def scrollup(self):
        return self.page.locator("#scrollUp")

    @allure.step("Click 'Scroll Up' button")
    def click_scrollup(self):
        return self.scrollup.click()

    @property
    def title_full_flaged(self):
        return self.page.locator("//div[@class='item active']//h2[text()='Full-Fledged practice website for Automation Engineers']")

    @allure.step("Verify 'Full-Fledged...' title is visible")
    def is_visible_title_full_flaged(self):
        return self.title_full_flaged.is_visible()