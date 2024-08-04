from selenium.webdriver.common.by import By
import time
from page_object.basepage import BasePage
from page_object.change_money import ChangeMoney
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_find_logo_id(browser, base_url):
    browser.get(base_url)
    time.sleep(2)
    navbar_items = browser.find_element(By.ID, "logo")
    assert navbar_items is not None


def test_find_image(browser, base_url):
    BasePage(browser).go_to_main_page(base_url)
    image_element = browser.find_element(By.XPATH, "/html/body/header/div/div/div[1]/div/a/img")
    assert image_element is not None
    assert image_element.get_attribute("src") != ""


def test_find_big_image(browser, base_url):
    BasePage(browser).go_to_main_page(base_url)
    big_image = browser.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div[2]/div[1]/div/div/a/img")
    assert big_image.get_attribute("src") != ""


def test_find_search(browser, base_url):
    BasePage(browser).go_to_main_page(base_url)
    search_find = browser.find_element(By.ID, "search")
    assert search_find.get_attribute("id") != ""


def test_find_button(browser, base_url):
    BasePage(browser).go_to_main_page(base_url)
    time.sleep(2)
    cart_buttons = browser.find_element(By.CSS_SELECTOR, "#navbar-menu > ul > li:first-child > a")
    cart_buttons.click()
    time.sleep(2)
    assert cart_buttons is not None


def test_change_money(browser, base_url):
    browser.get(base_url)
    ChangeMoney(browser).change_to_euro()
    browser.find_elements(By.CLASS_NAME, "product-thumb")[0].click()
    price_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h2")))
    assert "£368.73" in price_element.text



