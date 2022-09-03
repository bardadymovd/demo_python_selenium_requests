from selenium.webdriver.common.by import By

from automatiopractice.pages.BasePage import BasePage


class MainPage(BasePage):
    base_url = "http://automationpractice.com/"

    search_field_id = (By.ID, "search_query_top")
    search_button_css = (By.CSS_SELECTOR, "[name='submit_search']")

    def open_page(self, ):
        self.driver.get(self.base_url)
        return self

    def search_item(self, text):
        self.driver. \
            find_element(*self.search_field_id). \
            send_keys(text)
        self.driver. \
            find_element(*self.search_button_css). \
            click()
        return self
