import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import allure
import logging
import json


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--headless", action="store_true", default=False)
    parser.addoption("--opencart_url", action="store", default="http://192.168.17.119:8081/",
                     help="Base URL for OpenCart")
    parser.addoption("--executor", action="store", default="127.0.0.1")
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--logs", action="store_true")
    parser.addoption("--bv", action="store")


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    executor = request.config.getoption("--executor")
    vnc = request.config.getoption("--vnc")
    version = request.config.getoption("--bv")
    logs = request.config.getoption("--logs")
    executor_url = f"http://{executor}:4444/wd/hub"

    if browser_name == "chrome":
        options = ChromeOptions()
    elif browser_name == "firefox":
        options = FirefoxOptions()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    caps = {
        "browserName": browser_name,
        "browserVersion": version,
        "selenoid:options": {
            "name": request.node.name,
            "enableVNC": True,
            "screenResolution": "1920x1080",
            "enableLog": logs,
            "timeZone": "Europe/Moscow"
        },
        "acceptInsecureCerts": True,
    }
    for k, v in caps.items():
        options.set_capability(k, v)

        driver = webdriver.Remote(
            command_executor=executor_url,
            options=options
        )
    else:
        if browser_name == "chrome":
            driver = webdriver.Chrome(options=options)
        elif browser_name == "firefox":
            driver = webdriver.Firefox(options=options)

    allure.attach(
        name=driver.session_id,
        body=json.dumps(driver.capabilities, indent=4, ensure_ascii=False),
        attachment_type=allure.attachment_type.JSON
    )

    driver.test_name = request.node.name
    driver.log_level = logging.DEBUG

    yield driver
    driver.quit()


@pytest.fixture
def base_url(request):
    return request.config.getoption("--opencart_url")
