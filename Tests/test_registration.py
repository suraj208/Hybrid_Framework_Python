from Utilities.Baseclass import BaseClass
from PageObjects.FirstPage import FirstPage1
from PageObjects.RegisterPage import RegisterPage
from PageObjects.AccountPage import AccountPage
class TestRegistrationPage(BaseClass):
    def test_registrationPage_with_all_fields(self):
        firstname = FirstPage1(self.driver)
        firstname.getmyaccout().click()
        firstname.getregister().click()
        registerpage = RegisterPage(self.driver)
        registerpage.getFirstname().send_keys("ayodya")
        registerpage.getLastname().send_keys("Ramji")
        registerpage.getemail().send_keys("ramji1234562@gmail.com")
        registerpage.getTelephone().send_keys("80087565835")
        registerpage.getPassword().send_keys("suraj123")
        registerpage.getConfirm_Password().send_keys("suraj123")
        registerpage.getcheckbox().click()
        registerpage.getContinueButton().click()
        success_massege ="Your Account Has Been Created!"
        accountpage = AccountPage(self.driver)
        assert  accountpage.get_ac_Confirm_messege()==success_massege


    #def test_registrationpage_with_keeping_all_fields_empty(self):
