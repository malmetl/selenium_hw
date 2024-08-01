from selenium.webdriver.common.by import By
import time


def test_find_logo_id(browser, base_url):
    browser.get(base_url)
    time.sleep(2)
    navbar_items = browser.find_element(By.ID, "logo")
    assert navbar_items is not None


def test_find_image(browser, base_url):
    browser.get(base_url)
    image_element = browser.find_element(By.XPATH, "/html/body/header/div/div/div[1]/div/a/img")
    assert image_element is not None
    assert image_element.get_attribute("src") != ""


def test_find_big_image(browser, base_url):
    browser.get(base_url)
    big_image = browser.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div[2]/div[1]/div/div/a/img")
    assert big_image.get_attribute("src") != ""


def test_find_search(browser, base_url):
    browser.get(base_url)
    search_find = browser.find_element(By.ID, "search")
    assert search_find.get_attribute("id") != ""


def test_find_button(browser, base_url):
    browser.get(base_url)
    time.sleep(2)
    cart_buttons = browser.find_elements(By.CSS_SELECTOR, "#navbar-menu > ul > li:first-child > a")
    assert cart_buttons is not None


def test_change_money(browser, base_url):
    browser.get(base_url)
    browser.find_element(By.CLASS_NAME, "dropdown-toggle").click()
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, "#form-currency > div > ul > li:nth-child(2) > a").click()
    time.sleep(2)
    browser.find_elements(By.CLASS_NAME, "product-thumb")[0].click()
    time.sleep(2)
    assert "£368.73" in browser.find_element(By.TAG_NAME, "h2").text



