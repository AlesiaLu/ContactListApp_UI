from selenium.webdriver.common.by import By


class AddUserPageLocators:
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "email")
    PASSWORD = (By.XPATH, '//input[@id="password"]')
    SUBMIT_BTN = (By.CSS_SELECTOR, 'button[id="submit"]')
    CANCEL_BTN = (By.CSS_SELECTOR, 'button[id="cancel"]')
    ERROR_MESSAGE = (By.ID, "error")
