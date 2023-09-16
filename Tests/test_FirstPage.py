import time

import pytest

from Utilities.Baseclass import  BaseClass
from PageObjects.FirstPage import FirstPage1
from PageObjects.SearchResultPage import SearchResultPage1
class Test_FirstPage(BaseClass):
    def test_firsttestcase(self):
        firstpage = FirstPage1(self.driver)
        firstpage.getmyaccout().click()
        firstpage.getregister().click()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_search_for_valid_product(self):
        #self.getlogger("seraching valid product  hp....")
        firstpage = FirstPage1(self.driver)
        firstpage.getSearchfield().send_keys("hp")
        firstpage.getSearchButton()
        time.sleep(3)
        hp_product = "HP LP3065"
        searchresult = SearchResultPage1(self.driver)

        assert searchresult.get_hp_SearchResult().text == hp_product


    def test_search_for_invalid_product(self):
        #self.getlogger("seraching for invalid product  car...")
        firstpage = FirstPage1(self.driver)
        firstpage.getSearchfield().send_keys("car")
        firstpage.getSearchButton()
        warning_messege ="There is no product that matches the search criteria."
        searchresult = SearchResultPage1(self.driver)
        assert searchresult.get_warning_messege_for_invalid_product().text == warning_messege

