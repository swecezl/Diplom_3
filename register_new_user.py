import requests
import random
import string
from faker import Faker

faker = Faker()


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def register_new_user_return_login_pass_and_response():
    login_pass = []

    email = faker.free_email()
    password = generate_random_string(5)
    name = faker.first_name()

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    response = requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', data=payload)

    if response.status_code == 200:
        login_pass.append(email)
        login_pass.append(password)
        login_pass.append(name)

    return login_pass, response