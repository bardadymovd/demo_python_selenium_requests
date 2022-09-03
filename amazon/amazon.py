import pytest
from selenium import webdriver
import configparser

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


from amazon.pages.LoginPage import LoginPage
from amazon.pages.MainPage import MainPage

config = configparser.ConfigParser()
config.read('config.ini')
config = config.defaults()


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(15)
    yield driver
    driver.close()


def test_01_amazon_login(driver):
    login_page = LoginPage(driver)
    main_page = MainPage(driver)

    main_page.\
        open_main_page(config["base_url"]).\
        click_on_sign_in()
    login_page.\
        input_login(config["username"]).\
        input_password(config["password"])
    main_page.\
        should_be_logged_in(config["first_name"])
