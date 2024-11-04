class Urls:
    BASE_URL = 'https://thinking-tester-contact-list.herokuapp.com'
    LOGIN_URL = f'{BASE_URL}/login'
    ADD_USER_URL = f'{BASE_URL}/addUser'
    CONTACT_LIST_URL = f'{BASE_URL}/contactList'


class TestData:
    VALID_EMAIL = "alesia@gmail.com"
    VALID_PASSWORD = "1111111"
    NONEXISTENT_EMAIL = "alesi@gmail.com"
    INVALID_REG_EMAILS = ['', 'example.com', 'user@', '@gmail.com', 'user@invalid_domain',
                          'user@example.c', 'us er@example.com', 'user@@example.com']

