from selenium import webdriver
import time

from selenium.webdriver.support.select import Select


class AddCustomer:
    lnkCustomers_Menu_xpath = "//a[@href='#']/p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href = '/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"
    italian_customerinfo_xpath = "//div[@class='card-title']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_xpath = "//input[@id='Gender_Male']"
    rdFeMaleGender_xpath = "//input[@id='Gender_Female']"

    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"

    txtCustomerRoles_xpath = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    defaultRoleregister_xpath = "//span[@title='delete']"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"

    drpmgrOfVendor_xpath = "//select[@id='VendorId']"
    txt_AdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_Menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def clickOnItalianText(self):
        self.driver.find_element_by_xpath(self.italian_customerinfo_xpath)

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).clear()
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).clear()
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)

    def setFirstname(self, firstname):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).clear()
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(firstname)

    def setLastname(self, lastname):
        self.driver.find_element_by_xpath(self.txtLastName_xpath).clear()
        self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(lastname)

    def setCompanyName(self, compname):
        self.driver.find_element_by_xpath(self.txtCompanyName_xpath).clear()
        self.driver.find_element_by_xpath(self.txtCompanyName_xpath).send_keys(compname)

    def setDob(self, dob):
        self.driver.find_element_by_xpath(self.txtDob_xpath).send_keys(dob)

    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element_by_xpath(self.rdMaleGender_xpath).click()
        elif gender == "Female":
            self.driver.find_element_by_xpath(self.rdFeMaleGender_xpath).click()
        else:
            self.driver.find_element_by_xpath(self.rdMaleGender_xpath).click()

    def setCustomerRoles(self, role):
        self.driver.find_element_by_xpath(self.txtCustomerRoles_xpath).click()
        time.sleep(5)
        if role == "Registered":
            self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == "Administrators":
            self.listitem = self.driver.find_element_by_xpath(self.lstitemAdministrators_xpath)
        elif role == "Vendors":
            self.listitem = self.driver.find_element_by_xpath(self.lstitemVendors_xpath)
        elif role == "Guests":
            time.sleep(3)
            self.driver.find_element_by_xpath(self.defaultRoleregister_xpath).click()
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
            time.sleep(3)

        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setMangerOfVendor(self, value):
        drp = Select(self.driver.find_element_by_xpath(self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setAdminContent(self, content):
        self.driver.find_element_by_xpath(self.txt_AdminContent_xpath).clear()
        self.driver.find_element_by_xpath(self.txt_AdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()
