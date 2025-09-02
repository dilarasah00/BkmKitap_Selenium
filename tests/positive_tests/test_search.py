from pages.search_page import SearchPage
import pytest
from config.get_json_file import get_json_file


class TestSearch:

    test_data = get_json_file("data/search_data.json")

    @pytest.mark.parametrize("product_information",test_data)
    def test_search_product_with_name(self,get_page,product_information):
        page = get_page(SearchPage)
        page.accept_cookies()
        keyword= product_information["product_name"]
        page.input_product_information_and_submit(keyword)
        assert page.is_title_matching(keyword)
    
    @pytest.mark.parametrize("product_information",test_data)
    def test_search_with_brand(self,get_page,product_information):
        page = get_page(SearchPage)
        page.accept_cookies()
        keyword= product_information["brand"]
        page.input_product_information_and_submit(keyword)
        assert page.is_brand_matching(keyword)

    @pytest.mark.parametrize("product_information",test_data)
    def test_search_with_name_and_brand(self,get_page,product_information):
        page = get_page(SearchPage)
        page.accept_cookies()
        keyword_title = product_information["product_name"]
        keyword_brand = product_information["brand"]
        keyword= keyword_brand+" "+keyword_title
        page.input_product_information_and_submit(keyword)
        assert page.is_title_matching(keyword_title)
        assert page.is_brand_matching(keyword_brand)
