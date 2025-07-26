from pages.login_page import LoginPage
from config.get_json_file import get_json_file
import pytest


class TestInvalidLogin:
    @pytest.mark.parametrize("user_credentials",get_json_file("data/invalid_login_data.json"))
    def test_invalid_login(self,get_page,status_message,user_credentials):
        page = get_page(LoginPage)
        
        page.open_login_popup()
        page.login_user(user_credentials)

        login_status = status_message[user_credentials["expected_message_key"]]
        assert page.get_status_message_by_locator(login_status["locator"]) == login_status["message"] ,f"{user_credentials["description"]}: This case has failed"