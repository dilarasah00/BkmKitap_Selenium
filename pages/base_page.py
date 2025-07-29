from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from config.util import cookie_accept_button_xpath

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,15)


    def wait_for_element_visible(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def wait_for_elements_visible(self,locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))
    
    
    def click_to_web_element(self, locator):  
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def input_text(self,locator,text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text) 
    
    def input_text_and_submit(self,locator,text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text + Keys.ENTER)

    
    def get_status_message(self,locator): 
        message = self.wait.until(EC.visibility_of_element_located(locator)).text
        return message
    
    def get_current_url(self):
        return self.driver.current_url
    
    def scroll_to_element(self,locator):
        element = self.wait_for_element_clickable(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    
    def accept_cookies(self): 
        try:
            self.click_to_web_element((By.XPATH,cookie_accept_button_xpath))
        except NoSuchElementException:
            pass
    
    def get_product_subinfo(self,getter_function, by_type, locator):
        values = []
        for product in getter_function():
            try:
                el = product.find_element(by_type, locator)
                values.append(el.text)
            except Exception as e:
                print( f"Element not found: {e}")
        return values
    
    def all_values_match(self,getter_function,keyword):
        elements = getter_function()
        for element in elements:
            if keyword.lower() not in element.lower():
                return False
        return True