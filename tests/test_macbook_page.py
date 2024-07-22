from selenium.webdriver.common.by import By
import time


def test_main_page_product(browser, base_url):
    browser.get(base_url)
    items = browser.find_elements(By.CLASS_NAME, "product-thumb")
    items[0].click()
    time.sleep(2)
    header = browser.find_element(By.TAG_NAME, "h1").text
    assert "MacBook" in header
    time.sleep(2)


def test_main_page_brand(browser, base_url):
    browser.get(base_url + "en-gb/product/macbook")
    header = browser.find_element(By.CSS_SELECTOR, "#content > ul > li:nth-of-type(2) > a")
    time.sleep(2)
    header.click()
    time.sleep(2)
    memory = browser.find_element(By.CSS_SELECTOR, "#tab-specification > div > table > thead:first-of-type > tr > td").text
    time.sleep(1)
    assert "Memory" in memory
    name_memory = browser.find_element(By.CSS_SELECTOR, "#tab-specification > div > table > tbody:first-of-type > tr > td:first-of-type").text
    assert "test 1" in name_memory


def test_img_mac(browser, base_url):
    browser.get(base_url + "en-gb/product/macbook")
    img = browser.find_element(By.CSS_SELECTOR, "#content > div:first-of-type > div:first-of-type > div > a > img")
    assert img is not None
    assert img.get_attribute("src") != ""

def test_button_carts(browser, base_url):
    browser.get(base_url + "en-gb/product/macbook")
    btn = browser.find_element(By.ID, "button-cart")
    time.sleep(1)
    btn.click()
    time.sleep(1)
    succ = browser.find_element(By.CSS_SELECTOR, "#header-cart > div > button")
    succ.click()
    time.sleep(1)
    succ_full = browser.find_element(By.CLASS_NAME, "text-start")
    assert "MacBook" in succ_full.text

def test_button_carts(browser, base_url):
    browser.get(base_url + "en-gb/product/macbook")
    numbers = browser.find_element(By.ID, "input-quantity")
    time.sleep(1)
    numbers.click()
    numbers.clear()
    numbers.send_keys("3")
    assert numbers.get_attribute("value") == "3"


