from pages.search_page import SearchPage


class TestSearch:

    def test_search_product_with_name(self,get_page):
        page = get_page(SearchPage)
        page.accept_cookies()
        keyword= "kalem"
        page.input_product_information_and_submit(keyword)
        assert page.is_title_matching(keyword)
    
    def test_search_with_brand(self,get_page):
        page = get_page(SearchPage)
        page.accept_cookies()
        keyword= "Faber-Castell"
        page.input_product_information_and_submit(keyword)
        assert page.is_brand_matching(keyword)
    
    def test_search_with_name_and_brand(self,get_page):
        page = get_page(SearchPage)
        page.accept_cookies()
        keyword_title = "keçeli kalem"
        keyword_brand = "Faber-Castell"
        keyword= keyword_brand+" "+keyword_title
        page.input_product_information_and_submit(keyword)
        assert page.is_title_matching(keyword_title)
        assert page.is_brand_matching(keyword_brand)
