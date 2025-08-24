import pytest
import allure


def test_verify_address_details_in_checkout(home_page,products_page,view_cart_page,modal_page,
checkout_page,account_deleted_page,logged_in_user
):

    user_data = logged_in_user
    products_page.add_product_to_cart_by_id_on_hover(1)
    modal_page.click_continue_shopping()
    products_page.add_product_to_cart_by_id_on_hover(2)
    modal_page.click_view_cart()
    view_cart_page.click_proceed_checkout()
    delivery_address_parts = [
        f"Mr. {user_data['first_name']} {user_data['last_name']}",
        user_data["company"],
        user_data["address"],
        user_data["address2"],
        f"{user_data['city']} {user_data['state']} {user_data['zipcode']}",
        user_data["country"],
        user_data["mobile_number"],
    ]

    billing_address_parts = [
        f"Mr. {user_data['first_name']} {user_data['last_name']}",
        user_data["company"],
        user_data["address"],
        user_data["address2"],
        f"{user_data['city']} {user_data['state']} {user_data['zipcode']}",
        user_data["country"],
        user_data["mobile_number"],
    ]

    checkout_page.verify_address_contains_all_parts(
        checkout_page.get_delivery_address_details(), delivery_address_parts
    )

    checkout_page.verify_address_contains_all_parts(
        checkout_page.get_billing_address_details(), billing_address_parts
    )
    home_page.click_delete_account()
    account_deleted_page.is_visible_title_account_deletedd()
