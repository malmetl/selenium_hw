import time

from selenium.webdriver.common.by import By
from page_object.UserPage import UserPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_object.adminpage import AdminPage
from selenium.webdriver.common.alert import Alert


def test_administration_page_header(browser, base_url):
    UserPage(browser).go_to_admin_page(base_url)
    txt = browser.find_element(By.CLASS_NAME, "card-header")
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "card-header")))
    assert txt.text == "Please enter your login details."


def test_login(browser, base_url):
    UserPage(browser).go_to_admin_page(base_url)
    UserPage(browser).login("User", "bitnami")
    WebDriverWait(browser, 2).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#nav-profile > a > span"), "John Doe"))
    assert "John Doe" in browser.find_element(By.CSS_SELECTOR, "#nav-profile > a > span").text


def test_logout(browser, base_url):
    UserPage(browser).go_to_admin_page(base_url)
    UserPage(browser).login("User", "bitnami")
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "nav-logout"))).click()
    assert "Password" in browser.find_element(By.CSS_SELECTOR, "#form-login > div:nth-of-type(2) > label").text
    assert "Username" in browser.find_element(By.CLASS_NAME, "mb-3").text


def test_bad_login(browser, base_url):
    UserPage(browser).go_to_admin_page(base_url)
    UserPage(browser).login("User123", "bitnami")
    error_message = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#alert > div")))
    assert "No match for Username and/or Password." in error_message.text


def test_admin_panel_categ(browser, base_url):
    UserPage(browser).go_to_admin_page(base_url)
    UserPage(browser).login("User", "bitnami")
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div[1]/div/h1')))


def test_add_product(browser, base_url):
    UserPage(browser).go_to_admin_page(base_url)
    UserPage(browser).login("User", "bitnami")
    AdminPage(browser).description_new_product()
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[1]/div/div/button')))
    assert browser.find_element(By.XPATH, '//*[@id="alert"]/div')


def test_delete_product(browser, base_url):
    UserPage(browser).go_to_admin_page(base_url)
    UserPage(browser).login("User", "bitnami")
    AdminPage(browser).to_product(base_url)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form-product"]/div[1]/table/tbody/tr[1]/td[1]/input'))).click()
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[1]/div/div/button[3]'))).click()
    WebDriverWait(browser, 10).until(EC.alert_is_present())
    alert = Alert(browser)
    alert.accept()
    time.sleep(2)

