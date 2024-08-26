import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from page_object.basepage import BasePage
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import logging

fake = Faker()


class AdminPage(BasePage):
    error_mesage = By.CSS_SELECTOR, '#alert > div'
    logout = By.XPATH, '//*[@id="nav-logout"]/a'
    PRODUCT_NAME = By.ID, 'input-name-1'
    DESCRIPTION = By.CSS_SELECTOR, 'html > body > p'
    META_TAG_TITLE = By.ID, 'input-meta-title-1'
    META_TAG_DESCRIPTION = By.ID, 'input-meta-description-1'
    META_TAG_KEYWORDS = By.ID, 'input-meta-keyword-1'
    PRODUCT_TAGS = By.ID, 'input-tag-1'
    MODEL = By.ID, 'input-model'
    SKU = By.ID, 'input-sku'
    UPC = By.ID, 'input-upc'
    EAN = By.ID, 'input-ean'
    JAN = By.ID, 'input-jan'
    ISBN = By.ID, 'input-isbn'
    MPN = By.ID, 'input-mpn'
    LOCATION = By.ID, 'input-location'
    PRICE = By.ID, 'input-price'
    MANUFACTURER = By.ID, 'autocomplete-manufacturer'
    CATEGORIES = By.ID, 'autocomplete-category'
    SEO = By.ID, 'input-keyword-0-1'
    first = By.XPATH, '//*[@id="form-product"]/div[1]/table/tbody/tr[1]/td[1]/input'
    second = By.XPATH, '//*[@id="content"]/div[1]/div/div/button[3]'

    def to_product(self, browser):
        WebDriverWait(self.browser, 10).until((EC.element_to_be_clickable((By.ID, 'menu-catalog')))).click()
        WebDriverWait(self.browser, 10).until(
            (EC.element_to_be_clickable((By.XPATH, '//*[@id="collapse-1"]/li[2]/a')))).click()

    def __init__(self, browser):
        super().__init__(browser)
        self.fake = Faker()

    def description_new_product(self, PRODUCT_NAME_LOC):
        WebDriverWait(self.browser, 10).until((EC.element_to_be_clickable((By.ID, 'menu-catalog')))).click()
        WebDriverWait(self.browser, 10).until(
            (EC.element_to_be_clickable((By.XPATH, '//*[@id="collapse-1"]/li[2]/a')))).click()
        WebDriverWait(self.browser, 10).until(
            (EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[1]/div/div/a')))).click()
        WebDriverWait(self.browser, 10).until(
            (EC.element_to_be_clickable((By.CLASS_NAME, 'cke_notification_close')))).click()
        product_name = self.fake.catch_phrase()
        meta_tag_title = self.fake.sentence(nb_words=6)
        meta_tag_description = self.fake.text(max_nb_chars=160)
        meta_tag_keywords = ', '.join(self.fake.words(nb=10))
        product_tags = ', '.join(self.fake.words(nb=5))
        self.model = self.fake.bothify(text='??-####')
        sku = self.fake.bothify(text='SKU-#####')
        upc = self.fake.ean(length=13)
        ean = self.fake.ean(length=13)
        jan = self.fake.ean(length=13)
        isbn = self.fake.isbn13()
        mpn = self.fake.bothify(text='MPN-#####')
        location = self.fake.city()
        price = f'{self.fake.random_number(digits=2)}.{self.fake.random_number(digits=2)}'
        seo = ''.join(self.fake.words(nb=1))

        self.logger.info(f'Go to product {PRODUCT_NAME_LOC}')
        self.browser.find_element(*self.PRODUCT_NAME).send_keys(product_name)
        self.browser.find_element(*self.META_TAG_TITLE).send_keys(meta_tag_title)
        self.browser.find_element(*self.META_TAG_DESCRIPTION).send_keys(meta_tag_description)
        self.browser.find_element(*self.META_TAG_KEYWORDS).send_keys(meta_tag_keywords)
        self.browser.find_element(*self.PRODUCT_TAGS).send_keys(product_tags)
        WebDriverWait(self.browser, 10).until(
            (EC.element_to_be_clickable((By.XPATH, '//*[@id="form-product"]/ul/li[2]/a')))).click()
        self.browser.find_element(*self.MODEL).send_keys(self.model)
        self.browser.find_element(*self.SKU).send_keys(sku)
        self.browser.find_element(*self.UPC).send_keys(upc)
        self.browser.find_element(*self.EAN).send_keys(ean)
        self.browser.find_element(*self.JAN).send_keys(jan)
        self.browser.find_element(*self.ISBN).send_keys(isbn)
        self.browser.find_element(*self.MPN).send_keys(mpn)
        self.browser.find_element(*self.LOCATION).send_keys(location)
        self.browser.find_element(*self.PRICE).send_keys(price)
        WebDriverWait(self.browser, 10).until(
            (EC.element_to_be_clickable((By.XPATH, '//*[@id="form-product"]/ul/li[2]/a')))).click()
        WebDriverWait(self.browser, 10).until((EC.element_to_be_clickable((By.ID, 'input-tax-class')))).click()
        WebDriverWait(self.browser, 10).until(
            (EC.element_to_be_clickable((By.XPATH, '//*[@id="form-product"]/ul/li[3]/a')))).click()
        WebDriverWait(self.browser, 10).until(
            (EC.element_to_be_clickable((By.XPATH, '//*[@id="form-product"]/ul/li[11]/a')))).click()
        self.browser.find_element(*self.SEO).send_keys(seo)
        WebDriverWait(self.browser, 10).until(
            (EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[1]/div/div/button')))).click()


    @allure.step("Выход из админ панели")
    def check_logout(self, logout_locator):
        self.logger.info(f'Go to logout {logout_locator}')
        element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(logout_locator))
        element.click()
        return element

    @allure.step('Проверка error alert')
    def error_login(self, error_locator):
        self.logger.info(f'Go to {error_locator}')
        error_message = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(error_locator))
        return error_message
    @allure.step('Выбрать и нажать кнопку "Удалить"')
    def delete_first_product(self,fist_locator, second_locator):
        self.logger.info(f'Go to {fist_locator}')
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(fist_locator)).click()
        self.logger.info(f'Go to {second_locator}')
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(second_locator)).click()
