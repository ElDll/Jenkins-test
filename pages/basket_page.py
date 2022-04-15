from .locators import BasketPageLocators
from .base_page import BasePage

class BasketPage(BasePage):

    def we_dont_have_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ELEMENT), "We have element"

    def should_we_have_empty_basket_message(self):
        assert self.browser.find_element(*BasketPageLocators.EMPTY_MESSAGE).text == \
               "Your basket is empty. Continue shopping", "We don't have empty message"