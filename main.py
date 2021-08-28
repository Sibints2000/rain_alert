import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "9fcfa411c1742820ff1de86d72434f2c"

weather_params = {
    "lat":  51.759050,
    "lon":  19.458600,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    print(hour_data["weather"][0])

# print(weather_data["hourly"][0]["weather"][0]["id"])
