from selenium.webdriver import ActionChains

from Locators.Locators import *
import time


class ProductPage():

    def __init__(self,driver):
        self.driver = driver

        self.FAVORITEBUTTON = Locators.FAVORITE_BUTTON
        self.FAVORITE_LIST =  Locators.FAVORITE_LIST
        self.CONFIRM_BUTTON =  Locators.CONFIRM_BUTTON
        self.PRODUCTTITLE =  Locators.PRODUCTTITLE


    def addFavorite(self):
        driver = self.driver
        time.sleep(5)
        driver.find_element(*self.FAVORITEBUTTON).click()
        time.sleep(1)
        driver.find_element(*self.FAVORITE_LIST).click()
        driver.find_element(*self.CONFIRM_BUTTON).click()
        print(driver.find_element(*self.PRODUCTTITLE).text)



