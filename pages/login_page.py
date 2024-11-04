from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.contact_list_page_locators import ContactListLocators
from .base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def enter_login_email(self, email):
        self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL).send_keys(email)

    def enter_login_password(self, password):
        self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD).send_keys(password)

    def submit_login(self):
        self.browser.find_element(*LoginPageLocators.SUBMIT_LOGIN_BTN).submit()

    def error_message(self):
        error_message = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(LoginPageLocators.ERROR_MESSAGE))
        return error_message.text

    def find_logout(self):
        profile = self.browser.find_element(*ContactListLocators.LOGOUT_BTN)
        return profile
