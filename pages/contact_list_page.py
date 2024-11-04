from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage
from locators.add_contact_page_locators import AddContactLocators
from locators.contact_list_page_locators import ContactListLocators, ContactDetailsLocators


class ContactListPage(BasePage):
    def add_new_contact(self):
        self.browser.find_element(*ContactListLocators.ADD_NEW_CONTACT_BTN).click()

    def logout(self):
        self.browser.find_element(*ContactListLocators.LOGOUT_BTN).click()

    def enter_first_name(self, first_name):
        self.browser.find_element(*AddContactLocators.FIRST_NAME).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.browser.find_element(*AddContactLocators.LAST_NAME).send_keys(last_name)

    def enter_birthdate(self, birthdate):
        self.browser.find_element(*AddContactLocators.BIRTHDATE).send_keys(birthdate)

    def enter_email(self, email):
        self.browser.find_element(*AddContactLocators.EMAIL).send_keys(email)

    def enter_phone(self, phone):
        self.browser.find_element(*AddContactLocators.PHONE).send_keys(phone)

    def enter_first_street_address(self, first_street_address):
        self.browser.find_element(*AddContactLocators.STREET_ADDRESS_1).send_keys(first_street_address)

    def enter_second_street_address(self, second_street_address):
        self.browser.find_element(*AddContactLocators.STREET_ADDRESS_2).send_keys(second_street_address)

    def enter_city(self, city):
        self.browser.find_element(*AddContactLocators.CITY).send_keys(city)

    def enter_state_province(self, state_province):
        self.browser.find_element(*AddContactLocators.STATE_PROVINCE).send_keys(state_province)

    def enter_postal_code(self, postal_code):
        self.browser.find_element(*AddContactLocators.POSTAL_CODE).send_keys(postal_code)

    def enter_country(self, country):
        self.browser.find_element(*AddContactLocators.COUNTRY).send_keys(country)

    def submit_add_contact(self):
        self.browser.find_element(*AddContactLocators.SUBMIT_BTN).click()

    def cancel(self):
        self.browser.find_element(*AddContactLocators.CANCEL_BTN).click()

    def check_creation_contact(self, first_name, last_name):
        WebDriverWait(self.browser, 10).until(
            EC.text_to_be_present_in_element(
                ContactListLocators.CREATED_NAME,
                f"{first_name} {last_name}"))

    def check_deleting_contact(self, first_name, last_name):
        WebDriverWait(self.browser, 10).until_not(
                EC.text_to_be_present_in_element(
                    ContactListLocators.CREATED_NAME,
                    f"{first_name} {last_name}"))

    def delete_contact(self, first_name, last_name):
        WebDriverWait(self.browser, 10).until(
            EC.text_to_be_present_in_element(ContactListLocators.CREATED_NAME, f"{first_name} {last_name}"))
        self.browser.find_element(*ContactListLocators.CREATED_NAME).click()
        self.browser.find_element(*ContactDetailsLocators.DELETE_CONTACT_BTN).click()
        WebDriverWait(self.browser, 10).until(EC.alert_is_present())
        alert = self.browser.switch_to.alert
        alert.accept()

    def error_message(self):
        error_message = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(AddContactLocators.ERROR_MESSAGE))
        return error_message.text
