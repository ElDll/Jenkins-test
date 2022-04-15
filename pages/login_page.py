from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert current_url == self.url, "This is wrong url"


    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        input = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        input.send_keys(email)
        input1 = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD)
        input1.send_keys(password)
        input2 = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_REPEAT)
        input2.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REFISTER_FORM_BUTTON)
        button.click()

