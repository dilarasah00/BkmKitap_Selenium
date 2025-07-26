from pages.search_page import SearchPage
import pytest

class TestInvalidSearch:
    @pytest.mark.xfail(reason="System bug: A meaningless keyword should not return any products, but the page shows results." )
    def test_search_meaningless_input(self,get_page):
        page = get_page(SearchPage)
        page.accept_cookies()
        keyword = "şlkjhgfklş"
        page.input_product_information_and_submit(keyword)
        assert len(page.get_listed_products())==0, "Meaningless input: The product list is not empty."
    
    @pytest.mark.xfail(reason="System bug: Entering space characters should not trigger a search, but currently redirects to an empty results page.")
    def test_search_with_space_character(self,get_page,base_url):
        page = get_page(SearchPage)
        page.accept_cookies()
        keyword = "                 "
        page.input_product_information_and_submit(keyword)
        assert page.get_current_url() == base_url, "Space character input: The URL changed unexpectedly."
    
    def test_search_with_space_input_field(self,get_page,base_url):
        page = get_page(SearchPage)
        page.accept_cookies()
        keyword = ""
        page.input_product_information_and_submit(keyword)
        assert page.get_current_url() == base_url, "Empty input: The URL changed unexpectedly."