from selenium.webdriver.common.by import By
import time
from page_object.basepage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_object.selector import selector
from page_object.chage_category_catalog import change_to_category
from page_object.wishList import WishList
from page_object.change_money import ChangeMoney
import allure
from page_object.catalogPage import ComparePage


@allure.feature('Catalog Page')
@allure.title('Выбор продукта через каталог')
def test_main_page_open_product(browser, base_url):
    BasePage(browser).go_to_catalog_page(base_url)
    message = ComparePage(browser).check_compare_total(ComparePage.compare_total_id, ComparePage.compare_message_css)
    assert "You have not chosen any products to compare." in message


@allure.feature('Catalog Page')
@allure.title('Выбор определённого продукта')
def test_main_page_htc(browser, base_url):
    BasePage(browser).go_to_catalog_page(base_url)
    with allure.step("Нажать на первый смартфон"):
        locator = By.CLASS_NAME, "product-thumb"
        allure.attach(str(locator), name="Locator", attachment_type=allure.attachment_type.TEXT)
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable(locator)).click()
    with allure.step("Убедиться, что это HTC Touch HD и сделать скриншот"):
        locator = By.LINK_TEXT, "HTC Touch HD"
        allure.attach(str(locator), name="Locator", attachment_type=allure.attachment_type.TEXT)
        WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located(locator))
        screenshot = browser.get_screenshot_as_png()
        allure.attach(screenshot, name="Screenshot of HTC Touch HD", attachment_type=allure.attachment_type.PNG)
    assert "HTC Touch HD" is not None


@allure.feature('Catalog Page')
@allure.title('Проверка селектора по цене')
def test_main_page_filtr(browser, base_url):
    BasePage(browser).go_to_catalog_page(base_url)
    selector(browser).selector_to_price(selector.locator)
    with allure.step("Нажать на выбранный селектор"):
        locator = By.CLASS_NAME, "product-thumb"
        allure.attach(str(locator), name="Locator", attachment_type=allure.attachment_type.TEXT)
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable(locator)).click()
    with allure.step("Проверить правильность селекта"):
        locator = (By.LINK_TEXT, "Palm Treo Pro")
        allure.attach(str(locator), name="Locator", attachment_type=allure.attachment_type.TEXT)
        WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located(locator))
        screenshot = browser.get_screenshot_as_png()
        allure.attach(screenshot, name="Screenshot of HTC Touch HD", attachment_type=allure.attachment_type.PNG)
    assert "Palm Treo Pro" is not None


@allure.feature('Catalog Page')
@allure.title('Проверка смены каталога')
def test_main_page_change_to_pc(browser, base_url):
    BasePage(browser).go_to_catalog_page(base_url)
    selector(browser).select_photo_catalog()
    test_change_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h4")))
    test_change = test_change_element.text
    assert "Nikon D300" in test_change


@allure.feature('Catalog Page')
@allure.title('Проверка добавление в Wish list')
def test_main_page_change_aler(browser, base_url):
    BasePage(browser).go_to_catalog_page(base_url)
    selector(browser).select_photo_catalog()
    browser.find_element(By.XPATH, '//*[@id="product-list"]/div[1]/div/div[1]/a/img').click()
    WishList(browser).add_to_wish_list(WishList.add_wish_list)
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "alert-success")))


@allure.feature('Catalog Page')
@allure.title('Смена валют')
def test_change_money_in_catalog(browser, base_url):
    BasePage(browser).go_to_catalog_page(base_url)
    ChangeMoney(browser).change_to_euro(ChangeMoney.selector, ChangeMoney.toggle)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "product-thumb"))).click()
    assert "£86.70" in browser.find_element(By.TAG_NAME, "h2").text
