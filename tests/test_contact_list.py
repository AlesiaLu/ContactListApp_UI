import time

import allure
import pytest
from random_data_generation import first_name, last_name, birthdate, email, phone, first_street_address, second_street_address, city, state_province, postal_code, country
from settings import Urls
from pages.contact_list_page import ContactListPage

@allure.title("Test Add Contact")
@allure.feature('add_contact')
@allure.story('Enter valid first and last name')
@allure.severity('blocker')
@pytest.mark.smoke
def test_add_and_delete_contact_with_required_fields(browser, login):
    page = ContactListPage(browser, Urls.CONTACT_LIST_URL)
    page.open()
    page.add_new_contact()
    page.enter_first_name(first_name)
    page.enter_last_name(last_name)
    page.submit_add_contact()
    page.check_creation_contact(first_name, last_name)
    page.delete_contact(first_name, last_name)
    time.sleep(1)
    page.check_deleting_contact(first_name, last_name)
    assert browser.current_url == Urls.CONTACT_LIST_URL

@allure.story('Enter valid data in all fields')
def test_add_and_delete_contact_with_all_fields_filled_in(browser, login):
    page = ContactListPage(browser, Urls.CONTACT_LIST_URL)
    page.open()
    page.add_new_contact()
    page.enter_first_name(first_name)
    page.enter_last_name(last_name)
    page.enter_birthdate(birthdate)
    page.enter_email(email)
    page.enter_phone(phone)
    page.enter_first_street_address(first_street_address)
    page.enter_second_street_address(second_street_address)
    page.enter_city(city)
    page.enter_state_province(state_province)
    page.enter_postal_code(postal_code)
    page.enter_country(country)
    page.submit_add_contact()
    page.check_creation_contact(first_name, last_name)
    page.delete_contact(first_name, last_name)
    time.sleep(1)
    page.check_deleting_contact(first_name, last_name)
    assert browser.current_url == Urls.CONTACT_LIST_URL

@allure.story('Leave all fields empty')
def test_add_contact_with_empty_fields(browser, login):
    page = ContactListPage(browser, Urls.CONTACT_LIST_URL)
    page.open()
    page.add_new_contact()
    page.submit_add_contact()
    time.sleep(1)
    page.error_message()
    assert "Contact validation failed: firstName: Path `firstName` is required., lastName: Path `lastName` is required." in page.error_message()

