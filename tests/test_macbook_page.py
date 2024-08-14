import allure
from selenium.webdriver.common.by import By
import time
from page_object.basepage import BasePage
from page_object.cart import Cart
from page_object.productPage import ProductPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature('Product Page')
@allure.title('Главная страница продукта')
def test_main_page_product(browser, base_url):
    BasePage(browser).go_to_main_page(base_url)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "product-thumb"))).click()
    header = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1"))).text
    assert "MacBook" in header


@allure.feature('Product Page')
@allure.title('Проверка описания продукта')
def test_main_page_brand(browser, base_url):
    BasePage(browser).go_to_macbook_page(base_url)
    time.sleep(3)
    memory = ProductPage(browser).check_memory_product(ProductPage.memory)
    name_memory = ProductPage(browser).check_name_memory(ProductPage.name_memory)
    assert memory is not None
    assert name_memory is not None


@allure.feature('Product Page')
@allure.title('Проверка изображения продукта')
def test_img_mac(browser, base_url):
    BasePage(browser).go_to_macbook_page(base_url)
    img = ProductPage(browser).check_image_product(ProductPage.image)
    assert img is not None
    assert img.get_attribute("src") != ""


@allure.feature('Product Page')
@allure.title('Проверка добавления продукта в корзину')
def test_button_carts(browser, base_url):
    BasePage(browser).go_to_macbook_page(base_url)
    Cart(browser).add_to_cart(Cart.button_cart)
    Cart(browser).check_cart(Cart.check_cart_product)
    time.sleep(3)
    succ_full = browser.find_element(By.CLASS_NAME, "text-start")
    assert succ_full is not None


@allure.feature('Product Page')
@allure.title('Изменение кол-ва продуктов')
def test_check_number(browser, base_url):
    BasePage(browser).go_to_macbook_page(base_url)
    numbers = ProductPage(browser).check_product_number()
    time.sleep(1)
    numbers.click()
    numbers.clear()
    numbers.send_keys("3")
    assert numbers.get_attribute("value") == "3"
