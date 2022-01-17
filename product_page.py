from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def should_not_be_success_product_name(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_PRODUCT_NAME), \
            "Success message is presented, but should not be"

    def should_disappear_success_product_name(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_PRODUCT_NAME), \
            "Success message is presented, but should disappear"

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            'No add to basket button present in product page'

    def should_be_succes_product_price(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_PRODUCT_PRICE), \
            'No product price notification present in product page'

    def should_be_succes_product_name(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_PRODUCT_NAME), \
            'No product name notification present in product page'

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), \
            'No product price present in product page'

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), \
            'No product name present in product page'

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_success_product_price(self):
        return self.browser.find_element(*ProductPageLocators.SUCCESS_PRODUCT_PRICE).text

    def get_success_product_name(self):
        return self.browser.find_element(*ProductPageLocators.SUCCESS_PRODUCT_NAME).text

    def is_success_name_correct(self):
        assert self.get_product_name() == self.get_success_product_name(), \
            'Names of added product and product are unequal'

    def is_success_price_correct(self):
        self.get_product_price() == self.get_success_product_price(), \
        'Prices of added product and product are unequal'
