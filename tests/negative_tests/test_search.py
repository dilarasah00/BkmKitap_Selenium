from pages.search_page import SearchPage
import pytest

class TestInvalidSearch:
    @pytest.mark.xfail(reason="System bug: A meaningless keyword should not return any products, but the page shows results." )
    def test_search_meaningless_input(self,get_page, logger):
        page = get_page(SearchPage)
        page.accept_cookies()
        keyword = "şlkjhgfklş"

        logger.info(f"Starting search with meaningless input: '{keyword}'")
        page.input_product_information_and_submit(keyword)
        
        product_count = len(page.get_listed_products())
        logger.info(f"Number of products listed: {product_count}")

        if product_count != 0:
            logger.error("Bug detected: Products are listed for meaningless input.")
        
        assert product_count==0, "Meaningless input: The product list is not empty."
    
    
    @pytest.mark.xfail(reason="System bug: Entering space characters should not trigger a search, but currently redirects to an empty results page.")
    def test_search_with_space_characters(self,get_page,base_url,logger):
        page = get_page(SearchPage)
        page.accept_cookies()
        keyword = "                 "

        logger.info("Starting search with only space characters")
        page.input_product_information_and_submit(keyword)

        current_url = page.get_current_url()
        logger.info(f"URL after search: {current_url}")

        if current_url != base_url:
            logger.error("Bug detected: Space input redirected to an empty results page")
        
        assert current_url == base_url, "Space input: The URL changed unexpectedly."
    

    def test_search_with_empty_input(self,get_page,base_url, logger):
        page = get_page(SearchPage)
        page.accept_cookies()
        keyword = ""

        logger.info("Starting search with empty input")
        page.input_product_information_and_submit(keyword)

        current_url = page.get_current_url() 
        logger.info(f"URL after search: {current_url}")

        if current_url != base_url:
            logger.warning("Unexpected behavior: Empty input triggered a redirect.")
        
        assert current_url == base_url, "Empty input: The URL changed unexpectedly."