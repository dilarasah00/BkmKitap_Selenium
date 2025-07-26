from pages.search_page import SearchPage

class TestSuggestion:

    def test_suggested_results_while_typing(self,get_page):
        page = get_page(SearchPage)
        page.accept_cookies()

        keyword = "rüzgar"
        page.input_product_information(keyword)
        suggestions = page.get_suggestions_list()
        assert len(suggestions) > 0 , "There aren't any suggestions."
        assert page.is_title_matching(keyword)
    
    def test_filter_while_searching(self,get_page):
        page = get_page(SearchPage)
        page.accept_cookies()
        page.ask_me_later()


        keyword = "rüzgar"
        page.input_product_information(keyword)
        page.choose_filter()

        assert page.is_category_matching()
        assert page.is_title_matching(keyword)

        