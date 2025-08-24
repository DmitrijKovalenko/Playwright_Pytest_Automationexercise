import pytest
import allure


def test_verify_scroll_up(page, home_page ):
    home_page.navigate()
    home_page.verify_home_page_is_visible()
    page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
    home_page.is_visible_subscription()
    page.evaluate("window.scrollTo(0, 0)")
    home_page.is_visible_title_full_flaged()
