import allure
from pages.base_page import BasePage


class SignupPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.URL = "https://automationexercise.com/signup"

    @property
    def title_enter_accout_information(self):
        return self.page.locator('//b[text()="Enter Account Information"]')

    @allure.step("Verify 'Enter Account Information' title is visible")
    def is_visible_title_enter_accout_information(self):
        return self.title_enter_accout_information.is_visible()

    @property
    def gender_male(self):
        return self.page.locator("#id_gender1")

    @allure.step("Click 'Mr.' gender radio button")
    def click_gender_male(self):
        self.gender_male.click()

    @property
    def newsletter(self):
        return self.page.locator("#newsletter")

    @allure.step("Click 'Sign up for our newsletter!' checkbox")
    def click_newsletter(self):
        self.newsletter.click()

    @property
    def special_offers(self):
        return self.page.locator("#optin")

    @allure.step("Click 'Receive special offers from our partners!' checkbox")
    def click_special_offers(self):
        self.special_offers.click()

    @allure.step("Fill in password")
    def fill_password(self, name: str):
        self.fill_field("#password", name)

    @property
    def select_day(self):
        return self.page.locator('select[id="days"]')

    @allure.step("Select day: '1'")
    def select_day_1(self):
        self.select_day.select_option("1")

    @property
    def select_month(self):
        return self.page.locator('select[id="months"]')

    @allure.step("Select month: '1'")
    def select_month_1(self):
        self.select_month.select_option("1")

    @property
    def select_year(self):
        return self.page.locator('select[id="years"]')

    @allure.step("Select year: '2001'")
    def select_year_2001(self):
        self.select_year.select_option("2001")

    @property
    def first_name(self):
        return self.page.locator("#first_name")

    @allure.step("Fill in first name: '{first_name}'")
    def fill_first_name(self, first_name: str):
        self.fill_field("#first_name", first_name)

    @allure.step("Fill in last name: '{Last_name}'")
    def fill_Last_name(self, Last_name: str):
        self.fill_field("#last_name", Last_name)

    @allure.step("Fill in company: '{company}'")
    def fill_company(self, company: str):
        self.fill_field("#company", company)

    @allure.step("Fill in address: '{address}'")
    def fill_address(self, address: str):
        self.fill_field("#address1", address)

    @allure.step("Fill in address 2: '{address2}'")
    def fill_address2(self, address2: str):
        self.fill_field("#address2", address2)

    @property
    def select_country(self):
        return self.page.locator('select[name="country"]')

    @allure.step("Select country: 'United States'")
    def select_country_US(self):
        self.select_country.select_option("United States")

    @allure.step("Fill in state: '{state}'")
    def fill_state(self, state: str):
        self.fill_field("#state", state)

    @allure.step("Fill in city: '{city}'")
    def fill_city(self, city: str):
        self.fill_field("#city", city)

    @allure.step("Fill in zipcode: '{zipcode}'")
    def fill_zipcode(self, zipcode: str):
        self.fill_field("#zipcode", zipcode)

    @allure.step("Fill in mobile number: '{mobile_number}'")
    def fill_mobile_number(self, mobile_number: str):
        self.fill_field("#mobile_number", mobile_number)

    @property
    def create_account_button(self):
        return self.page.locator('button[data-qa="create-account"]')

    @allure.step("Click 'Create Account' button")
    def click_create_account_button(self):
        self.create_account_button.click()