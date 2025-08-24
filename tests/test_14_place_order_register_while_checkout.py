import pytest
import allure


def test_place_order_register_while_checkout(
    home_page,
    products_page,
    view_cart_page,
    modal_page,
    login_page,
    signup_page,
    account_created_page,
    checkout_page,
    payment_page,
    card_data,
    account_deleted_page,
    fake_user_data,
):

    fake_user = fake_user_data["valid"]
    card = card_data
    home_page.navigate()
    home_page.verify_home_page_is_visible()
    home_page.click_products_button()
    products_page.add_product_to_cart_by_id_on_hover(1)
    modal_page.click_view_cart()
    assert view_cart_page.is_product_visible_in_cart(1)
    price1 = view_cart_page.get_product_price(1)
    quantity1 = view_cart_page.get_product_quantity(1)
    total_price1 = view_cart_page.get_product_total_price(1)
    assert price1.is_visible()
    assert quantity1.is_visible()
    assert total_price1.is_visible()
    view_cart_page.click_proceed_checkout()
    modal_page.click_register_login_button()
    login_page.is_visible_title_new_user_signup()
    login_page.fill_name(fake_user["name"])
    login_page.fill_signup_email(fake_user["email"])
    login_page.click_signup_button()
    signup_page.is_visible_title_enter_accout_information()
    signup_page.click_gender_male()
    signup_page.fill_password(fake_user["password"])
    signup_page.select_day_1()
    signup_page.select_month_1()
    signup_page.select_year_2001()
    signup_page.click_newsletter()
    signup_page.click_special_offers()
    signup_page.fill_first_name(fake_user["first_name"])
    signup_page.fill_Last_name(fake_user["last_name"])
    signup_page.fill_company(fake_user["company"])
    signup_page.fill_address(fake_user["address"])
    signup_page.fill_address2(fake_user["address2"])
    signup_page.select_country_US()
    signup_page.fill_state(fake_user["state"])
    signup_page.fill_city(fake_user["city"])
    signup_page.fill_zipcode(fake_user["zipcode"])
    signup_page.fill_mobile_number(fake_user["mobile_number"])
    signup_page.click_create_account_button()
    account_created_page.is_visible_title_account_created()
    account_created_page.click_continue_button()
    home_page.is_visible_logged_in_as()
    home_page.click_cart_button()
    view_cart_page.click_proceed_checkout()

    delivery_address_parts = [
        f"Mr. {fake_user['first_name']} {fake_user['last_name']}",
        fake_user["company"],
        fake_user["address"],
        fake_user["address2"],
        f"{fake_user['city']} {fake_user['state']} {fake_user['zipcode']}",
        fake_user["country"],
    ]

    billing_address_parts = [
        f"Mr. {fake_user['first_name']} {fake_user['last_name']}",
        fake_user["company"],
        fake_user["address"],
        fake_user["address2"],
        f"{fake_user['city']} {fake_user['state']} {fake_user['zipcode']}",
        fake_user["country"],
    ]

    checkout_page.verify_address_contains_all_parts(
        checkout_page.get_delivery_address_details(), delivery_address_parts
    )
    checkout_page.verify_address_contains_all_parts(
        checkout_page.get_billing_address_details(), billing_address_parts
    )

    checkout_page.enter_comment("I'm sure the code could be cleaner.")
    checkout_page.click_place_order()
    payment_page.fill_name_on_card(card["name_on_card"])
    payment_page.fill_card_number(card["card_number"])
    payment_page.fill_cvc(card["cvc"])
    payment_page.fill_expiry_month(card["expiry_month"])
    payment_page.fill_expiry_year(card["expiry_year"])
    payment_page.click_pay_and_confirm_button()
    payment_page.is_visible_order_placed_succesfull_message()
    home_page.click_delete_account()
    account_deleted_page.is_visible_title_account_deletedd()
