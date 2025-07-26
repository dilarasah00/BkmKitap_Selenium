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
        titles = []
        for product in self.get_top10_products():
            title = product.find_element(By.CLASS_NAME,ru.product_title_locator)
            titles.append(title.text)
        print("Top 10 headlines:", titles)
        return titles
        
    def get_product_brands(self):
        brands = []
        for product in self.get_top10_products():
            brand = product.find_element(By.XPATH,ru.product_brand_locator)
            brands.append(brand.text)
        print("Top 10 headlines:", brands)
        return brands
    
    def get_product_category(self):
        categorys = []
        for product in self.get_top10_products():
            category = product.find_element(By.CLASS_NAME,ru.product_category_locator)
            categorys.append(category.text)
        print("Top 10 categories:", category)
        return categorys
    
    def is_title_matching(self, keyword):
        titles = self.get_product_titles()
        for title in titles:
            if keyword.lower() not in title.lower():
                return False
        return True
    
    def is_brand_matching(self, keyword):
        brands = self.get_product_brands()
        for brand in brands:
            if keyword.lower() not in brand.lower():
                return False
        return True
    
    def is_category_matching(self):
        categorys = self.get_product_category()
        for category in categorys:
            if category != "Çocuk Kitapları":
                return False
        return True

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
