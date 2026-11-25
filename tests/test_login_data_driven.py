import time
import pytest
from playwright.sync_api import Playwright,expect
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_accounts import MyAccount
from utilities.data_reder_util import read_csv_date,read_excel_date,read_json_date
#Load/read the data from the test data files
csv_data=read_csv_date("test_data/logindata.csv")
json_data=read_json_date("test_data/logindata.json")
excel_data=read_excel_date("test_data/logindata.xlsx")
@pytest.mark.datadriven
@pytest.mark.parametrize ("testName,email,password,expected",csv_data)
def test_login_data_driven(testName,email,password,expected,page):

    home_page = HomePage(page)
    login_page = LoginPage(page)
    my_account = MyAccount(page)

    home_page.click_my_account()
    home_page.click_login()

    login_page.login(email,password)
    time.sleep(4)
    if expected == "success":
        expect(my_account.account_page_heading()).to_be_visible(timeout=3000)
    else:
        expect(login_page.get_login_error()).to_be_visible(timeout=3000)

