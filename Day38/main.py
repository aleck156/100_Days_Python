import requests
import datetime as dt
from Personal_Projects import API_KEYS as ak


API_KEY = ak.NUTRITIONIX_API_KEY
APP_ID = ak.NUTRITIONIX_APP_ID

SITE_ENDPOINT = 'https://trackapi.nutritionix.com'
EXERCISE_ENDPOINT = '/v2/natural/exercise'

app_headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'x-remote-user-id': 'railgun6969',
    'Content-Type': 'application/json'
}

message = {
    'query': 'walked 15 km',
    'gender': 'male',
    'weight_kg': 67,
    'height_cm': 172,
    'age': 36
}


response = requests.post(url=f'{SITE_ENDPOINT}{EXERCISE_ENDPOINT}', headers=app_headers, json=message)
response.raise_for_status()
data = response.json()['exercises'][0]
print(data)

current_date = dt.datetime.now().strftime('%d/%m/%Y')
exercise_type = data['name']
exercise_duration = data['duration_min']
calories_burned = data['nf_calories']

# SHEETLY
SHEETLY_ENDPOINT = 'https://api.sheety.co/'
SHEETLY_USERNAME = ''
SHEETLY_GET = ak.SHEETLY_GET
SHEETLY_POST =  ak.SHEETLY_POST
workouts = {
    'workouts': {
        'date': current_date,
        'time': exercise_duration,
        'exercises': exercise_type,
        'duration': exercise_duration,
        'calories': calories_burned
    }
}


sheetly_post_res = requests.post(url=SHEETLY_POST, json=workouts)
sheetly_post_res.raise_for_status()
print(sheetly_post_res)
# print(workouts)

# sheetly_res = requests.get(url=SHEETLY_GET)
# print(sheetly_res.text)

# Date	Time	Exercise	Duration	Calories