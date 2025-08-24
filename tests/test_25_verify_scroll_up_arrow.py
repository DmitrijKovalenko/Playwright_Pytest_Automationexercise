import pytest
import allure


def test_verify_scroll_up(home_page ):
    home_page.navigate()
    home_page.verify_home_page_is_visible()
    home_page.scroll_to_footer()
    home_page.is_visible_subscription()
    home_page.click_scrollup()
    home_page.is_visible_title_full_flaged()
