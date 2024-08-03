from page_object.basepage import BasePage
from selenium.webdriver.common.by import By

class Cart(BasePage):
    def add_to_cart(self,base_url):
        self.browser.find_element(By.ID, "button-cart").click()

    def check_cart(self):
        self.browser.find_element(By.CSS_SELECTOR, "#header-cart > div > button").click()