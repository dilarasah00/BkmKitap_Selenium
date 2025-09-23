from pages.search_page import SearchPage
from config.get_json_file import get_json_file
import pytest

class TestSuggestion:

    test_data = get_json_file("data/suggestion_test_data.json")

    @pytest.mark.parametrize("product_information", test_data)
    def test_suggested_results_while_typing(self, get_page, product_information, logger):
        page = get_page(SearchPage)
        page.accept_cookies()
        searching_product = product_information["product_name"]
        logger.info(f"Starting suggestion test while typing for product: {searching_product}")

        page.input_product_information(searching_product)
        logger.info(f"Input product information: {searching_product}")

        suggestions = page.get_suggestions_list()
        if suggestions:
            logger.info(f"Suggestions found: {suggestions}")
        else:
            logger.error("No suggestions were found.")

        assert len(suggestions) > 0, "There aren't any suggestions."
        result_title = page.is_title_matching(searching_product)
        if result_title:
            logger.info(f"Search results title matched: {searching_product}")
        else:
            logger.error(f"Search results title did not match: {searching_product}")

        assert result_title

    @pytest.mark.parametrize("product_information", test_data)
    def test_filter_while_searching(self, get_page, product_information, logger):
        page = get_page(SearchPage)
        page.accept_cookies()
        page.ask_me_later()

        searching_product = product_information["product_name"]
        logger.info(f"Starting filter while searching test for product: {searching_product}")

        page.input_product_information(searching_product)
        logger.info(f"Input product information: {searching_product}")

        selected_category = product_information["category"]
        page.choose_filter(selected_category)
        logger.info(f"Selected filter category: {selected_category}")

        result_category = page.is_category_matching(selected_category)
        result_title = page.is_title_matching(searching_product)

        if result_category and result_title:
            logger.info(f"Filter applied successfully. Category matched: {selected_category}, Title matched: {searching_product}")
        else:
            logger.error(f"Filter/search mismatch. Category matched: {result_category}, Title matched: {result_title}")

        assert result_category
        assert result_title
