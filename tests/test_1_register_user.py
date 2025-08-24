import pytest
import allure


def test_register_user(
    page,
    home_page,
    login_page,
    signup_page,
    account_created_page,
    account_deleted_page,
    fake_user_data,
):

    fake_user = fake_user_data["valid"]
    home_page.navigate()
    home_page.verify_home_page_is_visible()
    allure.attach(
        page.screenshot(path="screenshots/home_page_visible.png"),
        name="Домашня сторінка",
        attachment_type=allure.attachment_type.PNG,
    )
    home_page.click_login_signup_button()
    login_page.is_visible_title_new_user_signup()
    login_page.fill_name(fake_user["name"])
    login_page.fill_signup_email(fake_user["email"])
    login_page.click_signup_button()
    signup_page.is_visible_title_enter_accout_information()
    signup_page.click_gender_male()
    signup_page.fill_password(fake_user["password"])
    signup_page.select_day_1()
    signup_page.select_month_1()
    signup_page.select_year_2001()
    signup_page.click_newsletter()
    signup_page.click_special_offers()
    signup_page.fill_first_name(fake_user["first_name"])
    signup_page.fill_Last_name(fake_user["last_name"])
    signup_page.fill_company(fake_user["company"])
    signup_page.fill_address(fake_user["address"])
    signup_page.fill_address2(fake_user["address2"])
    signup_page.select_country_US()
    signup_page.fill_state(fake_user["state"])
    signup_page.fill_city(fake_user["city"])
    signup_page.fill_zipcode(fake_user["zipcode"])
    signup_page.fill_mobile_number(fake_user["mobile_number"])
    signup_page.click_create_account_button()
    account_created_page.is_visible_title_account_created()
    account_created_page.click_continue_button()
    home_page.is_visible_logged_in_as()
    home_page.click_delete_account()
    account_deleted_page.is_visible_title_account_deletedd()
