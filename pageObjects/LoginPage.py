from selenium import webdriver
import time


class LoginPage:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[@type='submit']"
    button_logout_link_text = "Logout"

    """ this constructor capture the driver from testcase"""

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.button_logout_link_text).click()
