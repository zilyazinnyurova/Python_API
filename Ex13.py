import requests
import json
import pytest

class TestUserAgent:
    data_provider = [
        {
            "user_agent": "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
            "expected_responses": {
                "platform": "Mobile",
                "browser": "No",
                "device": "Android"
            }
        },
        {
            "user_agent": "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1",
            "expected_responses": {
                "platform": "Mobile",
                "browser": "No",
                "device": "iOS"
            }
        },
        {
            "user_agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
            "expected_responses": {
                "platform": "Googlebot",
                "browser": "Unknown",
                "device": "Unknown"
            }
        },
        {
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0",
            "expected_responses": {
                "platform": "Web",
                "browser": "Chrome",
                "device": "No"
            }
        },
        {
            "user_agent": "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
            "expected_responses": {
                "platform": "Mobile",
                "browser": "No",
                "device": "iPhone"
            }
        }
    ]

    @pytest.mark.parametrize('data_provider', data_provider)
    def test_check_1(self, data_provider):
        response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check", headers={"User-Agent": data_provider["user_agent"]})
        value = json.loads(response.text)
        assert value["platform"] == data_provider["expected_responses"]["platform"]
        assert value["browser"] == data_provider["expected_responses"]["browser"]
        assert value["device"] == data_provider["expected_responses"]["device"]

