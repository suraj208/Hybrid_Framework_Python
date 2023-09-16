import pytest

from Utilities.Baseclass import BaseClass
from PageObjects.LogiPage import LoginPage
from PageObjects.FirstPage import FirstPage1
from PageObjects.AccountPage import AccountPage
from Testdata.LoginPageData import LoginPageData


class TestLoginPage(BaseClass):
    def test_Login_Page_with_Correct_credentials(self,getData):
        log = self.getLogger()
        firstpage = FirstPage1(self.driver)
        firstpage.getmyaccout().click()
        firstpage.getlogin().click()
        loginpage = LoginPage(self.driver)
        log.info("usisng the email as "+getData["email"])
        loginpage.getEmail().send_keys(getData["email"])
        log.info("using password as "+getData["password"])
        loginpage.getPassword().send_keys(getData["password"])
        loginpage.getLoginButton().click()
        myaccounttext = "My Account"
        account_page = AccountPage(self.driver)
        assert account_page.getmyAccountText() == myaccounttext


    @pytest.fixture(params=LoginPageData.getLoginData("testcase1"))
    def getData(self,request):
        return request.param

