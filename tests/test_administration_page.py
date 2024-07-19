from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
from LoginAdmin import pageLogin
from LoginAdmin.pageLogin import LoginAdminPage


def test_administration_page_header(browser, base_url):
    browser.get(base_url + "administration/")
    txt = browser.find_element(By.CLASS_NAME, "card-header")
    time.sleep(2)
    assert txt.text == "Please enter your login details."


def test_login(browser, base_url):
    browser.get(base_url + "administration/")
    us = browser.find_element(By.CLASS_NAME, "mb-3")
    time.sleep(2)
    assert us.text == "Username"
    ps = browser.find_element(By.CSS_SELECTOR, "#form-login > div:nth-of-type(2) > label")
    assert ps.text == "Password"
    browser.find_element(*LoginAdminPage.USERNAME_INPUT).send_keys("User")
    browser.find_element(*LoginAdminPage.PASSWORD_INPUT).send_keys("bitnami")
    time.sleep(2)
    browser.find_element(*LoginAdminPage.SUBMIT_BUTTON).click()
    time.sleep(2)
    assert "John Doe" in browser.find_element(By.CSS_SELECTOR, "#nav-profile > a > span").text


def test_logout(browser, base_url):
    browser.get(base_url + "administration/")
    browser.find_element(*LoginAdminPage.USERNAME_INPUT).send_keys("User")
    browser.find_element(*LoginAdminPage.PASSWORD_INPUT).send_keys("bitnami")
    browser.find_element(*LoginAdminPage.SUBMIT_BUTTON).click()
    time.sleep(2)
    browser.find_element(By.ID, "nav-logout").click()
    time.sleep(1)
    assert "Password" in browser.find_element(By.CSS_SELECTOR, "#form-login > div:nth-of-type(2) > label").text
    assert "Username" in browser.find_element(By.CLASS_NAME, "mb-3").text


def test_bad_login(browser, base_url):
    browser.get(base_url + "administration/")
    browser.find_element(*LoginAdminPage.USERNAME_INPUT).send_keys("User123")
    browser.find_element(*LoginAdminPage.PASSWORD_INPUT).send_keys("bitnami123")
    browser.find_element(*LoginAdminPage.SUBMIT_BUTTON).click()
    time.sleep(2)
    assert "No match for Username and/or Password." in browser.find_element(By.CSS_SELECTOR, "#alert > div").text

