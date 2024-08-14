import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_object.basepage import BasePage
from page_object.regAccount import registrationAccount
import allure


@allure.feature('Registration accountPage')
@allure.title('Проверка страницы регистрации')
def test_register(browser, base_url):
    BasePage(browser).go_to_main_page(base_url)
    registrationAccount(browser).check_page_register(registrationAccount.register_link, registrationAccount.toggle_link)
    time.sleep(2)
    register_header = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    assert "Register Account" in register_header.text


@allure.feature('Registration accountPage')
@allure.title('Проверка успешной регистрации')
def test_succesfull_register(browser, base_url):
    BasePage(browser).go_to_reg_page(base_url)
    registrationAccount(browser).registerUser("Maximilioano", "Rengager", "asd23111113123321sdsdad@mail.ru", "testpass")
    time.sleep(2)
    assert "Your Account Has Been Created!" in browser.find_element(By.ID, "content").text
    time.sleep(3)


@allure.feature('Registration accountPage')
@allure.title('Проверка ошибки при плохой регистрации')
def test_without_full_red_polya(browser, base_url):
    BasePage(browser).go_to_reg_page(base_url)
    time.sleep(1)
    registrationAccount(browser).check_register_no_full_data("Maximiliaono","Renagese","leasd")
    time.sleep(2)
    assert "E-Mail Address does not appear to be valid!" in browser.find_element(By.CSS_SELECTOR, "#error-email").text
    time.sleep(2)


@allure.feature('Registration accountPage')
@allure.title('Проверка полноценной регистрации')
def test_full_registration(browser, base_url):
    BasePage(browser).go_to_reg_page(base_url)
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "input-firstname")))
    registrationAccount(browser).registerRandomUser()
    continue_link = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='content']/div/a")))
    continue_link.click()
    my_account_header = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h2")))
    assert "My Account" in my_account_header.text


@allure.feature('Registration accountPage')
@allure.title('Проверка незаполняемость полей')
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
