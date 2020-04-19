from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from Locators.Locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Homepage():

    #Constucter
    def __init__(self,driver):
        self.driver = driver

        self.signInButton   = Locators.SIGNIN_BUTTON
        self.searchBar      = Locators.SEARCH_BAR
        self.searchButton   = Locators.SEARCH_BUTTON
        self.MENU           = Locators.MENU
        self.WISHLIST       = Locators.WISHLIST
        self.RESULTTEXT     = Locators.RESULTTEXT



    def getHomepage(self):
        driver = self.driver
        driver.get("https://n11.com")

    def clickSignIn(self):
        driver = self.driver
        driver.find_element(*self.signInButton).click()

    def searchProd(self):
        driver = self.driver
        driver.find_element(*self.searchBar).send_keys("samsung")
        driver.find_element(*self.searchButton).click()
        try:
            driver.find_element(*self.RESULTTEXT)
            print("Arama sonuçları listelendi.")
        except NoSuchElementException:
            print("Sonuç bulunamadı")
            return False


    def clickWishlist(self):
        driver = self.driver

        menu_elem  = driver.find_element(*self.MENU)
        driver.execute_script("arguments[0].scrollIntoView();", menu_elem)
        action_hover  = ActionChains(driver).move_to_element(menu_elem)
        action_hover.perform()
        #click wishlist
        # WebDriverWait(driver, 20).until(EC.element_to_be_clickable(*self.WISHLIST))
        driver.find_element(*self.WISHLIST).click()


