import allure
from selenium.webdriver.support import expected_conditions as EC
from page_object.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class selector(BasePage):
    locator = By.CSS_SELECTOR, "#input-sort > option:nth-child(5)"
    PHOTO_LOCATOR = By.CSS_SELECTOR, "#column-left > div:nth-child(1) a:nth-child(7)"

    @allure.step("Выбор селектора по цене")
    def selector_to_price(self, locator):
        self.logger.info(f'Go to {locator}')
        self.browser.find_element(By.ID, "button-list").click()
        self.logger.info(f'Go to {selector}')
        self.browser.find_element(By.CSS_SELECTOR, "#input-sort > option:nth-child(5)").click()

    @allure.step("Выбор каталога фотоаппаратов")
    def select_photo_catalog(self):
        self.logger.info('Selecting photo catalog')
        element = self.browser.find_element(*self.PHOTO_LOCATOR)
        element.click()
        allure.attach(str(self.PHOTO_LOCATOR), name="Locator", attachment_type=allure.attachment_type.TEXT)
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.PHOTO_LOCATOR))
        screenshot = self.browser.get_screenshot_as_png()
        allure.attach(screenshot, name="Screenshot of the page", attachment_type=allure.attachment_type.PNG)

