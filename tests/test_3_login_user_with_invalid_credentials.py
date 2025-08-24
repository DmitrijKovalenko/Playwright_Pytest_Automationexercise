import pytest
import allure


def test_login_user_with_invalid_credentials(home_page,login_page,fake_user_data):
    fake_user = fake_user_data["invalid"][0]
    home_page.navigate()
    home_page.verify_home_page_is_visible()
    home_page.click_login_signup_button()
    login_page.is_visible_title_login_to_your_account()
    login_page.fill_login_email(fake_user["email"])
    login_page.fill_password(fake_user["password"])
    login_page.click_login_button()
    login_page.is_visible_login_password_error_msg()
