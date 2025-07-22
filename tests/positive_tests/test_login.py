from pages.login_page import LoginPage
from config.get_json_file import get_json_file
import pytest

@pytest.fixture(scope="module")
def login_data():
    return get_json_file("data/valid_login_data.json")

class TestLogin:

    def test_successful_login_with_email(self,driver,status_message,login_data):
        url ="https://www.bkmkitap.com/"
        driver.get(url)
        page = LoginPage(driver)
        user_credentials = login_data["valid_email_login"]
        
        page.open_login_popup()
        page.login_user(user_credentials)

        login_status = status_message[user_credentials["expected_message_key"]]
        assert page.get_status_message_by_locator(login_status["locator"]) == login_status["message"], f"{user_credentials['description']}: This case has failed."
    

    @pytest.mark.xfail(reason="Login with username is not implemented")
    def test_successful_login_with_username(self,driver,status_message,login_data):
        url ="https://www.bkmkitap.com/"
        driver.get(url)
        page = LoginPage(driver)
        user_credentials =login_data["valid_username_login"]

        page.open_login_popup()
        page.login_user(user_credentials)

        login_status = status_message[user_credentials["expected_message_key"]]
        assert page.get_status_message_by_locator(login_status["locator"]) == login_status["message"], f"{user_credentials['description']}: This case has failed."