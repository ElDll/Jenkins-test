from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM_EMAIL = (By.NAME, "registration-email")
    REGISTER_FORM_PASSWORD = (By.NAME, "registration-password1")
    REGISTER_FORM_PASSWORD_REPEAT = (By.NAME, "registration-password2")
    REFISTER_FORM_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators():
    ADD_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")

    PRODUCT_NAME = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    MESSAGE_NAME = (By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-success  fade in']"
                              "/div[@class='alertinner ']/strong")

    PRODUCT_PRICE = (By.XPATH, "//div[@class='col-sm-6 product_main']/p[@class='price_color']")
    MESSAGE_PRICE = (By.XPATH, "//div[@id='messages']/div[@class='alert alert-safe alert-noicon alert-info  fade in']"
                               "/div[@class='alertinner ']/p/strong")

    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages']/div[@class='alert alert-safe alert-noicon alert-success  fade in']")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.XPATH, "//span[@class='btn-group']/a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_ELEMENT = (By.XPATH, "//div[@class = 'basket-items']/")
    EMPTY_MESSAGE = (By.XPATH, "//div[@id='content_inner']/p")