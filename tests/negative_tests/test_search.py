from pages.search_page import SearchPage
import pytest

class TestInvalidSearch:
    @pytest.mark.xfail(reason="System bug: A meaningless keyword should not return any products, but the page shows results." )
    def test_search_meaningless_input(self,driver):
        url ="https://www.bkmkitap.com/"
        driver.get(url)
        page = SearchPage(driver)
        page.accept_cookie_before_search()
        keyword = "şlkjhgfklş"
        page.enter_product(keyword)
        assert len(page.get_listed_products())==0, "Meaningless input: The product list is not empty."
    
    @pytest.mark.xfail(reason="System bug: Entering space characters should not trigger a search, but currently redirects to an empty results page.")
    def test_search_with_space_character(self,driver):
        url ="https://www.bkmkitap.com/"
        driver.get(url)
        page = SearchPage(driver)
        page.accept_cookie_before_search()
        keyword = "                 "
        page.enter_product(keyword)
        #assert len(page.is_any_product_in_list())==0, f"{keyword} input: List includes some products"
        assert page.get_current_url() == url, "Space character input: The URL changed unexpectedly."
    
    def test_search_with_space_input_field(self,driver):
        url ="https://www.bkmkitap.com/"
        driver.get(url)
        page = SearchPage(driver)
        page.accept_cookie_before_search()
        keyword = ""
        page.enter_product(keyword)
        assert page.get_current_url() == url, "Empty input: The URL changed unexpectedly."