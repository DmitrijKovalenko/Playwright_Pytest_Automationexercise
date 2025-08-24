import pytest
import allure


def test_add_review_on_product(fake_user_data,home_page,products_page,product_details_page):
    fake_user = fake_user_data["valid"]
    home_page.navigate()
    home_page.verify_home_page_is_visible()
    home_page.click_products_button()
    products_page.is_visible_title_all_products()
    products_page.click_view_product_by_id(1)
    product_details_page.is_visible_review()
    product_details_page.fill_name(fake_user["name"])
    product_details_page.fill_email(fake_user["email"])
    product_details_page.fill_review(fake_user["review"])
    product_details_page.click_submit_review_button()
    product_details_page.is_visible_thanks_submit_message()
