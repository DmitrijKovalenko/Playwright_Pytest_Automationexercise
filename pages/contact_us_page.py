import allure
from pages.base_page import BasePage


class ContactPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.URL = "https://automationexercise.com/contact_us"

    @property
    def title_get_in_touch(self):
        return self.page.locator(".contact-form .title.text-center")

    @allure.step("Verify 'GET IN TOUCH' title is visible")
    def is_visible_title_get_in_touch(self):
        return self.title_get_in_touch.is_visible()

    @allure.step("Fill in name: '{name}'")
    def fill_name(self, name: str):
        self.fill_field("input[name='name']", name)

    @allure.step("Fill in email: '{name}'")
    def fill_email(self, name: str):
        self.fill_field('input[name="email"]', name)

    @allure.step("Fill in subject: '{name}'")
    def fill_subject(self, name: str):
        self.fill_field('input[name="subject"]', name)

    @allure.step("Fill in message: '{name}'")
    def fill_message(self, name: str):
        self.fill_field('#message', name)

    @property
    def upload_file_field(self):
        return self.page.locator('input[name="upload_file"]')

    @allure.step("Upload file: '{file_path}'")
    def upload_file(self, file_path: str):
        self.upload_file_field.set_input_files(file_path)

    @property
    def submit_button(self):
        return self.page.locator('input[name="submit"]')

    @allure.step("Click 'Submit' button")
    def click_submit_button(self):
        self.submit_button.click()

    @property
    def succes_message(self):
        return self.page.locator(".status.alert.alert-success")

    @allure.step("Verify success message is visible")
    def is_visible_succes_message(self):
        return self.succes_message.is_visible()