from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from .base_page import BasePage
from locators.add_user_page_locators import AddUserPageLocators


class AddUserPage(BasePage):
    def enter_first_name(self, first_name):
        self.browser.find_element(*AddUserPageLocators.FIRST_NAME).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.browser.find_element(*AddUserPageLocators.LAST_NAME).send_keys(last_name)

    def enter_email(self, email):
        self.browser.find_element(*AddUserPageLocators.EMAIL).send_keys(email)

    def enter_password(self, password):
        self.browser.find_element(*AddUserPageLocators.PASSWORD).send_keys(password)

    def submit(self):
        self.browser.find_element(*AddUserPageLocators.SUBMIT_BTN).click()

    def cancel(self):
        self.browser.find_element(*AddUserPageLocators.CANCEL_BTN).click()

    def error_message(self):
        error_message = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(AddUserPageLocators.ERROR_MESSAGE))
        return error_message.text
