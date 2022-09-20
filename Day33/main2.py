import requests

res = requests.get(url='http://api.open-notify.org/iss-now.json')
res.raise_for_status()

data = res.json()

longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']

iss_position = (longitude, latitude)
print(iss_position)

# if res.status_code == 400:
#     raise Exception('That resource does not exist')
# elif res.status_code == 401:
#     raise Exception('Yout are not authorized to access this data')