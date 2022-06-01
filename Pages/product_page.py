from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_item_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def get_item_name(self):
        return self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
    
    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_item_name_in_success_message(self, item_name):
        item_name_in_success_message = self.browser.find_element(*ProductPageLocators.ITEM_NAME_IN_SUCCESS_MESSAGE).text
        assert item_name == item_name_in_success_message, "Item name doesn't match item name in success message"

    def should_be_basket_price_updated(self, product_price):
        basket_total_in_message = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_IN_MESSAGE).text
        assert basket_total_in_message == product_price, "Basket price aren't updated"

        