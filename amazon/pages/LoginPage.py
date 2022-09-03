import time

from selenium.webdriver.common.by import By

from amazon.pages.BasePage import BasePage


class LoginPage(BasePage):

    login_field_id = (By.ID, "ap_email")
    continue_button_id = (By.ID, "continue")
    password_field_id = (By.ID, "ap_password")
    sign_in_button_id = (By.ID, "signInSubmit")

    def input_login(self, login):
        self.driver.\
            find_element(*self.login_field_id).\
            send_keys(login)
        self.driver.\
            find_element(*self.continue_button_id).\
            click()
        return self

    def input_password(self, password):
        time.sleep(5)   # add sleep for bypass captcha
        self.driver.\
            find_element(*self.password_field_id).\
            send_keys(password)
        self.driver.\
            find_element(*self.sign_in_button_id).\
            click()
        return self


