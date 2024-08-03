from selenium.webdriver.common.by import By
import time
from page_object.basepage import BasePage
from page_object.cart import Cart
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_page_product(browser, base_url):
    BasePage(browser).go_to_main_page(base_url)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "product-thumb"))).click()
    header = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1"))).text
    assert "MacBook" in header


def test_main_page_brand(browser, base_url):
    BasePage(browser).go_to_macbook_page(base_url)
    time.sleep(3)
    header = browser.find_element(By.CSS_SELECTOR, "#content > ul > li:nth-of-type(2) > a").click()
    time.sleep(2)
    memory = browser.find_element(By.CSS_SELECTOR,
                                  "#tab-specification > div > table > thead:first-of-type > tr > td").text
    time.sleep(1)
    assert "Memory" in memory
    time.sleep(2)
    name_memory = browser.find_element(By.CSS_SELECTOR,
                                       "#tab-specification > div > table > tbody:first-of-type > tr > td:first-of-type").text
    time.sleep(2)
    assert "test 1" in name_memory


def test_img_mac(browser, base_url):
    BasePage(browser).go_to_macbook_page(base_url)
    img = browser.find_element(By.CSS_SELECTOR, "#content > div:first-of-type > div:first-of-type > div > a > img")
    assert img is not None
    assert img.get_attribute("src") != ""


def test_button_carts(browser, base_url):
    BasePage(browser).go_to_macbook_page(base_url)
    Cart(browser).add_to_cart(base_url)
    Cart(browser).check_cart()
    time.sleep(3)
    succ_full = browser.find_element(By.CLASS_NAME, "text-start")
    assert "MacBook" in succ_full.text


def test_button_carts(browser, base_url):
    BasePage(browser).go_to_macbook_page(base_url)
    numbers = browser.find_element(By.ID, "input-quantity")
    time.sleep(1)
    numbers.click()
    numbers.clear()
    numbers.send_keys("3")
    assert numbers.get_attribute("value") == "3"
