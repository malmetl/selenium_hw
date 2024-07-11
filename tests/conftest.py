import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FFOptions
def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="ch", choices=["ch", "ya", "ff"]
    )
    parser.addoption(
        "--headless", action="store_true", default=False
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
