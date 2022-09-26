import datetime

import requests
from Personal_Projects import API_KEYS

lat = 50.064651
lon = 19.944981

API_key = API_KEYS.OPENWEATHERMAP_API_KEY

# OWN_Endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
# weather_params = {
#     'lat': lat,
#     'lon': lon,
#     'appid': API_key,
#     'exclude': 'current,minutely,daily'
# }
#
# res = requests.get(OWN_Endpoint, params=weather_params)
# res.raise_for_status()
#
# weather_data = res.json()
# weather_slice = weather_data["hourly"][:12]
# for hour_data in weather_slice:
#     print(hour_data['weather'])
#
# print(API_key)
# print(res)
# print(res.json())

# http://api.openweathermap.org/data/2.5/forecast?lat=50.064651&lon=19.944981&appid=
OWM_Endpoint = f'http://api.openweathermap.org/data/2.5/forecast'
weather_params = {
    'lat': lat,
    'lon': lon,
    'appid': API_key
}

res = requests.get(OWM_Endpoint, params=weather_params)
res.raise_for_status()
data_set = res.json()['list']

for data_piece in data_set:
    # print(data_piece)
    extract_time =datetime.datetime.fromtimestamp(data_piece['dt'])
    main = data_piece['weather'][0]['main']
    description = data_piece['weather'][0]['description']
    condition_code = data_piece['weather'][0]['id']
    print(f'[{extract_time}]:\t{condition_code}\t{main}\t{description}')