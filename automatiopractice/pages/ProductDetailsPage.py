from selenium.webdriver.common.by import By

from automatiopractice.pages.BasePage import BasePage


class ProductDetailsPage(BasePage):
    product_name_css = (By.CSS_SELECTOR, "[itemprop='name']")
    product_price_css = (By.CSS_SELECTOR, "[itemprop='price']")
    add_to_cart_button = (By.CSS_SELECTOR, "#add_to_cart button")
    proceed_to_checkout_button = (By.CSS_SELECTOR, "[title='Proceed to checkout']")

    def verify_product_name(self, expected_name):
        name = self.driver. \
            find_element(*self.product_name_css). \
            text.strip()
        assert name == expected_name
        return self

    def verify_product_price(self, expected_price):
        price = self.driver. \
            find_element(*self.product_price_css). \
            text.strip()
        assert price == expected_price
        return self

    def add_to_cart(self):
        self.driver. \
            find_element(*self.add_to_cart_button). \
            click()
        return self

    def proceed_to_checkout(self):
        self.wait_until_clickable(self.proceed_to_checkout_button)
        self.driver. \
            find_element(*self.proceed_to_checkout_button). \
            click()
        return self
