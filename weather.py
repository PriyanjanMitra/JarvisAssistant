import datetime as dt
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "6143db6b8b102b44ab3e0b1a866d2443"
CITY = "New Delhi"
url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()


def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius


temp_kelvin = response['main']['temp']
temp_celsius = kelvin_to_celsius(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius = kelvin_to_celsius(feels_like_kelvin)
temp_min_kelvin = response['main']['temp_min']
temp_min_celsius = kelvin_to_celsius(temp_min_kelvin)
temp_max_kelvin = response['main']['temp_max']
temp_max_celsius = kelvin_to_celsius(temp_max_kelvin)
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
wind_speed = response['wind']['speed']
