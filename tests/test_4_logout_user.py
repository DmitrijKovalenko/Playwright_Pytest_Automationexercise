import pytest
import allure


def test_logout_user(home_page,login_page,real_user_data,):
    user = real_user_data
    home_page.navigate()
    home_page.verify_home_page_is_visible()
    home_page.click_login_signup_button()
    login_page.is_visible_title_login_to_your_account()
    login_page.fill_login_email(user["email"])
    login_page.fill_password(user["password"])
    login_page.click_login_button()
    home_page.is_visible_logged_in_as()
    home_page.click_logout_button()
    login_page.verify_on_login_page()
