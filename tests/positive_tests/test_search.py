from pages.search_page import SearchPage
import pytest
from config.get_json_file import get_json_file

class TestSearch:

    test_data = get_json_file("data/search_data.json")

    @pytest.mark.parametrize("product_information", test_data)
    def test_search_product_with_name(self, get_page, product_information, logger):
        page = get_page(SearchPage)
        page.accept_cookies()
        keyword = product_information["product_name"]
        logger.info(f"Starting search test with product name: {keyword}")

        page.input_product_information_and_submit(keyword)
        logger.info(f"Submitted search keyword: {keyword}")

        result = page.is_title_matching(keyword)
        if result:
            logger.info(f"Search results correctly matched the product name: {keyword}")
        else:
            logger.error(f"Search results did not match the product name: {keyword}")
        
        assert result

    @pytest.mark.parametrize("product_information", test_data)
    def test_search_with_brand(self, get_page, product_information, logger):
        page = get_page(SearchPage)
        page.accept_cookies()
        keyword = product_information["brand"]
        logger.info(f"Starting search test with brand: {keyword}")

        page.input_product_information_and_submit(keyword)
        logger.info(f"Submitted search keyword: {keyword}")

        result = page.is_brand_matching(keyword)
        if result:
            logger.info(f"Search results correctly matched the brand: {keyword}")
        else:
            logger.error(f"Search results did not match the brand: {keyword}")
        
        assert result

    @pytest.mark.parametrize("product_information", test_data)
    def test_search_with_name_and_brand(self, get_page, product_information, logger):
        page = get_page(SearchPage)
        page.accept_cookies()
        keyword_title = product_information["product_name"]
        keyword_brand = product_information["brand"]
        keyword = f"{keyword_brand} {keyword_title}"
        logger.info(f"Starting search test with combined brand and product name: {keyword}")

        page.input_product_information_and_submit(keyword)
        logger.info(f"Submitted search keyword: {keyword}")

        result_title = page.is_title_matching(keyword_title)
        result_brand = page.is_brand_matching(keyword_brand)

        if result_title and result_brand:
            logger.info(f"Search results correctly matched title: {keyword_title} and brand: {keyword_brand}")
        else:
            logger.error(f"Search results mismatch. Title match: {result_title}, Brand match: {result_brand}")

        assert result_title
        assert result_brand
