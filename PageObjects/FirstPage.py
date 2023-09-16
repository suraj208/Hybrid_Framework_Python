from selenium.webdriver.common.by import By
class FirstPage1:
    def __init__(self , driver):
        self.driver = driver
    my_account_link_xpath = (By.XPATH,'//span[normalize-space()="My Account"]')
    register_by_xpath = (By.XPATH,'//a[(text()="Register")]')
    login_link_by_xpath = (By.XPATH,'//a[text()="Login"]')
    search_field_by_name = (By.NAME,'search')
    serach_button_by_xpath = (By.XPATH,'//input[@name="search"]/following::button[1]')


    def getmyaccout(self):
        return self.driver.find_element(*FirstPage1.my_account_link_xpath)

    def getregister(self):
        return self.driver.find_element(*FirstPage1.register_by_xpath)

    def getlogin(self):
        return self.driver.find_element(*FirstPage1.login_link_by_xpath)

    def getSearchfield(self):
        self.driver.find_element(*FirstPage1.search_field_by_name).clear()
        return self.driver.find_element(*FirstPage1.search_field_by_name)

    def getSearchButton(self):
        return self.driver.find_element(*FirstPage1.serach_button_by_xpath).click()