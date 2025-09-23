import pytest
import chromedriver_autoinstaller
from selenium import webdriver
from config.get_json_file import get_json_file
import logging

@pytest.fixture(scope="session")
def logger():
    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(console_format)
        logger.addHandler(console_handler)

        file_handler = logging.FileHandler("test_logs.log", mode='w', encoding='utf-8')
        file_handler.setLevel(logging.INFO)
        file_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_format)
        logger.addHandler(file_handler)
        
    return logger


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