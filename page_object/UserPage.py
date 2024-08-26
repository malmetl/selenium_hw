from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from page_object.basepage import BasePage
from selenium.webdriver.support import expected_conditions as EC
import allure


class UserPage(BasePage):
    LOGIN_INPUT = By.ID, "input-username"
    PASSWORD_INPUT = By.ID, "input-password"
    SUBMIT_LOGIN_BUTTON = By.CSS_SELECTOR, "#form-login button"
    LOGOUT_LINK = By.LINK_TEXT, "Logout"
    USER_MENU = By.CSS_SELECTOR, "#column-right"
    WISH_LIST_LINK = By.LINK_TEXT, "Wish List"

    @allure.step("Войти в личный кабинет")
    def login(self, username, password):
        self.logger.info(f'Send key "{username}" using locator  {self.LOGIN_INPUT}')
        self.browser.find_element(*self.LOGIN_INPUT).send_keys(username)
        self.logger.info(f'Send key "{password}" using locator  {self.PASSWORD_INPUT}')
        self.browser.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*self.SUBMIT_LOGIN_BUTTON).click()

    @allure.step("Переход на страницу администратора")
    def go_to_admin_page(self,base_url):
        self.logger.info(f"Going to {base_url + "administration/"}")
        self.browser.get(base_url + "administration/")

    @allure.step("Ожидание локатора на выход")
    def wait_logged_in(self, LOGOUT_LINK):
        self.logger.info(f'Waiting for logout {LOGOUT_LINK}')
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.LOGOUT_LINK))


