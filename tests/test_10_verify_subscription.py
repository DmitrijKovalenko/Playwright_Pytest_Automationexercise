import pytest
import allure


def test_verify_subscription( home_page, real_user_data):
    user = real_user_data
    home_page.navigate()
    home_page.verify_home_page_is_visible()
    home_page.scroll_to_footer()
    home_page.is_visible_subscription()
    home_page.fill_subscribe_email(user["email"])
    home_page.is_visible_succesfull_subscribe_message()
