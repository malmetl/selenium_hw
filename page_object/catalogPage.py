import allure
from selenium.webdriver.common.by import By
from page_object.basepage import BasePage
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ComparePage(BasePage):
    compare_total_id = By.ID, "compare-total"
    compare_message_css = By.CSS_SELECTOR, "#content > p"

    @allure.step("Клик на кнопку 'Compare Total'")
    def check_compare_total(self,compare_total_id, compare_message_css):
        self.logger.info(f"Click to element with locator: {self.compare_total_id}")
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(compare_total_id)).click()
        self.logger.info(f"Waiting element with locator: {self.compare_message_css}")
        message_element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(compare_message_css))
        return message_element.text
