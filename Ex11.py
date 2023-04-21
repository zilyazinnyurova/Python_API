import requests

class TestFirstAPI:
    def test_do_request(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"
        response = requests.get(url)
        cookie_value = response.cookies
        print(cookie_value)
        assert cookie_value["HomeWork"] == "hw_value"



