import time
import pytest
from settings import Urls, TestData
from pages.login_page import LoginPage
import allure
from allure_commons.types import AttachmentType

@allure.title("Test Authentication")
@allure.feature('user_login')
@allure.story('Enter valid email and password')
@allure.severity('blocker')
@pytest.mark.smoke
def test_login_with_valid_data(browser):
    page = LoginPage(browser, Urls.LOGIN_URL)
    page.open()
    page.enter_login_email(TestData.VALID_EMAIL)
    page.enter_login_password(TestData.VALID_PASSWORD)
    page.submit_login()
    time.sleep(1)
    with allure.step('Make screenshot'):
        allure.attach(browser.get_screenshot_as_png(), name='result1', attachment_type=AttachmentType.PNG)
    assert page.find_logout()
    assert browser.current_url == Urls.CONTACT_LIST_URL, (f"Wrong result {browser.current_url}, expected to be on "
                                                          f"Contact List page")

@allure.story('Leave email and password empty')
def test_login_with_empty_data(browser):
    page = LoginPage(browser, Urls.LOGIN_URL)
    page.open()
    page.submit_login()
    time.sleep(1)
    page.error_message()
    assert "Incorrect username or password" in page.error_message()

@allure.story('Enter nonexistent email and valid password')
def test_login_with_nonexistent_data(browser):
    page = LoginPage(browser, Urls.LOGIN_URL)
    page.open()
    page.enter_login_email(TestData.NONEXISTENT_EMAIL)
    page.enter_login_password(TestData.VALID_PASSWORD)
    page.submit_login()
    time.sleep(1)
    page.error_message()
    assert "Incorrect username or password" in page.error_message()
