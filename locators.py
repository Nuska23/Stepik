from selenium.webdriver.common.by import By

class BasketPageLocators():
    EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner p')
    BASKET_SUMMARY = (By.CSS_SELECTOR, '.basket_summary')

class MainPageLocators():
    pass

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REG_EMAIL_FIELD = (By.CSS_SELECTOR, '[name=registration-email]')
    REG_PASSWORD_FIELD1 = (By.CSS_SELECTOR, '[name=registration-password1]')
    REG_PASSWORD_FIELD2 = (By.CSS_SELECTOR, '[name=registration-password2]')
    REG_SUBMIT_BUTTON = (By.CSS_SELECTOR, '[name=registration_submit]')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, '.basket-mini a')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    SUCCESS_PRODUCT_NAME = (By.CSS_SELECTOR, '.alert-success:nth-child(1) strong')
    SUCCESS_PRODUCT_PRICE = (By.CSS_SELECTOR, '.alert-info strong')
