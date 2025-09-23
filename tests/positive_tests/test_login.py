from pages.login_page import LoginPage
from config.get_json_file import get_json_file
import pytest

@pytest.fixture(scope="module")
def login_data():
    return get_json_file("data/valid_login_data.json")

class TestLogin:

    def test_successful_login_with_email(self, get_page, status_message, login_data, logger):
        page = get_page(LoginPage)
        user_credentials = login_data["valid_email_login"]
        
        logger.info(f"Starting successful login test with email: {user_credentials['username_or_email']}")

        page.open_login_popup()
        logger.info("Login popup opened")

        page.login_user(user_credentials)
        logger.info(f"Entered credentials: email={user_credentials['username_or_email']}, password={'*'*len(user_credentials['password'])}")

        login_status = status_message[user_credentials["expected_message_key"]]
        actual_message = page.get_status_message_by_locator(login_status["locator"])

        if actual_message == login_status["message"]:
            logger.info(f"Login successful. Expected message displayed: {actual_message}")
        else:
            logger.error(f"Login failed. Expected: {login_status['message']}, Got: {actual_message}")

        assert actual_message == login_status["message"], f"{user_credentials['description']}: This case has failed."

    @pytest.mark.xfail(reason="Login with username is not implemented")
    def test_successful_login_with_username(self, get_page, status_message, login_data, logger):
        page = get_page(LoginPage)
        user_credentials = login_data["valid_username_login"]

        logger.info(f"Starting login test with username: {user_credentials['username_or_email']} (expected to fail)")

        page.open_login_popup()
        logger.info("Login popup opened")

        page.login_user(user_credentials)
        logger.info(f"Entered credentials: username={user_credentials['username_or_email']}, password={'*'*len(user_credentials['password'])}")

        login_status = status_message[user_credentials["expected_message_key"]]
        actual_message = page.get_status_message_by_locator(login_status["locator"])

        logger.info(f"Actual message: {actual_message}")
        assert actual_message == login_status["message"], f"{user_credentials['description']}: This case has failed."
