import pytest
from selenium import webdriver
import time
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from utilities import XLUtils


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    def test_login(self, setup):
        self.logger.info("*************Test_002_DDT_Login*****************")
        self.logger.info("*************Verifying login DDT Test*****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("No of rows in excel...",self.rows)

        lst_status = []
        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, "Sheet1", r, 1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("******Passed*****")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("*********Failed*****")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("*********Failed*****")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("******Passed*****")
                    lst_status.append("Pass")
        print(lst_status)
        if "Fail" not in lst_status:
            self.logger.info("*********DDT test is passed......")
            self.driver.close()
            assert True
        else:
            self.logger.info("*********DDT test is failed......")
            self.driver.close()
            assert False

        self.logger.info("************End of Login DDT Test****************")
        self.logger.info("************Completed  Login DDT Test****************")
