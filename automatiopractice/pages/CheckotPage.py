from selenium.webdriver.common.by import By

from automatiopractice.pages.BasePage import BasePage


class CheckoutPage(BasePage):
    product_name = (By.CSS_SELECTOR, "#cart_summary .product-name")
    total_price = (By.CSS_SELECTOR, "#total_product")

    def verify_product_name(self, expected_name):
        name = self.driver. \
            find_element(*self.product_name). \
            text.strip()
        assert name == expected_name
        return self

    def verify_product_price(self, expected_price):
        price = self.driver. \
            find_element(*self.total_price). \
            text.strip()
        assert price == expected_price
        return self
