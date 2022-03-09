import random
import string
import time

import pytest

from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()
    def test_addCustomer(self, setup):
        self.driver = setup
        self.logger.info("***********entering_url**************")
        self.lp = LoginPage(self.driver)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*************Login successfull************")
        self.logger.info("***********Starting_Test_003_AddCustomer**************")
        self.addcust = AddCustomer(self.driver)

        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()
        self.addcust.clickOnAddNew()
        self.addcust.clickOnItalianText()
        time.sleep(3)
        self.logger.info("*********Providing customer info ******")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstname("suma")
        self.addcust.setLastname("Rampur")
        self.addcust.setCompanyName("google")
        self.addcust.setDob("1/08/1989")
        self.addcust.setGender("Female")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setMangerOfVendor("Vendor 2")
        self.addcust.setAdminContent("This is for testing.....")
        self.addcust.clickOnSave()
        self.logger.info("***************saving customer info***************")
        self.logger.info("*************Add customer validation started********")

        self.message = self.driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissable']").text
        print(self.message)
        if "The new customer has been added successfully." in self.message:
            assert True
            self.logger.info("*******Customer Added successfully**********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")
            self.logger.error("********Add customer test is failed***************")
            assert False

        self.driver.close()
        self.logger.info("*********Ending Add Customer test************")

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))