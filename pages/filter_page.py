from pages.base_page import BasePage
import config.util as ru
from selenium.webdriver.common.by import By
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException


class FilterPage(BasePage):

    def input_product_information(self,product_information):
        self.input_text_and_submit((By.ID,ru.search_input_locator),product_information)

    def select_category(self):
        self.click_to_web_element((By.XPATH,ru.child_books_option_locator))
    
    def select_author(self):
        self.click_to_web_element((By.XPATH,ru.author_option_locator))
    
    def click_sorting_options(self):
        self.click_to_web_element((By.CLASS_NAME,ru.sorting_options_locator))
    
    def click_decreasing_option(self):
        self.click_to_web_element((By.CSS_SELECTOR,ru.pu_value_locator))
    
    def click_increasing_option(self):
        self.click_to_web_element((By.CSS_SELECTOR,ru.up_value_locator))
    
    def get_products(self):
        products= self.wait_for_elements_visible((By.CLASS_NAME,ru.product_item_locator))
        return products
    

    def get_product_price(self):
        prices = []
        price_list = self.get_product_subinfo(self.get_products,By.CLASS_NAME,ru.product_price_locator)
        for price in price_list:
            price = price.replace(".", "").replace(",", ".").strip()
            price_f = re.sub(r"[^\d.]", "", price)
            prices.append(float(price_f))
        return prices

    def get_product_category(self):
        return self.get_product_subinfo(self.get_products,By.XPATH,ru.product_brand_locator)
    
    def get_product_author(self):
        return self.get_product_subinfo(self.get_products, By.XPATH,ru.author_locator)
    
    def is_category_matching(self):
        return self.all_values_match(self.get_product_category, "İthaki Çocuk Yayınları")
    
    def is_author_matching(self):
        return self.all_values_match(self.get_product_author, "James Foley")
        
    
    def wait_until_prices_change(self, previous_prices):
        def price_changed(driver):
            try:
                return self.get_product_price() != previous_prices
            except StaleElementReferenceException:
                return False
            
        WebDriverWait(self.driver, 15).until(price_changed)
