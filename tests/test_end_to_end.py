import pytest
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from pages.my_accounts import MyAccount
from pages.logout_page import LogoutPage
from pages.product_page import ProductPage
from pages.search_results_page import SearchResultsPage
from config import Config
from pages.shopping_cart_page import ShoppingCartPage
from utilities.random_data_util import RandomDataUtil

@pytest.mark.end_to_end
def test_end_to_end_flow(page):
    """
        End-to-End Test Flow:
        1. Register a new user.
        2. Logout.
        3. Login with the registered credentials.
        4. Search and add a product to cart.
        5. Verify cart contents.
        """
    # Step 1: Register a new account and capture the generated email
    registered_email, registered_password = perform_registration(page)
    print("✅ Registration completed successfully!")

    # Step 2: Logout after registration
    perform_logout(page)
    print("✅ Logout completed successfully!")

    # Step 3: Login with registered email
    perform_login(page, registered_email, registered_password)
    print("✅ Login completed successfully!")

    # Step 4: Search product and add to cart
    add_product_to_cart(page)
    print("✅ Product added to cart successfully!")

    # Step 5: Verify cart details
    verify_shopping_cart(page)
    print("✅ Shopping cart verification completed!")

# -------------------------------------------------------------
# Helper Function: Register a New User
# -------------------------------------------------------------
def perform_registration(page):
    home_page = HomePage(page)
    registration_page = RegistrationPage(page)

    # --- Step 2: Navigate to Registration Page ---
    home_page.click_my_account()
    home_page.click_register()
    # --- Step 3: Generate Random Test Data ---
    # Using RandomDataUtil to generate random user details
    random_data = RandomDataUtil()
    first_name = random_data.get_first_name()
    last_name = random_data.get_last_name()
    email = random_data.get_email()
    phone_number = random_data.get_phone_number()
    password = random_data.get_password()

    # --- Step 4: Fill Registration Form ---
    registration_page.set_first_name(first_name)
    registration_page.set_last_name(last_name)
    registration_page.set_email(email)
    registration_page.set_telephone(phone_number)
    registration_page.set_password(password)
    registration_page.set_confirm_password(password)
    # --- Step 5: Accept Privacy Policy and Submit ---
    registration_page.set_privacy_policy()
    registration_page.click_continue()

    # --- Step 6: Verify Account Creation Confirmation ---
    confirm_msg = registration_page.get_confirm_msg()
    expect(confirm_msg).to_contain_text("Your Account Has Been Created!")
    page.wait_for_timeout(5000)
    return email, password

def perform_logout(page):
    logout_page = LogoutPage(page)
    my_account = MyAccount(page)
    my_account.click_logout()

    expect(logout_page.get_continue_button()).to_be_visible(timeout=3000)
    logout_page.click_continue()

    expect(page).to_have_title("Your Store")
    page.wait_for_timeout(timeout=3000)

def perform_login(page,registered_email,registered_password):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    my_account = MyAccount(page)

    home_page.click_my_account()
    home_page.click_login()

    login_page.login(registered_email,registered_password)

    expect(my_account.account_page_heading()).to_be_visible(timeout=3000)

def add_product_to_cart(page):
    product_name = Config.product_name
    quantity = Config.product_quantity
    # --- Page Object Initialization ---
    home_page = HomePage(page)
    search_page = SearchResultsPage(page)
    # --- Step 1: Search for a Product ---
    home_page.enter_product_name(product_name)
    page.wait_for_timeout(timeout=3000)
    home_page.click_search()
    page.wait_for_timeout(4000)
    expect(search_page.get_search_page_header()).to_be_visible(timeout=3000)
    expect(search_page.is_products_present(product_name)).to_be_visible(timeout=3000)
    # --- Step 2: Select the Product from Search Results ---
    product_page = search_page.select_product(product_name)
    # --- Step 3: Set Quantity and Add to Cart ---
    product_page.set_quantity(quantity)
    product_page.add_to_cart()
    page.wait_for_timeout(4000)
    # --- Step 4: Verify Confirmation Message ---
    # Ensure the success message appears within 3 seconds after adding the product
    expect(product_page.get_confirmation_message()).to_be_visible(timeout=4000)



def verify_shopping_cart(page):
    product_page = ProductPage(page)
    product_page.click_items_to_navigate_to_cart()

    shopping_cart_page = product_page.click_view_cart()
    config = Config()
    page.wait_for_timeout(4000)

    print("🛒 Navigated to Shopping Cart Page!")
    expect(shopping_cart_page.get_total_price()).to_contain_text(config.total_price)

















