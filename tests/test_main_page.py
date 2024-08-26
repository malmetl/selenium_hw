import allure
from selenium.webdriver.common.by import By
from page_object.checkMainPage import checkImg
import time
from page_object.basepage import BasePage
from page_object.change_money import ChangeMoney
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature('Check main page')
@allure.title('Проверка логотипа')
def test_find_logo_id(browser, base_url):
    BasePage(browser).go_to_main_page(base_url)
    time.sleep(2)
    image_element = checkImg(browser).check_logo(checkImg.logo)
    assert image_element is not None


@allure.feature('Check main page')
@allure.title('Проверка шапочной картинки')
def test_find_image(browser, base_url):
    BasePage(browser).go_to_main_page(base_url)
    image_element = checkImg(browser).check_header(checkImg.header)
    assert image_element is not None
    assert image_element.get_attribute("src") != ""


@allure.feature('Check main page')
@allure.title('Проверка большой картинки')
def test_find_big_image(browser, base_url):
    BasePage(browser).go_to_main_page(base_url)
    big_image = checkImg(browser).check_big_image(checkImg.check_big_image)
    assert big_image.get_attribute("src") != ""


@allure.feature('Check main page')
@allure.title('Проверка поисковой строки')
def test_find_search(browser, base_url):
    BasePage(browser).go_to_main_page(base_url)
    search_find = checkImg(browser).check_search(checkImg.check_search)
    assert search_find.get_attribute("id") != ""


@allure.feature('Check main page')
@allure.title('Проверка кнопки "Поиск"')
def test_find_button(browser, base_url):
    BasePage(browser).go_to_main_page(base_url)
    time.sleep(2)
    cart_buttons = checkImg(browser).check_search_button
    time.sleep(2)
    assert cart_buttons is not None


@allure.feature('Check main page')
@allure.title('Проверка смены валюты')
def test_change_money(browser, base_url):
    BasePage(browser).go_to_main_page(base_url)
    ChangeMoney(browser).change_to_euro(ChangeMoney.toggle, ChangeMoney.selector)
    browser.find_elements(By.CLASS_NAME, "product-thumb")[0].click()
    price_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h2")))
    assert "£427.82" in price_element.text
