from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def should_be_empty_basket_message(self):
        lang_msg = {
            'en': 'Your basket is empty. Continue shopping',
            'ru': 'Ваша корзина пуста Продолжить покупки'
        }
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), 'In basket page here is no empty message'
        msg = self.browser.find_element(*BasketPageLocators.EMPTY_MESSAGE)
        lang = self.browser.execute_script(
            "return window.navigator.userLanguage || window.navigator.language")
        assert lang_msg[lang] == msg.text, f'Text in basket empty message field is incorrect "{msg.text}"'

    def should_not_be_basket_summary(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY), \
            'Basket should be empty'
