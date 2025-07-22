from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,15)

    
    def wait_for_element_visible(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def wait_for_element_clickable(self,locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    def click_to_web_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def input_text(self,locator,input_text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(input_text) 
    
    def get_status_message(self,locator):
        message = self.wait.until(EC.visibility_of_element_located(locator)).text
        return message
    
    def get_current_url(self):
        return self.driver.current_url
        
    def get_text(self,locator):
        text = self.wait.until(EC.visibility_of_element_located(locator)).text
        return text
    
    def scroll_to_element(self,locator):
        element = self.wait_for_element_clickable(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    
    def accept_cookies(self,locator):
        self.click_to_web_element(locator)