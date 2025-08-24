import pytest
import allure


def test_add_review_on_product(home_page,products_page, modal_page,view_cart_page,):
    home_page.navigate()
    home_page.recommended_items.scroll_into_view_if_needed()
    home_page.is_visible_recommended_items()
    products_page.add_product_to_cart_by_id_on_hover(5)
    modal_page.click_view_cart()
    view_cart_page.is_product_visible_in_cart(5)
