import pytest
import chromedriver_autoinstaller
from selenium import webdriver
from config.get_json_file import get_json_file

@pytest.fixture
def url_factory():
    base_url = "https://www.bkmkitap.com"
    def make_url(detail):
        return f"{base_url}{detail}"
    return make_url

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