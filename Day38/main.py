import requests
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
print(response.json())