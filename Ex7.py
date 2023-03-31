import requests


def do_request_without_params(method="HEAD"):
    if method == "GET":
        response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
    elif method == "POST":
        response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type")
    elif method == "DELETE":
        response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type")
    elif method == "PUT":
        response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type")
    else:
        response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
    print(response.status_code)
    print(response.text)


do_request_without_params("GET")
do_request_without_params("POST")
do_request_without_params("DELETE")
do_request_without_params("PUT")
do_request_without_params()


print("================")

def do_request_with_params(method):
    if method == "GET":
        response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": "GET"})
    elif method == "POST":
        response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "POST"})
    elif method == "DELETE":
        response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "DELETE"})
    elif method == "PUT":
        response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "PUT"})
    print(response.status_code)
    print(response.text)


do_request_with_params("GET")
do_request_with_params("POST")
do_request_with_params("DELETE")
do_request_with_params("PUT")


print("================")

def do_request_with_params(methods):
    for current_method in methods:
        print(current_method)
        response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": current_method})
        print(response.status_code)
        print(response.text)
    print("-------------")
    for current_method in methods:
        print(current_method)
        response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": current_method})
        print(response.status_code)
        print(response.text)
    print("-------------")
    for current_method in methods:
        print(current_method)
        response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": current_method})
        print(response.status_code)
        print(response.text)
    print("-------------")
    for current_method in methods:
        print(current_method)
        response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": current_method})
        print(response.status_code)
        print(response.text)

do_request_with_params(["GET","PUT","DELETE","POST"])

