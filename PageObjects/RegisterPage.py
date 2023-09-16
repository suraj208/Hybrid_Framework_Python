from selenium.webdriver.common.by import By
class RegisterPage:
    def __init__(self ,driver):
        self.driver = driver

    first_name_by_id=(By.ID,"input-firstname")
    last_name_by_id = (By.ID,'input-lastname')
    email_by_id = (By.ID,'input-email')
    telephone_by_id = (By.ID,'input-telephone')
    password_by_id = (By.ID,'input-password')
    confirm_password_by_id = (By.ID,'input-confirm')
    checkbox_by_xpath =(By.XPATH,'//input[@name="agree"][1]')
    Continue_by_Xpath =(By.XPATH,'//input[@value="Continue"]')

    def getContinueButton(self):
        return self.driver.find_element(*RegisterPage.Continue_by_Xpath)

    def getFirstname(self):
        return self.driver.find_element(*RegisterPage.first_name_by_id)

    def getLastname(self):
        return self.driver.find_element(*RegisterPage.last_name_by_id)

    def getemail(self):
        return self.driver.find_element(*RegisterPage.email_by_id)

    def getTelephone(self):
        return self.driver.find_element(*RegisterPage.telephone_by_id)

    def getPassword(self):
        return self.driver.find_element(*RegisterPage.password_by_id)

    def getConfirm_Password(self):
        return self.driver.find_element(*RegisterPage.confirm_password_by_id)

    def getcheckbox(self):
        return self.driver.find_element(*RegisterPage.checkbox_by_xpath)