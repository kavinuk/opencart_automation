from playwright.sync_api import Page,sync_playwright
class HomePage:

    def __init__(self,page):
        #pages initalisation
        self.page = page
        #locators
        self.my_accounts_link = page.locator('span:has-text("My Account")')
        self.register_link = page.locator('a:has-text("Register")')
        self.login_link = page.locator('a:has-text("Login")')
        self.search_box = page.locator("input[placeholder='Search']")
        self.search_button = page.locator('#search button[type="button"]')

    def get_home_page_title(self):
        title = self.page.title()
        return title
    def click_my_account(self):
        try:
            self.my_accounts_link.click()
        except Exception as e:
            print(f"Exception while clicking 'my account' : {e}")
            raise
    def click_register(self):
        try:
            self.register_link.click()
        except Exception as e:
            print(f"Exception while clicking 'register' : {e}")
            raise
    def click_login(self):
        try:
            self.login_link.click()
        except Exception as e:
            print(f"Exception while clicking 'login' : {e}")
            raise

    def enter_product_name(self,product_name:str):
        try:
            self.search_box.fill(product_name)
        except Exception as e:
            print(f"Exception while entering product name '{product_name}' : {e}")
            raise
    def click_search(self):
        try:
            self.search_button.click()
        except Exception as e:
            print(f"Exception while clicking 'search' button : {e}")
            raise
