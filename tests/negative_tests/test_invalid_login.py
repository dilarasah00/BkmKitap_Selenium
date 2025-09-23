from pages.login_page import LoginPage
from config.get_json_file import get_json_file
import pytest


class TestInvalidLogin:
    @pytest.mark.parametrize("user_credentials",get_json_file("data/invalid_login_data.json"))
    def test_invalid_login(self,get_page,status_message,user_credentials,logger):
        page = get_page(LoginPage)

        logger.info(f"Starting invalid login test with data: {user_credentials['description']}")
        
        page.open_login_popup()
        logger.info("Login field opened")

        page.login_user(user_credentials)
        logger.info(f"Attempted login with invalid data: email: {user_credentials['username_or_email']} and password: {user_credentials['password']}")

        login_status = status_message[user_credentials["expected_message_key"]]
        actual_message = page.get_status_message_by_locator(login_status["locator"])
        
        if actual_message == login_status["message"]:
            logger.info(f"Expected error message displayed: {actual_message}")
        else:
            logger.error(
                f"Test failed for {user_credentials['description']} | "
                f"Expected: '{login_status['message']}', Got: '{actual_message}'"
            )


        assert actual_message == login_status["message"], f"{user_credentials['description']}: This case has failed"