import unittest
from selenium import webdriver
from Pages.Homepage import Homepage
from Pages.ResultPage import ResultPage
from Pages.ProductPage import ProductPage
from Pages.LoginPage import Login
from Pages.FavoritePage import FavoritePage

# using python unittest
# Geckodriver copied to ExternalLib/Scripts/Geckodriver.exe
# You can change it with your favorite driver.


class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    ## Open N11.com
    def test001_OpenPage(self):
        driver = self.driver
        Home = Homepage(driver)
        Home.getHomepage()
        assert "n11" in driver.title

    ## Click to Sign In
    def test002_clickLogin(self):
        driver = self.driver
        signIn = Homepage(driver)
        signIn.clickSignIn()
        assert "giris-yap" in driver.current_url

    ## Login Processes
    def test003_Login(self):
        driver = self.driver
        login  = Login(driver)
        login.userLogin()
        self.assertEqual("https://www.n11.com/",driver.current_url)

    ## Search product
    def test004_Search(self):
        driver = self.driver
        search = Homepage(driver)
        search.searchProd()
        assert "samsung" in driver.current_url

    ## Go to Second page in results.
    def test005_secondPage(self):
        driver = self.driver
        page2 = ResultPage(driver)
        page2.clickPage2()
        self.assertIn("pg=2",driver.current_url)

    ## Choose thirth product in results.
    def test006_thirthProduct(self):
        driver = self.driver
        PROD3 = ResultPage(driver)
        PROD3.clickProduct()

    ## Add your favorites.
    def test007_Favorite(self):
        driver = self.driver
        favorite = ProductPage(driver)
        favorite.addFavorite()

    ## Go to your favorites Menu -> Wishlist.
    def test008_GoToWishlist(self):
        driver = self.driver
        wishlist = Homepage(driver)
        wishlist.clickWishlist()

    ## Choose Favorites List in your All lists.
    def test009_goToFavorites(self):
        driver = self.driver
        favorites = FavoritePage(driver)
        favorites.clickFavoritePage()
        favorites.checkFavorites()

    ## Delete product from your favorite list.
    def test010_deleteItem(self):
        driver = self.driver
        delItem = FavoritePage(driver)
        delItem.deleteItem()

    # if __name__ == '__main__':
    #     unittest.main()