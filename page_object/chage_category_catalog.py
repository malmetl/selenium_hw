import allure
from page_object.basepage import BasePage
from selenium.webdriver.common.by import By


class change_to_category(BasePage):
    @allure.step("Смена каталога на фотоаппараты")
    def change_to_photograph(self):
        self.browser.find_elements(By.CSS_SELECTOR, "#column-left > div:nth-child(1) a")[6].click()


