import requests
import json

def test_postman_api():
    url = "https://postman-echo.com/post"
    data = {
        "name": "Tester",
        "role": "QA"
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, data=json.dumps(data), headers=headers)

    assert response.status_code == 200
    response_data = response.json()["data"]
    assert json.loads(response_data) == data

def test_status_code():
    url = "https://postman-echo.com/post"
    data = {
        "name": "Tester",
        "role": "QA"
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, data=json.dumps(data), headers=headers)

    assert response.status_code == 200

def test_response_body():
    url = "https://postman-echo.com/post"
    data = {
        "name": "Tester",
        "role": "QA"
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, data=json.dumps(data), headers=headers)

    response_data = response.json()["data"]
    assert json.loads(response_data) == data
