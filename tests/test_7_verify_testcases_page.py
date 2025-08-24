import pytest
import allure


def test_verify_testcases_page( home_page, test_cases_page):
    home_page.navigate()
    home_page.verify_home_page_is_visible()
    home_page.click_test_cases_button()
    test_cases_page.verify_on_test_page()
    home_page.click_products_button()
