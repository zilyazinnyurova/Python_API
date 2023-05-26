import requests

response = requests.post("https://playground.learnqa.ru/api/check_type")
print(response.text)
