import allure
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.URL = "https://automationexercise.com/login"

    @property
    def title_new_user_signup(self):
        return self.page.locator(".signup-form h2")

    @allure.step("Verify 'New User Signup!' title is visible")
    def is_visible_title_new_user_signup(self):
        return self.title_new_user_signup.is_visible()

    @property
    def title_login_to_your_account(self):
        return self.page.locator('//h2[text()="Login to your account"]')

    @allure.step("Verify 'Login to your account' title is visible")
    def is_visible_title_login_to_your_account(self):
        return self.title_login_to_your_account.is_visible()

    @property
    def input_name(self):
        return self.page.locator("input[name='name']")

    @allure.step("Fill in name: '{name}'")
    def fill_name(self, name: str):
        self.fill_field("input[name='name']", name)

    @allure.step("Fill in signup email: '{email}'")
    def fill_signup_email(self, email: str):
        self.fill_field('input[data-qa="signup-email"]', email)

    @property
    def signup_button(self):
        return self.page.locator('button[data-qa="signup-button"]')

    @allure.step("Click 'Signup' button")
    def click_signup_button(self):
        self.signup_button.click()

    @allure.step("Fill in login password")
    def fill_password(self, password: str):
        self.fill_field('input[data-qa="login-password"]', password)

    @allure.step("Fill in login email: '{email}'")
    def fill_login_email(self, email: str):
        self.fill_field('input[data-qa="login-email"]', email)

    @property
    def login_button(self):
        return self.page.locator('button[data-qa="login-button"]')

    @allure.step("Click 'Login' button")
    def click_login_button(self):
        self.login_button.click()

    @property
    def login_password_error_msg(self):
        return self.page.locator('//p[text()="Your email or password is incorrect!"]')

    @allure.step("Verify 'Your email or password is incorrect!' error message is visible")
    def is_visible_login_password_error_msg(self):
        return self.login_password_error_msg.is_visible()

    @allure.step("Verify user is on the login page")
    def verify_on_login_page(self):
        assert (
            self.page.url == self.URL
        ), f"Not on the login page. Current URL: {self.page.url}"

    @property
    def already_exist_error_msg(self):
        return self.page.locator('//p[text()="Email Address already exist!"]')

    @allure.step("Verify 'Email Address already exist!' error message is visible")
    def is_visible_already_exist_error_msgg(self):
        return self.already_exist_error_msg.is_visible()