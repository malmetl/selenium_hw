from selenium.webdriver.common.by import By
import time


class LoginAdminPage:
    USERNAME_INPUT = (By.ID, "input-username")
    PASSWORD_INPUT = (By.ID, "input-password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

