import json
import pytest
from playwright.sync_api import Playwright

WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"
CITY_NAME="Jerusalem,IL"
API_KEY = "ad48510a9aed1ff96b51557d94bc5964"
UNITS = "metric"


class Test_Open_Weather_Map:

    @pytest.fixture(scope="session", autouse=True)
    def setup(self, playwright: Playwright):
        global request_context
        request_context = playwright.request.new_context(base_url=WEATHER_API_URL)
        yield
        request_context.dispose()


    def test_get_request(self):
        api_params = {
            "appid": API_KEY,
            "q": CITY_NAME,
            "units": UNITS
        }

        response = request_context.get("", params=api_params)
        result = response.json()

        print(json.dumps(result, indent=2))
        print(f"Status code: {response.status}")
        print(f"Date: {response.headers['date']}")
        print(f"Content-Type: {response.headers['content-type']}")
        assert response.status == 200
        assert "json" in response.headers["content-type"]

    def test_parsing_json(self):
        api_params = {
            "appid": API_KEY,
            "q": CITY_NAME,
            "units": UNITS
        }

        response = request_context.get("", params=api_params)
        weather_data = response.json()

        print(f"Country: {weather_data['sys']['country']}")
        print(f"Humidity: {weather_data['main']['humidity']}")
        print(f"Temperature: {weather_data['main']['temp']}")

        assert weather_data["sys"]["country"] == "IL"
