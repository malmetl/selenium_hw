from page_object.basepage import BasePage
from selenium.webdriver.common.by import By
import allure
import logging


class Cart(BasePage):
    button_cart = By.ID, 'button-cart'
    check_cart_product = By.CSS_SELECTOR, '#header-cart > div > button'

    @allure.step("Добавить в корзину")
    def add_to_cart(self, button_cart):
        self.logger.info(f'Go to cart {button_cart}')
        element = self.browser.find_element(*self.button_cart).click()

    @allure.step("Проверить корзину ")
    def check_cart(self,check_locator):
        self.logger.info(f'Go to check cart {check_locator}')
        self.browser.find_element(*self.check_cart_product).click()
