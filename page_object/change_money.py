import allure

from page_object.basepage import BasePage
from selenium.webdriver.common.by import By
import time


class ChangeMoney(BasePage):
    toggle = By.CLASS_NAME, 'dropdown-toggle'
    selector = By.CSS_SELECTOR, '#form-currency > div > ul > li:nth-child(2) > a'

    @allure.step('Смена денег на £')
    def change_to_euro(self, toggle_locator, selector_locator):
        self.logger.info(f'Check toggle to change {toggle_locator}')
        element1 = self.browser.find_element(*self.toggle).click()
        self.logger.info(f'Change to selector {selector_locator}')
        element = self.browser.find_element(*self.selector).click()
        return element, element1
