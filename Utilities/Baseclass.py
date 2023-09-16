import inspect
import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configparser import ConfigParser



@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('../Logs/logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger


    def type(self,text):
        self.get_element().clear()
        self.get_element.send_keys(text)

    def click_element(self):
        self.get_element().click()

    def select_option_by_text(self,locator,text):
        drp= Select(locator)
        drp.select_by_visible_text(text)

    def select_option_by_index(self,locator,indexno):
        drp = Select(locator)
        drp.select_by_index(indexno)

    def verify_link_presence(self,text):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(By.LINK_TEXT,text))


    def get_elemet(self,locator):
        element = None
        if locator.__contains("_id"):
            element = self.driver.find_element(By.ID, locator)
        elif locator.__contains("_name"):
            element = self.driver.find_element(By.NAME, locator)
        elif locator.__contains("_link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locator)
        elif locator.__contains("_partial_link_text"):
            element = self.driver.find_element(By.PARTIAL_LINK_TEXT, locator)
        elif locator.__contains("_css_selector"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator)
        elif locator.__contains("_class_name"):
            element = self.driver.find_element(By.CLASS_NAME, locator)
        elif locator.__contains("_xpath"):
            element = self.driver.find_element(By.XPATH, locator)
        return element