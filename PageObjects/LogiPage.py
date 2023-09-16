from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    email_id_bt_id =(By.ID,'input-email')
    password_by_id =(By.ID,'input-password')
    login_button_by_xpath =(By.XPATH,'//input[@value="Login"]')

    def getEmail(self):
        return self.driver.find_element(*LoginPage.email_id_bt_id)

    def getPassword(self):
        return self.driver.find_element(*LoginPage.password_by_id)

    def getLoginButton(self):
        return self.driver.find_element(*LoginPage.login_button_by_xpath)

