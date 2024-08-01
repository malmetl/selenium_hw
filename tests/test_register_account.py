from selenium.webdriver.common.by import By
import time
from LoginAdmin.regAccount import registrationAccount
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_register(browser, base_url):
    browser.get(base_url)
    browser.find_elements(By.CLASS_NAME, "dropdown-toggle")[1].click()
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="top"]/div/div[2]/ul/li[2]/div/ul/li[1]/a').click()
    time.sleep(2)
    assert "Register Account" in browser.find_element(By.TAG_NAME, "h1").text


def test_succesfull_register(browser, base_url):
    browser.get(base_url + "/index.php?route=account/register")
    time.sleep(1)
    browser.find_element(*registrationAccount.firstnameAccount).send_keys("Maximiliano")
    browser.find_element(*registrationAccount.lastnameAccount).send_keys("Fertuche")
    browser.find_element(*registrationAccount.emailAccount).send_keys("333231315@mail.ru")
    browser.find_element(*registrationAccount.passwordAccount).send_keys("213213paswordw")
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="form-register"]/div/div/input').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '//*[@id="form-register"]/div/button').click()
    time.sleep(3)
    assert "Your Account Has Been Created!" in browser.find_element(By.ID, "content").text
    time.sleep(3)


def test_without_full_red_polya(browser, base_url):
    browser.get(base_url + "/index.php?route=account/register")
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
    browser.get(base_url + "/index.php?route=account/register")
    time.sleep(1)
    browser.find_element(*registrationAccount.firstnameAccount).send_keys("Maximiliano")
    browser.find_element(*registrationAccount.lastnameAccount).send_keys("Fertuche")
    browser.find_element(*registrationAccount.emailAccount).send_keys("3dddsdsd3231315@mail.ru")
    browser.find_element(*registrationAccount.passwordAccount).send_keys("213213paswordw")
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="form-register"]/div/div/input').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '//*[@id="form-register"]/div/button').click()
    time.sleep(3)
    browser.find_element(By.XPATH,"//*[@id='content']/div/a").click()
    time.sleep(2)
    assert "My Account" in browser.find_element(By.TAG_NAME,"h2").text

def test_easy_check_reg(browser, base_url):
    browser.get(base_url + "/index.php?route=account/register")
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="form-register"]/div/button').click()
    time.sleep(3)
    assert "First Name must be between 1 and 32 characters!" in browser.find_element(By.ID, "error-firstname").text
    assert "Last Name must be between 1 and 32 characters!" in browser.find_element(By.ID, "error-lastname").text
    assert "E-Mail Address does not appear to be valid!" in browser.find_element(By.ID, "error-email").text
    assert "Password must be between 4 and 20 characters!" in browser.find_element(By.ID, "error-password").text
    time.sleep(4)