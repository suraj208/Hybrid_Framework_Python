from selenium.webdriver.common.by import By


class AccountPage:
    def __init__(self,driver):
        self.driver = driver

    my_account_by_xpath = (By.XPATH,'//h2[text()="My Account"]')
    account_create_success_messege_by_xpath = (By.XPATH,'//h1[text()="Your Account Has Been Created!"]')

    def getmyAccountText(self):
        return self.driver.find_element(*AccountPage.my_account_by_xpath).text

    def get_ac_Confirm_messege(self):
        return self.driver.find_element(*AccountPage.account_create_success_messege_by_xpath).text