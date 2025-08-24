import pytest
import allure


def test_verify_all_products( home_page , brand_page):
    home_page.navigate()
    home_page.verify_home_page_is_visible()
    home_page.click_products_button()
    home_page.is_visible_brands()
    home_page.click_brand_link("Polo")
    brand_page.verify_brand_page_is_displayed("Polo")
    home_page.click_brand_link("H&M")
    brand_page.verify_brand_page_is_displayed("H&M")
