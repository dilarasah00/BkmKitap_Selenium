from pages.filter_page import FilterPage


class TestFilter:

    def test_filter_functionality(self,get_page):
        page = get_page(FilterPage)
        page.accept_cookies()

        keyword = "ithaki yayınları"
        page.input_product_information(keyword)
        page.select_category()
        assert page.is_category_matching()

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

        page.select_author()
        assert page.is_author_matching()