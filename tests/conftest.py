import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from settings import Urls, TestData


@pytest.fixture(autouse=True)
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture()
def login(browser):
    page = LoginPage(browser, Urls.LOGIN_URL)
    page.open()
    page.enter_login_email(TestData.VALID_EMAIL)
    page.enter_login_password(TestData.VALID_PASSWORD)
    page.submit_login()
