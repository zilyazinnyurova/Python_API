import requests

class TestFirstAPI:
    def test_do_request(self):
        url = "https://playground.learnqa.ru/api/homework_header"
        response = requests.get(url)
        header_value = response.headers
        # print(header_value)
        assert header_value["x-secret-homework-header"] == "Some secret value"



