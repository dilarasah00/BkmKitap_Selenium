from pages.search_page import SearchPage
from config.get_json_file import get_json_file
import pytest

class TestSuggestion:

    test_data = get_json_file("data/suggestion_test_data.json")

    @pytest.mark.parametrize("product_information",test_data)
    def test_suggested_results_while_typing(self,get_page,product_information):
        page = get_page(SearchPage)
        page.accept_cookies()

        searching_product = product_information["product_name"]
        page.input_product_information(searching_product)
        suggestions = page.get_suggestions_list()
        assert len(suggestions) > 0 , "There aren't any suggestions."
        assert page.is_title_matching(searching_product)
    
    @pytest.mark.parametrize("product_information",test_data)
    def test_filter_while_searching(self,get_page,product_information):
        page = get_page(SearchPage)
        page.accept_cookies()
        page.ask_me_later()


        searching_product = product_information["product_name"]
        page.input_product_information(searching_product)
        
        selected_category = product_information["category"]
        page.choose_filter(selected_category)

        assert page.is_category_matching(selected_category)
        assert page.is_title_matching(searching_product)
