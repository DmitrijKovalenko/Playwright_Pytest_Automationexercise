import pytest
import allure


def test_verify_product_quantatity_in_cart(
    page, home_page, products_page, product_details_page,view_cart_page,modal_page):
    home_page.navigate()
    home_page.verify_home_page_is_visible()
    products_page.click_view_product_by_id(15)
    page.wait_for_timeout(2000)
    assert product_details_page.is_product_detail_visible("Availability")
    assert product_details_page.is_product_detail_visible("Condition")
    assert product_details_page.is_product_detail_visible("Brand")
    product_details_page.set_quantity(4)
    product_details_page.click_add_to_cart()
    modal_page.click_view_cart()
    quantity_in_cart =view_cart_page.get_product_quantity(15).inner_text()
    assert quantity_in_cart == "4"
