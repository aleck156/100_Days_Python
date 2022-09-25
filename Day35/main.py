import requests
from Personal_Projects import API_KEYS

lat = 50.064651
lon = 19.944981

API_key = API_KEYS.OPENWEATHERMAP_API_KEY

URL = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'

res = requests.get(URL)

print(URL)
print(res)
print(res.json())