from pages.base_page import BasePage
import config.util as ru
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    def navigate_to_the_login(self):
        self.click_to_web_element((By.ID,ru.login_nav_button_locator))
    
    def enter_email_or_username(self,email_or_username):
        self.input_text((By.ID,ru.email_input_locator),email_or_username)
    
    def enter_password(self,password):
        self.input_text((By.ID,ru.password_input_locator),password)
    
    def click_login_button(self):
        self.click_to_web_element((By.ID,ru.login_button_locator))
    
    def click_forgot_password_link(self):
        self.click_to_web_element((By.ID,ru.forgot_password_link_locator))
    
    def click_facebook_button(self):
        self.click_to_web_element((By.ID,ru.facebook_login_button_locator))
    
    def click_google_button(self):
        self.click_to_web_element((By.ID,ru.google_login_button_locator))
    
    def click_apple_button(self):
        self.click_to_web_element((By.CSS_SELECTOR,ru.apple_login_button_locator))

    def enter_email_for_password_change(self,email):
        self.input_text((By.CLASS_NAME,ru.forgot_email_input_locator),email)
    
    
    def click_send_reset_email_button(self):
        self.click_to_web_element((By.ID,ru.forgot_password_submit_button_locator))
    
    
    def get_status_message_by_locator(self,locator):
        return self.get_status_message((By.CSS_SELECTOR,locator))
    
    def login_accept_cookie(self):
        self.accept_cookies((By.XPATH,ru.cookie_accept_button_xpath))

    
    def open_login_popup(self):
        self.login_accept_cookie()
        self.navigate_to_the_login()
    
    def login_user(self,credentials):
        self.enter_email_or_username(credentials["username_or_email"])
        self.enter_password(credentials["password"])
        self.click_login_button()