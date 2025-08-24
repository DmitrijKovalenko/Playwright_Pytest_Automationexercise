import pytest
import allure
import random
from faker import Faker
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.account_created_page import AccountCreatedPage
from pages.account_deleted_page import AccountDeletedPage
from pages.contact_us_page import ContactPage
from pages.testcases_page import TestCasePage
from pages.products_page import ProductsPage
from pages.product_details_page import ProductDetailsPage
from pages.view_cart_page import ViewCartPage
from pages.modal_page import ModalPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage
from pages.brand_page import BrandPage
@pytest.fixture
def home_page(page):
    return HomePage(page)


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def signup_page(page):
    return SignupPage(page)


@pytest.fixture
def account_created_page(page):
    return AccountCreatedPage(page)


@pytest.fixture
def account_deleted_page(page):
    return AccountDeletedPage(page)


@pytest.fixture
def contact_us_page(page):
    return ContactPage(page)


@pytest.fixture
def test_cases_page(page):
    return TestCasePage(page)


@pytest.fixture
def products_page(page):
    return ProductsPage(page)


@pytest.fixture
def product_details_page(page):
    return ProductDetailsPage(page)


@pytest.fixture
def view_cart_page(page):
    return ViewCartPage(page)


@pytest.fixture
def modal_page(page):
    return ModalPage(page)


@pytest.fixture
def checkout_page(page):
    return CheckoutPage(page)


@pytest.fixture
def payment_page(page):
    return PaymentPage(page)


@pytest.fixture
def brand_page(page):
    return BrandPage(page)


@pytest.fixture(scope="session")
def browser_type_name(request):
    return request.config.getoption("browser")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if hasattr(item, "instance") and item.instance is not None:
        item.instance.rep_call = report


@pytest.fixture(autouse=True)
def attach_screenshot_on_fail(request, page):
    yield
    if hasattr(request.node, "instance") and request.node.instance is not None:
        if (
            hasattr(request.node.instance, "rep_call")
            and request.node.instance.rep_call.failed
        ):
            allure.attach(
                page.screenshot(),
                name="screenshot on fail",
                attachment_type=allure.attachment_type.PNG,
            )


@pytest.fixture
def fake_user_data():
    fake = Faker()
    unique_name = fake.unique.first_name() + str(random.randint(100, 999))
    unique_email = fake.unique.email() + str(random.randint(100, 999))

    valid_fake_data = {
        "name": unique_name,
        "email": unique_email,
        "password": fake.password(length=12),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "address": fake.street_address(),
        "address2": fake.secondary_address(),
        "country": "United States",
        "state": fake.state(),
        "city": fake.city(),
        "zipcode": fake.zipcode(),
        "mobile_number": fake.phone_number(),
        "company": fake.company(),
        "review": fake.text(),
    }

    invalid_fake_data = [
        {"name": "", "email": "", "password": "password123"},
    ]

    return {"valid": valid_fake_data, "invalid": invalid_fake_data}


@pytest.fixture
def real_user_data():

    return {
        "name": "Dimon",
        "email": "dmitrijkovalenko86@gmail.com",
        "password": "12345",
        "subject": "job",
        "message": "I want to work on complex and interesting projects",
        "first_name": "Dmytro",
        "last_name": "Kovalenko",
        "address": "Alishera-navoi",
        "address2": "Lesya-Kurbasa",
        "country": "United States",
        "state": "Kiev region",
        "city": "Kiev",
        "zipcode": "03194",
        "mobile_number": "0675069867",
        "company": "Test Squad",
    }


@pytest.fixture
def card_data():
    
    return {
        "name_on_card": "Dmytro Kovalenko",
        "card_number": "1234567890123456",
        "cvc": "123",
        "expiry_month": "12",
        "expiry_year": "2025",
    }

@pytest.fixture
def logged_in_user(page, home_page, login_page, signup_page, account_created_page, account_deleted_page):
    """Фікстура для реєстрації та входу користувача перед тестом."""
    fake = Faker()
    unique_name = fake.unique.first_name() + str(random.randint(100, 999))
    unique_email = fake.unique.email() + str(random.randint(100, 999))
    user_data = {
        "name": unique_name,
        "email": unique_email,
        "password": fake.password(length=12),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "address": fake.street_address(),
        "address2": fake.secondary_address(),
        "country": "United States",
        "state": fake.state(),
        "city": fake.city(),
        "zipcode": fake.zipcode(),
        "mobile_number": fake.phone_number(),
        "company": fake.company(),
        "review": fake.text(),
    }
    
    home_page.navigate()
    home_page.click_login_signup_button()
    login_page.is_visible_title_new_user_signup()
    login_page.fill_name(user_data["name"])
    login_page.fill_signup_email(user_data["email"])
    login_page.click_signup_button()
    signup_page.is_visible_title_enter_accout_information()
    signup_page.click_gender_male()
    signup_page.fill_password(user_data["password"])
    signup_page.select_day_1()
    signup_page.select_month_1()
    signup_page.select_year_2001()
    signup_page.click_newsletter()
    signup_page.click_special_offers()
    signup_page.fill_first_name(user_data["first_name"])
    signup_page.fill_Last_name(user_data["last_name"])
    signup_page.fill_company(user_data["company"])
    signup_page.fill_address(user_data["address"])
    signup_page.fill_address2(user_data["address2"])
    signup_page.select_country_US()
    signup_page.fill_state(user_data["state"])
    signup_page.fill_city(user_data["city"])
    signup_page.fill_zipcode(user_data["zipcode"])
    signup_page.fill_mobile_number(user_data["mobile_number"])
    signup_page.click_create_account_button()
    account_created_page.is_visible_title_account_created()
    account_created_page.click_continue_button()
    home_page.is_visible_logged_in_as()
       
    yield user_data

    
