import pytest
import allure


def test_verify_search_product( home_page, products_page):
    home_page.navigate()
    home_page.verify_home_page_is_visible()
    home_page.click_products_button()
    products_page.is_visible_title_all_products()
    products_page.fill_search_product("Green Side Placket Detail T-Shirt")
    products_page.click_search_button()
    products_page.is_visible_title_searched_products()
    products_page.click_view_product_for_searched_item()
