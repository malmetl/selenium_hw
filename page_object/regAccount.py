import allure

from page_object.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import logging

fake = Faker()


class registrationAccount(BasePage):
    firstnameAccount = By.ID, 'input-firstname'
    lastnameAccount = By.ID, 'input-lastname'
    emailAccount = By.ID, 'input-email'
    passwordAccount = By.ID, 'input-password'
    register_link = By.XPATH, '//*[@id="top"]/div/div[2]/ul/li[2]/div/ul/li[1]/a'
    toggle_link = By.CLASS_NAME, 'dropdown-toggle'

    @allure.step("Заполнение формы регистрации: {firstname}, {lastname}, {email}, {password}")
    def registerUser(self, firstname, lastname, email, password):
        self.logger.info(f'Sending keys to firstname: {firstname} using locator {self.firstnameAccount}')
        self.browser.find_element(*self.firstnameAccount).send_keys(firstname)
        self.logger.info(f'Sending keys to lastname: {lastname} using locator {self.lastnameAccount}')
        self.browser.find_element(*self.lastnameAccount).send_keys(lastname)
        self.logger.info(f'Sending keys to email: {email} using locator {self.emailAccount}')
        self.browser.find_element(*self.emailAccount).send_keys(email)
        self.logger.info(f'Sending keys to password: {password} using locator {self.passwordAccount}')
        self.browser.find_element(*self.passwordAccount).send_keys(password)
        self.logger.info('Clicking on the checkbox')
        self.browser.find_element(By.XPATH, '//*[@id="form-register"]/div/div/input').click()
        self.logger.info('Clicking on the register button')
        self.browser.find_element(By.XPATH, '//*[@id="form-register"]/div/button').click()

    @allure.step('Рандомные данные регистрации')
    def registerRandomUser(self):
        firstname = fake.first_name()
        lastname = fake.last_name()
        email = fake.email()
        password = fake.password()
        self.registerUser(firstname, lastname, email, password)

    @allure.step('Проверка страницы регистрации')
    def check_page_register(self, register_link, toggle_link):
        self.logger.info(f'Check link {toggle_link}')
        elements = self.browser.find_elements(*toggle_link)

        if len(elements) > 1:
            elements[1].click()
        else:
            self.logger.error("Dont find index [1] in toggle_link")
            return
        self.logger.info(f'Check link {register_link}')
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(register_link)).click()

    @allure.step("Заполнение формы регистрации: {firstname}, {lastname}, {password}")
    def check_register_no_full_data(self, firstname, lastname, password):
        self.logger.info(f'Sending keys to firstname: {firstname} using locator {self.firstnameAccount}')
        self.browser.find_element(*self.firstnameAccount).send_keys(firstname)
        self.logger.info(f'Sending keys to lastname: {lastname} using locator {self.lastnameAccount}')
        self.browser.find_element(*self.lastnameAccount).send_keys(lastname)
        self.logger.info(f'Sending keys to password: {password} using locator {self.passwordAccount}')
        self.browser.find_element(*self.passwordAccount).send_keys(password)
        self.logger.info('Clicking on the checkbox')
        self.browser.find_element(By.XPATH, '//*[@id="form-register"]/div/div/input').click()
        self.logger.info('Clicking on the register button')
        self.browser.find_element(By.XPATH, '//*[@id="form-register"]/div/button').click()
