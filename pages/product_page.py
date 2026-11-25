from playwright.sync_api import expect

from pages.shopping_cart_page import ShoppingCartPage


class ProductPage:
    def __init__(self, page):
        self.page = page
        #locators
        self.txt_quantity = page.locator("#input-quantity")
        self.btn_add_to_cart = page.locator("#button-cart")
        self.conf_msg = page.locator(".alert.alert-success.alert-dismissible")
        self.btn_items = page.locator("#cart")
        self.link_view_cart = page.locator('strong:has-text("View Cart")')


    #quantity
    def set_quantity(self, qty:str):
        try:
            self.txt_quantity.fill("")
            self.txt_quantity.fill(qty)
        except Exception as e:
            print(f"error while setting quantity :{e}")
            raise
    #add to cart
    def add_to_cart(self):
        try:
            self.btn_add_to_cart.click()
        except Exception as e:
            print(f"error while click add to cart button :{e}")
            raise
    def get_confirmation_message(self):
        try:
            return self.conf_msg
        except Exception as e:
            print(f" confirmation message not found :{e}")
            return None

    def click_items_to_navigate_to_cart(self):
        try:
            self.btn_items.click()
        except Exception as e:
            print(f"error while clicking catr items :{e}")
            raise
    def click_view_cart(self):
        try:
            self.link_view_cart.click()
            return ShoppingCartPage(self.page)
        except Exception as e:
            print(f"error while click view cart button :{e}")
            raise
    #combined
    def add_product_to__cart(self,quantity:str):
        try:
            self.set_quantity(quantity)
            self.add_to_cart()
            expect(self.get_confirmation_message()).to_be_visible()
        except Exception as e:
            print(f"error in add_product_to_cart_workflow:{e}")
            raise








