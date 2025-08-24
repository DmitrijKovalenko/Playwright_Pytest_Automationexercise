import pytest
import allure


def test_register_user_with_existing_email(home_page,login_page,real_user_data):
    user = real_user_data
    home_page.navigate()
    home_page.verify_home_page_is_visible()
    home_page.click_login_signup_button()
    login_page.is_visible_title_new_user_signup()
    login_page.fill_name(user["name"])
    login_page.fill_signup_email(user["email"])
    login_page.click_signup_button()
    login_page.is_visible_already_exist_error_msgg()
