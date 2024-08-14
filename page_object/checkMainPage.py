import allure
from selenium.webdriver.common.by import By
from page_object.basepage import BasePage


class checkImg(BasePage):
    logo = By.XPATH, '//*[@id="logo"]/a/img'
    header = By.XPATH, '/html/body/header/div/div/div[1]/div/a/img'
    big_image = By.XPATH, '//*[@id="carousel-banner-0"]/div[2]/div[1]/div/div/a/img'
    search = By.ID, 'search'
    search_button = By.XPATH, '//*[@id="search"]/button'

    @allure.step("Проверка логотипа")
    def check_logo(self, logo_locator):
        self.logger.info(f'Checking logo for {logo_locator}')
        element = self.browser.find_element(*self.logo)
        return element

    @allure.step("Проверка шапки главной страницы")
    def check_header(self, header_locator):
        self.logger.info(f'Checking logo for {header_locator}')
        element = self.browser.find_element(*self.header)
        return element

    @allure.step("Проверка общей картинки на главной странице")
    def check_big_image(self, big_image_locator):
        self.logger.info(f'Checking logo for {big_image_locator}')
        element = self.browser.find_element(*self.big_image)
        return element

    @allure.step("Проверка поисковой строки")
    def check_search(self, search_locator):
        self.logger.info(f'Checking logo for {search_locator}')
        element = self.browser.find_element(*self.search)
        return element

    @allure.step("Проверка поисковой кнопки")
    def check_search_button(self):
        self.logger.info(f'Checking logo for {self.search_button}')
        element = self.browser.find_element(*self.search_button)
        return element
