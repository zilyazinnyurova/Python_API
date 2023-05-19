import requests
import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime
class TestUserRegister(BaseCase):
    def setup_method(self):
        base_part = "learnga"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        self.email = f"{base_part}{random_part}@{domain}"

    def test_create_user_successfully(self):
        data = {

            'password':'123',
            'username':'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.email
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = {

            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"

    def test_create_user_invalid_email(self):
        email = 'vinkotovexample.com'
        data = {

            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Invalid email format", f"Unexpected response content {response.content}"


    @pytest.mark.parametrize('exclude_field', ['password', 'username', 'firstName', 'lastName', 'email'])
    def test_create_user_without_parameter(self, exclude_field):
        print(exclude_field)

        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': 'vinkotov@example.com'
        }

        del data[exclude_field]
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The following required params are missed: {exclude_field}", f"Unexpected response content {response.content}"


    def test_create_user_invalid_username_one_symbol(self):
        username = 'З'
        data = {

            'password': '123',
            'username': username,
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.email
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")



    def test_create_user_invalid_username_250_symbol(self):
        username = 'DCMiNkw2Ts47b8ZEQLIxKhzYZKXcqhFXR8jUnsE9xMcPJlygF7z2kIhDZNu9hPvD62rtDB18SgteWYaf1FRqrllA6NaY1EUs55JAuw9SItdFVr18olFcttKAQYojDSIWiejSTreZlSHGgqe9a519W91z5pbOGNrAlsMCwIwb1yFaFgJn9lPmrpHVzZI8UpgtVTN0rhOWD9X2S7GHsLDPTLCVyjVDEe8ni74xpLcrsRoA5wWxsrYX7o0zagdq4do'
        data = {

            'password': '123',
            'username': username,
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.email
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        # print(response.status_code)
        # print(response.content)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'username' field is too long", f"Unexpected response content {response.content}"
