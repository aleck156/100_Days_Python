import requests
from Personal_Projects import API_KEYS as ak
from datetime import datetime as dt

pixela_endpoint = 'https://pixe.la/v1/users/'

USERNAME = 'railgun6969'

endpoint_params = {
    'token':        ak.PIXELA_TOKEN,
    'username':     USERNAME,
    'agreeTermsOfService':
                    "yes",
    'notMinor':     "yes"
}

# response = requests.post(url=pixela_endpoint, json=endpoint_params)
# print(response.text)
# with open('./response_create_user.html', mode='w+') as file:
#     file.write(response.text)



graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/'
graphID = 'graph1'

graph_config = {
    'id': graphID,
    'name': 'cycling_graph',
    'unit': 'km',
    'type': 'float',
    'color': 'ajisai'
}

pixela_headers = {
    'X-USER-TOKEN': ak.PIXELA_TOKEN
}

response_graph = requests.post(url=graph_endpoint, json=graph_config, headers=pixela_headers)
print(response_graph.text)
# with open('./response_txt.html', mode='w+') as file:
#     file.write(response_graph.text)

pixel_creation = f'{pixela_endpoint}/{USERNAME}/graphs/{graphID}'

print(pixel_creation)

pixel_data = {
    'date':         dt.now().strftime('%Y%m%d'),
    'quantity':     '9.74',
}


response_pixel_creation = requests.post(url=pixel_creation, json=pixel_data, headers=pixela_headers)
print(response_pixel_creation.text)


# f'{dt.now().year}{dt.now().month}{dt.now().day:02d}'