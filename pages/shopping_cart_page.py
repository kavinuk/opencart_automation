from playwright.sync_api import Page,sync_playwright

from pages.check_out_page import CheckOutPage


class ShoppingCartPage:
    def __init__(self, page):
        self.page = page
        #locators
        self.lbl_total_price = page.locator('//*[@id="content"]//div//table//strong[text()="Total:"]//following::td')
        self.btn_checkout = page.locator("a[class='btn btn-primary']")

    def get_total_price(self):
        try:
            return self.lbl_total_price
        except Exception as e:
            print(f"Unable to retrieve total price: {e}")
            return None


    def click_on_checkout(self):
        try:
            self.btn_checkout.click()
            return CheckOutPage(self.page)
        except Exception as e:
            print(f"Error in clicking  on checkout button: {e}")

    def is_page_loaded(self):
        try:
            return self.btn_checkout
        except Exception as e:
            print(f"Error in verifying shopping cart page load : {e}")
            return None
