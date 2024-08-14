import allure
from selenium.webdriver.common.by import By
from page_object.basepage import BasePage


class ProductPage(BasePage):
    header = By.XPATH, '//*[@id="content"]/div[1]/div[2]/h1'
    memory = By.CSS_SELECTOR, '#tab-specification > div > table > thead:first-of-type > tr > td'
    name_memory = By.CSS_SELECTOR, '#tab-specification > div > table > tbody:first-of-type > tr > td:first-of-type'
    image = By.CSS_SELECTOR, '#content > div:first-of-type > div:first-of-type > div > a > img'
    number_product = By.ID, 'input-quantity'

    @allure.step("Проверка названия продукта")
    def check_description_product(self, locator_header):
        self.logger.info(f'Check header {locator_header}')
        self.browser.find_element(*self.header)

    @allure.step("Проверка header характеристики")
    def check_memory_product(self, locator_memory):
        self.logger.info(f'Check memory  {locator_memory}')
        memory_text = self.browser.find_element(*self.memory).text
        return memory_text

    @allure.step("Проверка описания характеристики")
    def check_name_memory(self, locator_name_memory):
        self.logger.info(f'Check memory table {locator_name_memory}')
        name_memory_text = self.browser.find_element(*self.name_memory).text
        return name_memory_text

    @allure.step("Проверка изображения продукта")
    def check_image_product(self,image_locator):
        self.logger.info(f'Check images of {image_locator}')
        image = self.browser.find_element(*self.image)
        return image

    @allure.step("Проверка поля кол-ва продукта")
    def check_product_number(self):
        self.logger.info(f'Seach table number for  {self.number_product}')
        element = self.browser.find_element(*self.number_product)
        return element



