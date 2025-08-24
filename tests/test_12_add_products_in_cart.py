import pytest
import allure


def test_add_products_in_cart( page , home_page, products_page, view_cart_page,modal_page):
    home_page.navigate()
    home_page.verify_home_page_is_visible()
    home_page.click_products_button()
    products_page.add_product_to_cart_by_id_on_hover(1)
    modal_page.click_continue_shopping()
    products_page.add_product_to_cart_by_id_on_hover(2)
    modal_page.click_view_cart()
    assert view_cart_page.is_product_visible_in_cart(1)
    assert view_cart_page.is_product_visible_in_cart(2)
    price1 = view_cart_page.get_product_price(1)
    quantity1 = view_cart_page.get_product_quantity(1)
    total_price1 = view_cart_page.get_product_total_price(1)
    assert price1.is_visible()
    assert quantity1.is_visible()
    assert total_price1.is_visible()
    page.wait_for_timeout(2000)
    price2 = view_cart_page.get_product_price(2)
    quantity2 = view_cart_page.get_product_quantity(2)
    total_price2 = view_cart_page.get_product_total_price(2)
    assert price2.is_visible()
    assert quantity2.is_visible()
    assert total_price2.is_visible()
