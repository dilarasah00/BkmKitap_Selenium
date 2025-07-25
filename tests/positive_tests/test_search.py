from pages.search_page import SearchPage


class TestSearch:

    def test_search_product_with_name(self,driver):
        url ="https://www.bkmkitap.com/"
        driver.get(url)
        page = SearchPage(driver)
        page.accept_cookie_before_search()
        keyword= "kalem"
        page.enter_product(keyword)
        assert page.is_title_matching(keyword)
    
    def test_search_with_brand(self,driver):
        url ="https://www.bkmkitap.com/"
        driver.get(url)
        page = SearchPage(driver)
        page.accept_cookie_before_search()
        keyword= "Faber-Castell"
        page.enter_product(keyword)
        assert page.is_brand_matching(keyword)
    
    def test_search_with_name_and_brand(self,driver):
        url ="https://www.bkmkitap.com/"
        driver.get(url)
        page = SearchPage(driver)
        page.accept_cookie_before_search()
        keyword_title = "keçeli kalem"
        keyword_brand = "Faber-Castell"
        keyword= keyword_brand+" "+keyword_title
        page.enter_product(keyword)
        assert page.is_title_matching(keyword_title)
        assert page.is_brand_matching(keyword_brand)
