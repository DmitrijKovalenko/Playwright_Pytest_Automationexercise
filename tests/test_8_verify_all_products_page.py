import pytest
import allure


def test_verify_all_products(page, home_page, products_page, product_details_page):
    home_page.navigate()
    home_page.verify_home_page_is_visible()
    home_page.click_products_button()
    products_page.is_visible_title_all_products()
    products_page.is_visible_list_products()
    products_page.click_view_product_by_id(1)
    product_details_page.verify_on_product_details_page()
    product_details_page.is_visible_product_name()
    product_details_page.is_visible_category()
    product_details_page.is_visible_price()
    product_details_page.is_visible_availability()
    product_details_page.is_visible_condition()
    product_details_page.is_visible_brand()
