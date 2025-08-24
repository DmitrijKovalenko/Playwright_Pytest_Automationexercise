import pytest
import allure


def test_remov_products_from_cart(home_page):
    home_page.navigate()
    home_page.is_visible_left_sidebar()
    home_page.click_woman_catagory()
    home_page.click_dress()
    home_page.is_visible_title_woman_products()
    home_page.click_men_catagory()
    home_page.click_t_shirt()
    home_page.is_visible_title_men_products()
