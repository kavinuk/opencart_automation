from playwright.sync_api import Playwright,Page
from pages.logout_page import LogoutPage
class MyAccount:
    def __init__(self,page):
        self.page = page
        #locators
        self.msg_heading = page.locator('h2:has-text("My Account")')
        self.link_logout = page.locator('.list-group-item:has-text("Logout")')

    def account_page_heading(self):

        try:
            return self.msg_heading
        except Exception as e:
            print(f"Error returning My Account page heading: {e}")
        return None

    def click_logout(self):
        try:
            self.link_logout.click()
            return LogoutPage(self.page)
        except Exception as e:
            print(f"Error trying to click Logout button: {e}")
            raise e

    def get_page_title(self):
        try:
            return self.page.title()
        except Exception as e:
            print(f"Error retrieving to get page title: {e}")


