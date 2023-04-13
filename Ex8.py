import requests
import time
import json
class TestFirstAPI:
    def test_do_request(self):
        url = "https://playground.learnqa.ru/ajax/api/longtime_job"
        response = requests.get(url)
        obj_1 = json.loads(response.text)
        token_value = obj_1["token"]
        seconds_value = obj_1["seconds"]
        print(obj_1)

        data = {"token":token_value}
        response = requests.get(url, params=data)
        obj_2 = json.loads(response.text)
        assert obj_2["status"] == "Job is NOT ready"
        print(obj_2)

        time.sleep(seconds_value)
        response = requests.get(url, params=data)
        obj_3 = json.loads(response.text)
        assert obj_3["status"] == "Job is ready"
        assert "result" in obj_3
        print(obj_3)



TestFirstAPI.test_do_request("test")
