import pytest
import chromedriver_autoinstaller
from selenium import webdriver
from config.get_json_file import get_json_file

@pytest.fixture(scope="module")
def base_url():
    return "https://www.bkmkitap.com/"


@pytest.fixture(scope="function")
def driver():
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def status_message():
    return get_json_file("data/status_messages.json")

@pytest.fixture
def get_page(driver,base_url):
    def _get(page_class):
        driver.get(base_url)
        return page_class(driver)
    return _get