# from Personal_Projects/API_KEYS.py import OPENWEATHERMAP_API_KEY as API_key
from Personal_Projects import API_KEYS

lat = 50.064651
lon = 19.944981

API_key = API_KEYS.OPENWEATHERMAP_API_KEY

URL = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={API_key}'

print(URL)