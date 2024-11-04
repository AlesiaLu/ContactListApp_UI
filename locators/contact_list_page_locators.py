from selenium.webdriver.common.by import By


class ContactListLocators:
    ADD_NEW_CONTACT_BTN = (By.ID, "add-contact")
    LOGOUT_BTN = (By.ID, "logout")
    CREATED_NAME = (By.XPATH, '//*[@id="myTable"]/tr[1]/td[2]')


class ContactDetailsLocators:
    DELETE_CONTACT_BTN = (By.ID, "delete")
