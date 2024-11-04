import time
import allure
import pytest
from random_data_generation import first_name, last_name, email, password
from settings import Urls, TestData
from pages.add_user_page import AddUserPage

@allure.title("Test Registration")
@allure.feature('user_registration')
@allure.story('Enter valid first_name, last_name, email and password')
@allure.severity('blocker')
@pytest.mark.smoke
def test_add_user_with_valid_data(browser):
    page = AddUserPage(browser, Urls.ADD_USER_URL)
    page.open()
    page.enter_first_name(first_name)
    page.enter_last_name(last_name)
    page.enter_email(email)
    page.enter_password(password)
    page.submit()
    time.sleep(3)
    assert browser.current_url == Urls.CONTACT_LIST_URL, (f"Wrong result {browser.current_url}, expected to be on "
                                                          f"Contact List page")

@allure.story('Leave first_name, last_name, email and password empty')
def test_add_user_with_empty_data(browser):
    page = AddUserPage(browser, Urls.ADD_USER_URL)
    page.open()
    page.submit()
    time.sleep(1)
    page.error_message()
    assert ("User validation failed: firstName: Path `firstName` is required., lastName: Path `lastName` is required., "
            "email: Email is invalid, password: Path `password` is required.") in page.error_message()


@allure.story('Enter valid first_name, last_name, password and invalid email')
@pytest.mark.parametrize('invalid_email', TestData.INVALID_REG_EMAILS)
def test_add_user_with_invalid_email(browser, invalid_email):
    page = AddUserPage(browser, Urls.ADD_USER_URL)
    page.open()
    page.enter_first_name(first_name)
    page.enter_last_name(last_name)
    page.enter_email(invalid_email)
    page.enter_password(password)
    page.submit()
    time.sleep(1)
    page.error_message()
    assert "User validation failed: email: Email is invalid" in page.error_message()

@allure.story('Enter valid first_name, last_name, email and invalid password')
def test_add_user_with_invalid_password(browser):
    page = AddUserPage(browser, Urls.ADD_USER_URL)
    page.open()
    page.enter_first_name(first_name)
    page.enter_last_name(last_name)
    page.enter_email(email)
    page.enter_password('111111')
    page.submit()
    time.sleep(1)
    page.error_message()
    assert ("User validation failed: password: Path `password` (`111111`) is shorter than the minimum"
            " allowed length (7).") in page.error_message()
