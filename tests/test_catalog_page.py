from selenium.webdriver.common.by import By
import time


def test_main_page_open_product(browser, base_url):
    browser.get(base_url + "en-gb/catalog/smartphone")
    btn = browser.find_element(By.ID, "compare-total")
    time.sleep(2)
    btn.click()
    copare_page = browser.find_element(By.CSS_SELECTOR, "#content > p").text
    assert "You have not chosen any products to compare." in copare_page
    time.sleep(2)


def test_main_page_htc(browser, base_url):
    browser.get(base_url + "en-gb/catalog/smartphone")
    phone_htc = browser.find_elements(By.CLASS_NAME, "product-thumb")
    phone_htc[0].click()
    phone_htc1 = browser.find_elements(By.LINK_TEXT, "HTC Touch HD")
    time.sleep(1)
    assert phone_htc1 is not None


def test_main_page_filtr(browser, base_url):
    browser.get(base_url + "en-gb/catalog/smartphone")
    btn_grid = browser.find_element(By.ID, "button-list")
    btn_grid.click()
    fifth_option = browser.find_element(By.CSS_SELECTOR, "#input-sort > option:nth-child(5)")
    time.sleep(1)
    fifth_option.click()
    time.sleep(1)
    expensive = browser.find_elements(By.CLASS_NAME, "product-thumb")
    expensive[0].click()
    time.sleep(1)
    product_name = browser.find_element(By.TAG_NAME, "h4").text
    print(product_name)
    assert "Palm Treo Pro" in product_name


def test_main_page_change_to_pc(browser, base_url):
    browser.get(base_url + "en-gb/catalog/smartphone")
    time.sleep(1)
    change = browser.find_elements(By.CSS_SELECTOR, "#column-left > div:nth-child(1) a")
    change[6].click()
    time.sleep(2)
    test_change = browser.find_element(By.TAG_NAME, "h4").text
    assert "Canon EOS 5D" in test_change


def test_main_page_change_aler(browser, base_url):
    browser.get(base_url + "en-gb/catalog/smartphone")
    time.sleep(1)
    change = browser.find_elements(By.CSS_SELECTOR, "#column-left > div:nth-child(1) a")
    change[6].click()
    time.sleep(2)
    btn_love = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    btn_love.click()
    time.sleep(2)
    btn_love = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    btn_love.click()
    time.sleep(2)

