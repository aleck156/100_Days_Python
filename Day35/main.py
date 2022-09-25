import requests
from Personal_Projects import API_KEYS

lat = 50.064651
lon = 19.944981

API_key = API_KEYS.OPENWEATHERMAP_API_KEY

OWN_Endpoint = 'https://api.openweathermap.org/data/3.0/onecall'
weather_params = {
    'lat': lat,
    'lon': lon,
    'appid': API_key
}

res = requests.get(OWN_Endpoint, params=weather_params)

print(API_key)
print(res)
print(res.json())