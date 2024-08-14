from page_object.basepage import BasePage
from selenium.webdriver.common.by import By


class ChangeMoney(BasePage):
    def change_to_euro(self):
        self.browser.find_element(By.CLASS_NAME, "dropdown-toggle").click()
        self.browser.find_element(By.CSS_SELECTOR, "#form-currency > div > ul > li:nth-child(2) > a").click()
