from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, "email")
    LOGIN_PASSWORD = (By.XPATH, '//input[@id="password"]')
    SUBMIT_LOGIN_BTN = (By.CSS_SELECTOR, 'button[id="submit"]')
    SIGNUP_BTN = (By.CSS_SELECTOR, 'button[id="signup"]')
    ERROR_MESSAGE = (By.ID, "error")
