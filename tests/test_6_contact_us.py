import pytest
import allure


def test_contact_us_form(page,home_page , contact_us_page, real_user_data):
    page.on("dialog", lambda dialog: dialog.accept())
    user = real_user_data
    home_page.navigate()
    home_page.verify_home_page_is_visible()
    home_page.click_contact_us_button()
    contact_us_page.is_visible_title_get_in_touch()
    contact_us_page.fill_name(user["name"])
    contact_us_page.fill_email(user["email"])
    contact_us_page.fill_subject(user["subject"])
    contact_us_page.fill_message(user["message"])
    file_to_upload = "requirements.txt"
    contact_us_page.upload_file(file_to_upload)
    contact_us_page.click_submit_button()
    contact_us_page.is_visible_succes_message()
    home_page.click_home_button()
    home_page.verify_home_page_is_visible()
