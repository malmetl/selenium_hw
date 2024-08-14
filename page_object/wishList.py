from page_object.basepage import BasePage
from selenium.webdriver.common.by import By
import allure


class WishList(BasePage):
    add_wish_list = By.CSS_SELECTOR, "button[type='submit']"

    @allure.step("Добавление в вишлист через кнопку")
    def add_to_wish_list(self, locator_wishlist):
        self.logger.info(f'Go to wishlish {locator_wishlist}')
        self.browser.find_element(*self.add_wish_list).click()
