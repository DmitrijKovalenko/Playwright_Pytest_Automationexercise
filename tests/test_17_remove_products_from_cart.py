import pytest
import allure


def test_remov_products_from_cart(home_page, products_page, view_cart_page, modal_page):
    home_page.navigate()
    home_page.verify_home_page_is_visible()
    home_page.click_products_button()
    products_page.add_product_to_cart_by_id_on_hover(1)
    modal_page.click_continue_shopping()
    products_page.add_product_to_cart_by_id_on_hover(2)
    modal_page.click_view_cart()
    view_cart_page.is_cart_page_displayed()
    view_cart_page.delete_product_by_id(1)
    assert view_cart_page.is_product_not_visible_in_cart(1)
    view_cart_page.delete_product_by_id(2)
    assert view_cart_page.is_product_not_visible_in_cart(2)
    view_cart_page.is_visible_title_empty_cart()
