import logging
import os

import allure
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, browser, log_level=logging.INFO, to_file=False):
        self.browser = browser
        self.actions = ActionChains(browser)
        self.__config_logger(log_level, to_file)

    def __config_logger(self, log_level, to_file):
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.setLevel(log_level)
        if not self.logger.hasHandlers():
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

            if to_file:
                os.makedirs("logs", exist_ok=True)
                file_handler = logging.FileHandler('logs/application.log')
                file_handler.setFormatter(formatter)
                self.logger.addHandler(file_handler)

            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

    @allure.step(f'Открываю url страницы каталога смартфонов')
    def go_to_catalog_page(self, base_url):
        self.logger.info(f"Going to {base_url}en-gb/catalog/smartphone")
        self.browser.get(base_url + "en-gb/catalog/smartphone")

    @allure.step(f'Открываю url главной страницы')
    def go_to_main_page(self, base_url):
        self.logger.info(f"Going to {base_url}")
        self.browser.get(base_url)

    @allure.step(f'Открываю url продукта Macbook')
    def go_to_macbook_page(self, base_url):
        self.logger.info(f"Going to {base_url}en-gb/product/macbook")
        self.browser.get(base_url + "en-gb/product/macbook")

    @allure.step(f'Открываю url страницы регистрации')
    def go_to_reg_page(self, base_url):
        self.logger.info(f"Going to {base_url}index.php?route=account/register")
        self.browser.get(base_url + "/index.php?route=account/register")
