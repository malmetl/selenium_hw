from page_object.basepage import BasePage
from selenium.webdriver.common.by import By


class WishList(BasePage):
    def add_to_wish_list(self):
        self.browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
