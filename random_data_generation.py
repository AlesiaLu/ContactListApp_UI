from faker import Faker
import random
import string


fake = Faker()


def generate_first_name():
    return fake.first_name()


def generate_last_name():
    return fake.last_name()


def generate_email():
    return fake.email()


def generate_password(length=7):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


def generate_birthdate():
    return fake.date_of_birth(minimum_age=18, maximum_age=90).isoformat()


def generate_phone():
    return fake.phone_number()


def generate_first_street_address():
    return fake.street_address()


def generate_second_street_address():
    return fake.secondary_address()


def generate_city():
    return fake.city()


def generate_state_province():
    return fake.state()


def generate_postal_code():
    return fake.postcode()


def generate_country():
    return fake.country()


first_name = generate_first_name()
last_name = generate_last_name()
email = generate_email()
password = generate_password()
birthdate = generate_birthdate()
phone = generate_phone()
first_street_address = generate_first_street_address()
second_street_address = generate_second_street_address()
city = generate_city()
state_province = generate_state_province()
postal_code = generate_postal_code()
country = generate_country()

print("First Name:", first_name)
print("Last Name:", last_name)
print("Email:", email)
print("Password:", password)
print("Birthdate:", birthdate)
print("Phone:", phone)
print("First Street Address:", first_street_address)
print("Second Street Address:", second_street_address)
print("City:", city)
print("State/Province:", state_province)
print("Postal Code:", postal_code)
print("Country:", country)

