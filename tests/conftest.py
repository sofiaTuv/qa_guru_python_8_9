import pytest
from selene.support.shared import browser
from selenium import webdriver

@pytest.fixture(scope='function', autouse=True)
def browser_management():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')

    browser.config.driver_options = options
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 15