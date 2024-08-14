from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from page_object.basepage import BasePage
from selenium.webdriver.support import expected_conditions as EC


class UserPage(BasePage):
    LOGIN_INPUT = By.ID, "input-username"
    PASSWORD_INPUT = By.ID, "input-password"
    SUBMIT_LOGIN_BUTTON = By.CSS_SELECTOR, "#form-login button"
    LOGOUT_LINK = By.LINK_TEXT, "Logout"
    USER_MENU = By.CSS_SELECTOR, "#column-right"
    WISH_LIST_LINK = By.LINK_TEXT, "Wish List"

    def login(self, username, password):
        self.browser.find_element(*self.LOGIN_INPUT).send_keys(username)
        self.browser.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*self.SUBMIT_LOGIN_BUTTON).click()

    def go_to_admin_page(self,base_url):
        self.browser.get(base_url + "administration/")

    def wait_logged_in(self):
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.LOGOUT_LINK))

    def click_wish_list(self):
        self.browser.find_element(*self.USER_MENU).find_element(*self.WISH_LIST_LINK).click()
