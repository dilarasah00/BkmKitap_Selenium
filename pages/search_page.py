from pages.base_page import BasePage
import config.util as ru
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class SearchPage(BasePage):

    def input_product_information_and_submit(self,product_information):  
        self.input_text_and_submit((By.ID,ru.search_input_locator),product_information)
    
    def input_product_information(self,product_information):  
        self.input_text((By.ID,ru.search_input_locator),product_information)
    
    def choose_filter(self):
        self.click_to_web_element((By.XPATH,ru.child_book_locator))

    def get_top10_products(self):
        products= self.wait_for_elements_visible((By.CLASS_NAME,ru.product_detail_locator))
        top10_products = products[:10]
        return top10_products
    
    def get_product_titles(self):
        return self.get_product_subinfo(self.get_top10_products,By.CLASS_NAME,ru.product_title_locator)
        
    def get_product_brands(self):
        return self.get_product_subinfo(self.get_top10_products,By.XPATH,ru.product_brand_locator)
    
    def get_product_category(self):
        return self.get_product_subinfo(self.get_top10_products,By.CLASS_NAME,ru.product_category_locator)
    
    def is_title_matching(self, keyword):
        return self.all_values_match(self.get_product_titles,keyword)
    
    def is_brand_matching(self, keyword):
        return self.all_values_match(self.get_product_brands,keyword)
    
    def is_category_matching(self):
        return self.all_values_match(self.get_product_category, "Çocuk Kitapları")
       
    def get_listed_products(self):
        try:
            products = self.wait_for_elements_visible((By.ID,ru.product_list_locator))
            return products
        except TimeoutException:
            return [] 
        
    def get_suggestions_list(self):
        try:
            return self.wait_for_elements_visible((By.CLASS_NAME,ru.suggestions_list_locator))
        except TimeoutException:
            return []
    
    def ask_me_later(self):
        self.click_to_web_element((By.XPATH,ru.desktop_chosen_locator))
