from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)

    def should_be_empty_basket_message(self):
        assert "empty" in self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text