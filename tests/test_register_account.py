import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_object.basepage import BasePage
from page_object.regAccount import registrationAccount


def test_register(browser, base_url):
    BasePage(browser).go_to_main_page(base_url)
    browser.find_elements(By.CLASS_NAME, "dropdown-toggle")[1].click()
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="top"]/div/div[2]/ul/li[2]/div/ul/li[1]/a'))).click()
    register_header = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    assert "Register Account" in register_header.text


def test_succesfull_register(browser, base_url):
    BasePage(browser).go_to_reg_page(base_url)
    time.sleep(1)
    registrationAccount(browser).registerUser("Maximilioano", "Rengager", "asdsdsdad@mail.ru", "testpass")
    time.sleep(2)
    assert "Your Account Has Been Created!" in browser.find_element(By.ID, "content").text
    time.sleep(3)


def test_without_full_red_polya(browser, base_url):
    BasePage(browser).go_to_reg_page(base_url)
    time.sleep(1)
    browser.find_element(*registrationAccount.firstnameAccount).send_keys("Maximiliano")
    browser.find_element(*registrationAccount.lastnameAccount).send_keys("Fertuche")
    browser.find_element(*registrationAccount.passwordAccount).send_keys("213213paswordw")
    browser.find_element(By.XPATH, '//*[@id="form-register"]/div/div/input').click()
    time.sleep(3)
    browser.find_element(By.XPATH, '//*[@id="form-register"]/div/button').click()
    time.sleep(4)
    assert "E-Mail Address does not appear to be valid!" in browser.find_element(By.CSS_SELECTOR, "#error-email").text
    time.sleep(2)


def test_full_registration(browser, base_url):
    BasePage(browser).go_to_reg_page(base_url)
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "input-firstname")))
    registrationAccount(browser).registerRandomUser()
    continue_link = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='content']/div/a")))
    continue_link.click()
    my_account_header = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h2")))
    assert "My Account" in my_account_header.text


def test_easy_check_reg(browser, base_url):
    BasePage(browser).go_to_reg_page(base_url)
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="form-register"]/div/button').click()
    time.sleep(3)
    assert "First Name must be between 1 and 32 characters!" in browser.find_element(By.ID, "error-firstname").text
    assert "Last Name must be between 1 and 32 characters!" in browser.find_element(By.ID, "error-lastname").text
    assert "E-Mail Address does not appear to be valid!" in browser.find_element(By.ID, "error-email").text
    assert "Password must be between 4 and 20 characters!" in browser.find_element(By.ID, "error-password").text
    time.sleep(4)
