from selenium.webdriver.common.by import By


class AddContactLocators:
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    BIRTHDATE = (By.ID, "birthdate")
    EMAIL = (By.ID, "email")
    PHONE = (By.ID, "phone")
    STREET_ADDRESS_1 = (By.ID, "street1")
    STREET_ADDRESS_2 = (By.ID, "street2")
    CITY = (By.ID, "city")
    STATE_PROVINCE = (By.ID, "stateProvince")
    POSTAL_CODE = (By.ID, "postalCode")
    COUNTRY = (By.ID, "country")
    SUBMIT_BTN = (By.ID, "submit")
    CANCEL_BTN = (By.ID, "cancel")
    ERROR_MESSAGE = (By.XPATH, '//span[@id="error"]')
