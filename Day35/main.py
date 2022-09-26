import requests
from Personal_Projects import API_KEYS

lat = 50.064651
lon = 19.944981

API_key = API_KEYS.OPENWEATHERMAP_API_KEY

OWN_Endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
weather_params = {
    'lat': lat,
    'lon': lon,
    'appid': API_key
}

res = requests.get(OWN_Endpoint, params=weather_params)
res.raise_for_status()

print(API_key)
print(res)
print(res.json())

