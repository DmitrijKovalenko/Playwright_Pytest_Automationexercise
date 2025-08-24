import pytest
import allure


def test_search_products_and_verify_cart_after_login(real_user_data,view_cart_page,modal_page,
    home_page,products_page,login_page,):
    user = real_user_data
    home_page.navigate()
    home_page.verify_home_page_is_visible()
    home_page.click_products_button()
    products_page.is_visible_title_all_products()
    products_page.fill_search_product("Green Side Placket Detail T-Shirt")
    products_page.click_search_button()
    products_page.is_visible_title_searched_products()
    products_page.add_product_to_cart_by_id_on_hover(29)
    modal_page.click_view_cart()
    view_cart_page.is_product_visible_in_cart(29)
    home_page.click_login_signup_button()
    login_page.fill_login_email(user["email"])
    login_page.fill_password(user["password"])
    home_page.click_cart_button()
    view_cart_page.is_product_visible_in_cart(29)
