from selenium.webdriver.common.by import By
import time
from page_object.basepage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_object.selector import selector
from page_object.chage_category_catalog import change_to_category
from page_object.wishList import WishList
from page_object.change_money import ChangeMoney

def test_main_page_open_product(browser, base_url):
    BasePage(browser).go_to_catalog_page(base_url)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "compare-total"))).click()
    compare_page_message = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#content > p"))).text
    assert "You have not chosen any products to compare." in compare_page_message


def test_main_page_htc(browser, base_url):
    BasePage(browser).go_to_catalog_page(base_url)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "product-thumb"))).click()
    WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.LINK_TEXT, "HTC Touch HD")))
    assert "HTC Touch HD" is not None


def test_main_page_filtr(browser, base_url):
    BasePage(browser).go_to_catalog_page(base_url)
    selector(browser).selector_to_price()
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "product-thumb"))).click()
    product_name_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h4")))
    product_name = product_name_element.text
    assert "Palm Treo Pro" in product_name


def test_main_page_change_to_pc(browser, base_url):
    BasePage(browser).go_to_catalog_page(base_url)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#column-left > div:nth-child(1) a:nth-child(7)"))).click()
    test_change_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h4")))
    test_change = test_change_element.text
    assert "Canon EOS 5D" in test_change


def test_main_page_change_aler(browser, base_url):
    BasePage(browser).go_to_catalog_page(base_url)
    change_to_category(browser).change_to_photograph()
    browser.find_element(By.XPATH, '//*[@id="product-list"]/div[1]/div/div[1]/a/img').click()
    WishList(browser).add_to_wish_list()
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "alert-success")))


def test_change_money_in_catalog(browser, base_url):
    BasePage(browser).go_to_catalog_page(base_url)
    ChangeMoney(browser).change_to_euro()
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "product-thumb"))).click()
    assert "£74.73" in browser.find_element(By.TAG_NAME, "h2").text
