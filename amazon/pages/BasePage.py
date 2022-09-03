from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    driver: WebDriver  # explicit type definition, for enable code completion in IDE

    def __init__(self, driver):
        self.driver = driver

    def wait_until_visible(self, element_locator):
        WebDriverWait(self.driver, 20). \
            until(visibility_of_element_located(element_locator))
