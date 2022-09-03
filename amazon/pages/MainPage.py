from selenium.webdriver.common.by import By

from amazon.pages.BasePage import BasePage


class MainPage(BasePage):

    sign_in_button_id = (By.ID, "nav-link-accountList")
    account_line_css = (By.CSS_SELECTOR, "[data-nav-role='signin']")

    def open_main_page(self, base_url):
        self.driver.get(base_url)
        return self

    def click_on_sign_in(self):
        self.driver.\
            find_element(*self.sign_in_button_id).\
            click()
        return self

    def should_be_logged_in(self, name):
        self.wait_until_visible(self.account_line_css)
        text = self.driver.\
            find_element(*self.account_line_css).\
            text
        assert f"Hello, {name}" in text
        return self
