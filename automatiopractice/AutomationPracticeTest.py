import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from automatiopractice import variables
from automatiopractice.pages.CheckotPage import CheckoutPage
from automatiopractice.pages.MainPage import MainPage
from automatiopractice.pages.ProductDetailsPage import ProductDetailsPage
from automatiopractice.pages.SearchResultsPage import SearchResultsPage


@pytest.fixture(scope="module")
def driver():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.implicitly_wait(variables.timeout)
    yield browser
    browser.close()


def test_01_add_to_cart(driver):
    main_page = MainPage(driver)
    search_results_page = SearchResultsPage(driver)
    product_details_page = ProductDetailsPage(driver)
    checkout_page = CheckoutPage(driver)

    main_page. \
        open_page(). \
        search_item("dress")

    name = search_results_page.get_name_of_first_item()
    price = search_results_page.get_price_of_first_item()
    assert "dress" in name.lower()
    search_results_page.open_fist_item_details()

    product_details_page. \
        verify_product_name(name). \
        verify_product_price(price)

    product_details_page. \
        add_to_cart(). \
        proceed_to_checkout()

    checkout_page. \
        verify_product_name(name). \
        verify_product_price(price)
