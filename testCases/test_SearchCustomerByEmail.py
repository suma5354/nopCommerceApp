import time
from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import searchCustomer


class Test_SearchCustomerByEmail_0004:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_searchCustomerByEmail(self, setup):
        self.logger.info("********Test_SearchCustomerByEmail_0004*********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("*******Login successful*********")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.logger.info("*********starting search customer*************")
        self.searchCust = searchCustomer(self.driver)
        self.searchCust.setEmail("victoria_victoria@nopCommerce.com")
        self.searchCust.clickOnSearch()
        time.sleep(5)
        status = self.searchCust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True == status
        self.driver.close()
        self.logger.info("*********Search customer by Email finished************")







