from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait

from automatiopractice import variables


class BasePage:
    driver: WebDriver  # explicit type definition, for enable code completion in IDE

    def __init__(self, driver):
        self.driver = driver

    def hover_on_element(self, element_locator):
        ActionChains(self.driver). \
            move_to_element(self.driver.find_element(*element_locator)). \
            perform()

    def wait_until_clickable(self, element_locator):
        WebDriverWait(self.driver, variables.timeout). \
            until(element_to_be_clickable(element_locator))
