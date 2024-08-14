from page_object.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class selector(BasePage):
    def selector_to_price(self):
        self.browser.find_element(By.ID, "button-list").click()
        self.browser.find_element(By.CSS_SELECTOR, "#input-sort > option:nth-child(5)").click()
