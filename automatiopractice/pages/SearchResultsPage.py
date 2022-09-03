from selenium.webdriver.common.by import By

from automatiopractice.pages.BasePage import BasePage


class SearchResultsPage(BasePage):
    product_items_css = (By.CSS_SELECTOR, ".product-container")
    product_name_css = (By.CSS_SELECTOR, ".product-name")
    product_price_css = (By.CSS_SELECTOR, ".price")
    product_view_button_css = (By.CSS_SELECTOR, ".button[title='View']")

    def get_name_of_first_item(self, ):
        return self.driver. \
            find_element(*self.product_items_css). \
            find_element(*self.product_name_css). \
            text.strip()

    def get_price_of_first_item(self):
        return self.driver. \
            find_element(*self.product_items_css). \
            find_element(*self.product_price_css). \
            get_attribute('textContent').strip()

    def open_fist_item_details(self):
        self.hover_on_element(self.product_items_css)
        self.driver. \
            find_element(*self.product_items_css). \
            find_element(*self.product_view_button_css). \
            click()
        return self
