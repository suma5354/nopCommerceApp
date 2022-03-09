import pytest
from selenium import webdriver
import time
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("*************Test_001_Login*****************")
        self.logger.info("*************Verifying_HomePageTitle*****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*************HomePageTitle test is passed*****************")
        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("*************HomePageTitle test is Failed*****************")
            assert False

    def test_login(self, setup):
        self.logger.info("*************Verifying login Test*****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        time.sleep(5)
        self.lp.setPassword(self.password)
        time.sleep(5)
        # time.sleep(10)
        self.lp.clickLogin()
        act_title = self.driver.title
        print(act_title)
        assert self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("*************login Test is passed*****************")
        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_login.png")
            # .//scrrenshots.png// .--represents current directory
            self.driver.close()
            self.logger.error("*************login Test is Failed*****************")
            assert False
