import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FFOptions
import time

def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="ch", choices=["ch", "eg", "ff"]
    )
    parser.addoption(
        "--headless", action="store_true", default=False
    )
    parser.addoption(
        "--opencart_url", action="store", default="http://192.168.0.11:8081/", help="Base URL for OpenCart"
    )


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")

    headless = request.config.getoption("--headless")
    driver = None

    if browser_name == "ch":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)

    elif browser_name == "ff":
        options = FFOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)

    elif browser_name == "eg":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)

    driver.set_window_size(1920, 1080)
    yield driver

    driver.quit()


@pytest.fixture
def base_url(request):
    return request.config.getoption("--opencart_url")
