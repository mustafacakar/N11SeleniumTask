from Locators.Locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ResultPage():


    def __init__(self,driver):
        self.driver = driver

        self.BUTTONPAGE2  = Locators.PAGE2BUTTON
        self.PRODUCT3     = Locators.PRODUCT3


    def clickPage2(self):
        driver = self.driver
        WebDriverWait(driver,20).until(EC.element_to_be_clickable(Locators.PAGE2BUTTON))
        time.sleep(5)
        driver.find_element(*self.BUTTONPAGE2).click()

    def clickProduct(self):
        driver = self.driver
        driver.find_element(*self.PRODUCT3).click()
