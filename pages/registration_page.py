from playwright.sync_api import Page,sync_playwright

class RegistrationPage:
    def __init__(self,page):
       self.page = page
       #locators
       # input fields
       self.txt_firstname= page.locator("#input-firstname")
       self.txt_lastname= page.locator("#input-lastname")
       self.txt_email= page.locator("#input-email")
       self.txt_telephone= page.locator("#input-telephone")
       self.txt_password= page.locator("#input-password")
       self.txt_confirm_password= page.locator("#input-confirm")
       #check box and buttons
       self.chk_policy = page.locator('input[name="agree"]')
       self.continue_btn = page.locator("input[value='Continue']")

       #success msg after registration
       self.msg_confirmation = page.locator("h1:has-text('Your Account Has Been Created!')")

    #Action methods
    def set_first_name(self,fname:str):
        self.txt_firstname.fill(fname)
    def set_last_name(self,lname:str):
        self.txt_lastname.fill(lname)
    def set_email(self,email:str):
        self.txt_email.fill(email)
    def set_telephone(self,telephone:str):
        self.txt_telephone.fill(telephone)
    def set_password(self,password:str):
        self.txt_password.fill(password)
    def set_confirm_password(self,confirm_password:str):
        self.txt_confirm_password.fill(confirm_password)

    def set_privacy_policy(self):
        self.chk_policy.check()

    def click_continue(self):
        self.continue_btn.click()

    def get_confirm_msg(self):
        return self.msg_confirmation

    #combined
    def complete_registration(self,user_data:dict):
        """
        Example
        user_data = {
        "firstname":"John",
        "lastname":"Doe",
        "email":"johndoe@mail.com",
        "telephone":"48848888",
        "password":"4999",
        "confirm_password":"4999",
        }

        """
        self.txt_firstname.fill(user_data["firstname"])
        self.txt_lastname.fill(user_data["lastname"])
        self.txt_email.fill(user_data["email"])
        self.txt_telephone.fill(user_data["telephone"])
        self.txt_password.fill(user_data["password"])
        self.txt_confirm_password.fill(user_data["confirm_password"])
        self.chk_policy.check()
        self.continue_btn.click()

        #return msg
        return self.msg_confirmation.click()


