from playwright.sync_api import Playwright, Page
from pages.product_page import ProductPage


class SearchResultsPage:
    def __init__(self,page: Page):
        self.page = page

        #locators
        self.search_page_header = page.locator('#content h1',has_text="Search -")
        #link of products
        self.search_products = page.locator('h4 a')


    def get_search_page_header(self):
        try:
            return self.search_page_header
        except Exception as e:
            print(f"exception while getting search page header :{e}")
            return None

    def is_products_present(self,product_name:str):
        try:
            count = self.search_products.count()
            for i in range(count):
                product = self.search_products.nth(i)
                title = self.search_products.text_content()
                if title and title.strip() == product_name:
                    return product
        except Exception as e:
            print(f"exception while checking product presence :{e}")
            return None

    def select_product(self,product_name:str):
        try:
            count = self.search_products.count()
            for i in range(count):
                product = self.search_products.nth(i)
                title = self.search_products.text_content()
                if title and title.strip() == product_name:
                    product.click()
                    return ProductPage(self.page)

            print(f"product not present :{product_name}")
        except Exception as e:
            print(f"exception while selecting product :{e}")
            return None

    def get_product_count(self):
        try:
            return self.search_products
        except Exception as e:
            print(f"error while getting product count :{e}")
            return None









