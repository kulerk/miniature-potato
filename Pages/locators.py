from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ITEM_NAME_IN_SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]//strong")
    BASKET_TOTAL_IN_MESSAGE = (By.CSS_SELECTOR, "#messages p strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    ITEM_NAME = (By.CSS_SELECTOR, "div.product_main h1")