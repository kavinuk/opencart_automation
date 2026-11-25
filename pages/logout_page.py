from playwright.sync_api import Page,sync_playwright
from pages.home_page import HomePage

class LogoutPage:
    def __init__(self,page):
        self.page = page

        #locators
        self.btn_continue = page.locator('.btn.btn-primary')
        #action
    def click_continue(self):
        try:
            self.btn_continue.click()
        except Exception as e:
            print(f"Exception while clicking continue button: {e}")

    def get_continue_button(self):
        try:
            return self.btn_continue
        except Exception as e:
            print(f"Exception while fetching continue button locator : {e}")
            return None