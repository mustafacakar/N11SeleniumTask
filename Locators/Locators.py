from selenium.webdriver.common.by import By

class Locators(object):

    ## Homepage Locators
    SIGNIN_BUTTON = (By.CLASS_NAME , "btnSignIn")
    SEARCH_BAR    = (By.ID, "searchData")
    SEARCH_BUTTON = (By.CLASS_NAME,"searchBtn")
    MENU          = (By.CLASS_NAME , "myAccount")
    WISHLIST      = (By.LINK_TEXT , "Favorilerim / Listelerim")
    RESULTTEXT    = (By.CLASS_NAME , "resultText")

    ##LoginPage Locators
    EMAIL         = (By.ID, "email")
    PASSWORD      = (By.ID, "password")
    LOGINBUTTON   = (By.ID, "loginButton")

    ## ResultPage Locators
    PAGE2BUTTON = (By.CSS_SELECTOR, ".pagination > a:nth-child(2)")
    PRODUCT3    = (By.XPATH,"/html/body/div[1]/div[3]/div/div/div[2]/section[1]/div[2]/ul/li[3]/div/div[1]/a/h3")

    ## ProductPage

    FAVORITE_BUTTON = (By.XPATH, '//*[@id="getWishList"]')
    FAVORITE_LIST   = (By.XPATH, "/html/body/div[1]/div[3]/div/div[3]/div[1]/div[1]/div[2]/div[5]/div[2]/div[3]/div/div[2]/div[1]")
    CONFIRM_BUTTON  = (By.XPATH,"//span[@class='btn btnBlack confirm']")
    PRODUCTTITLE    = (By.CLASS_NAME , "proName")

    ## FavoritesPage

    GOFAVORITES     = (By.XPATH , "/html/body/div[1]/div[3]/div/div[2]/div[3]/ul/li[1]/div/a")
    DELETEBUTTON    = (By.XPATH , "/html/body/div[1]/div[3]/div/div[2]/div[3]/div[1]/div[2]/ul/li[1]/div/div[3]/span")
    FAVSGROUP    = (By.XPATH , "/html/body/div[1]/div[3]/div/div[2]/div[3]/div[1]")
