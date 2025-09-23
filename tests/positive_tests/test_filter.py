from pages.filter_page import FilterPage
from config.get_json_file import get_json_file
import pytest


class TestFilter:
    test_data = get_json_file("data/filter_data_for_search_input.json")

    @pytest.mark.parametrize("searh_information",test_data)
    def test_filter(self,get_page,searh_information, logger):
        page = get_page(FilterPage)
        page.accept_cookies()
        keyword = searh_information['search_input']

        logger.info(f"Starting search with {keyword}")
        page.input_product_information(keyword)

        logger.info(f"Selecting category: {searh_information['category']}")
        page.select_category(searh_information['category'])

        #assert page.is_category_matching(searh_information['category'])
        
        logger.info(f"Selecting author: {searh_information['author']}")
        page.select_author(searh_information['author'])

        assert page.is_author_matching(searh_information['author']), f"Author filter failed for {keyword}"
        logger.info("Author filter successfully applied")

        page.click_sorting_options()
        old_prices = page.get_product_price()
        page.click_increasing_option()
        page.wait_until_prices_change(old_prices)
        increasing_prices = page.get_product_price()

        logger.info(f"Ascending prices: {increasing_prices}")
        assert increasing_prices == sorted(increasing_prices), f"Ascending sort failed for {keyword}"
        logger.info("Ascending sort verified successfully")

        page.click_decreasing_option()
        page.wait_until_prices_change(increasing_prices)
        decreasing_prices = page.get_product_price()

        logger.info(f"Descending prices: {decreasing_prices}")
        assert decreasing_prices == sorted(decreasing_prices, reverse=True), f"Descending sort failed for {keyword}"
        logger.info("Descending sort verified successfully")

        logger.info(f"Filter test completed for keyword: {keyword}")