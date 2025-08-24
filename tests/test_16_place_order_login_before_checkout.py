import pytest
import allure


def test_place_order_login_before_checkout(
    home_page,
    products_page,
    view_cart_page,
    modal_page,
    logged_in_user,
    checkout_page,
    payment_page,
    card_data,
    account_deleted_page,
):

    user = logged_in_user
    card = card_data
    products_page.add_product_to_cart_by_id_on_hover(1)
    modal_page.click_view_cart()
    assert view_cart_page.is_product_visible_in_cart(1)
    view_cart_page.click_proceed_checkout()
    delivery_address_parts = [
        f"Mr. {user['first_name']} {user['last_name']}",
        user["company"],
        user["address"],
        user["address2"],
        f"{user['city']} {user['state']} {user['zipcode']}",
        user["country"],
    ]

    billing_address_parts = [
        f"Mr. {user['first_name']} {user['last_name']}",
        user["company"],
        user["address"],
        user["address2"],
        f"{user['city']} {user['state']} {user['zipcode']}",
        user["country"],
    ]

    checkout_page.verify_address_contains_all_parts(
        checkout_page.get_delivery_address_details(), delivery_address_parts
    )
    checkout_page.verify_address_contains_all_parts(
        checkout_page.get_billing_address_details(), billing_address_parts
    )

    checkout_page.enter_comment("Automated order placed after logging in.")
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
