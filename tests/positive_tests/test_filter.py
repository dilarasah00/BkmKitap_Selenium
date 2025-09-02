from pages.filter_page import FilterPage
from config.get_json_file import get_json_file
import pytest


class TestFilter:
    test_data = get_json_file("data/filter_data_for_search_input.json")

    @pytest.mark.parametrize("searh_information",test_data)
    def test_filter(self,get_page,searh_information):
        page = get_page(FilterPage)
        page.accept_cookies()

        keyword = searh_information['search_input']
        page.input_product_information(keyword)
        page.select_category(searh_information['category'])
        #assert page.is_category_matching(searh_information['category'])
        
        page.select_author(searh_information['author'])
        assert page.is_author_matching(searh_information['author'])

        page.click_sorting_options()
        old_prices = page.get_product_price()
        page.click_increasing_option()
        page.wait_until_prices_change(old_prices)

        increasing_prices = page.get_product_price()
        assert increasing_prices == sorted(increasing_prices)

        page.click_decreasing_option()
        page.wait_until_prices_change(increasing_prices)

        decreasing_prices = page.get_product_price()
        assert decreasing_prices == sorted(decreasing_prices, reverse=True)