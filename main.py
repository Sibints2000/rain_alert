import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "9fcfa411c1742820ff1de86d72434f2c"

weather_params = {
    "lat":  12.914142,
    "lon":  74.855957,
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.json()

