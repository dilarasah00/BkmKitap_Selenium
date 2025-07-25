from pages.search_page import SearchPage

class TestSuggestion:

    def test_suggested_results_while_typing(self,driver):
        url ="https://www.bkmkitap.com/"
        driver.get(url)
        page = SearchPage(driver)
        page.accept_cookie_before_search()

        keyword = "rüzgar"
        page.enter_product_information(keyword)
        suggestions = page.get_suggestions_list()
        assert len(suggestions) > 0 , "There aren't any suggestions."
        assert page.is_title_matching(keyword)
    
    def test_filter_while_searching(self,driver):
        url ="https://www.bkmkitap.com/"
        driver.get(url)
        page = SearchPage(driver)
        page.accept_cookie_before_search()
        page.ask_me_later()


        keyword = "rüzgar"
        page.enter_product_information(keyword)
        page.choose_filter()

        assert page.is_category_matching()
        assert page.is_title_matching(keyword)

        