from Locators.Locators import *
from selenium.common.exceptions import NoSuchElementException

class FavoritePage():

    def __init__(self,driver):
        self.driver = driver
        self.GOFAVORITES = Locators.GOFAVORITES
        self.DELETEBUTTON = Locators.DELETEBUTTON
        self.CONFIRM_BUTTON = Locators.CONFIRM_BUTTON
        self.FAVSGROUP = Locators.FAVSGROUP





    def clickFavoritePage(self):
        driver = self.driver
        driver.find_element(*self.GOFAVORITES).click()

    def checkFavorites(self):
        driver = self.driver
        try:
            driver.find_element(*self.FAVSGROUP)
            print("Favorilerde Ürün Bulundu.")
        except NoSuchElementException:
            print("Favorilerde ürün bulunamadı.")
            return False

    def deleteItem(self):
        driver = self.driver
        driver.find_element(*self.DELETEBUTTON).click()
        driver.find_element(*self.CONFIRM_BUTTON).click()



