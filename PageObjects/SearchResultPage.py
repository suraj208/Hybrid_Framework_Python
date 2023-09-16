from selenium.webdriver.common.by import By


class SearchResultPage1:
    def __init__(self, driver):
        self.driver = driver

    hp_search_by_xpath =(By.XPATH,'//a[text()="HP LP3065"]')
    search_invalid_product_by_xpath = (By.XPATH,'//input[@id="button-search"]/following::p[1]')



    def get_hp_SearchResult(self):
        return self.driver.find_element(*SearchResultPage1.hp_search_by_xpath)

    def get_warning_messege_for_invalid_product(self):
        return self.driver.find_element(*SearchResultPage1.search_invalid_product_by_xpath)