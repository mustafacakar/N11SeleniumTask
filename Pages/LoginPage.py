from Locators.Locators import *
from Locators.User import Users

class Login():


    def __init__(self,driver):
        self.driver = driver

        self.EMAIL       = Locators.EMAIL
        self.PASSWORD    = Locators.PASSWORD
        self.LOGINBUTTON = Locators.LOGINBUTTON



    def userLogin(self):
        driver = self.driver
        driver.find_element(*self.EMAIL).send_keys(Users.USER1_EMAIL)
        driver.find_element(*self.PASSWORD).send_keys(Users.USER1_PASSWORD)
        driver.find_element(*self.LOGINBUTTON).click()





