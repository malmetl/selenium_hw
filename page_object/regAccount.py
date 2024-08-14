from page_object.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

fake = Faker()


class registrationAccount(BasePage):
    firstnameAccount = (By.ID, "input-firstname")
    lastnameAccount = (By.ID, "input-lastname")
    emailAccount = (By.ID, "input-email")
    passwordAccount = (By.ID, "input-password")

    def registerUser(self, firstname, lastname, email, password):
        self.browser.find_element(*self.firstnameAccount).send_keys(firstname)
        self.browser.find_element(*self.lastnameAccount).send_keys(lastname)
        self.browser.find_element(*self.emailAccount).send_keys(email)
        self.browser.find_element(*self.passwordAccount).send_keys(password)
        self.browser.find_element(By.XPATH, '//*[@id="form-register"]/div/div/input').click()
        self.browser.find_element(By.XPATH, '//*[@id="form-register"]/div/button').click()

    def registerRandomUser(self):
        firstname = fake.first_name()
        lastname = fake.last_name()
        email = fake.email()
        password = fake.password()
        self.registerUser(firstname, lastname, email, password)
