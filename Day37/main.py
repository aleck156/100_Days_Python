import requests
from Personal_Projects import API_KEYS as ak

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



graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
graphID = 'graph1'

graph_config = {
    'id': graphID,
    'name': 'cycling graph',
    'unit': 'km',
    'type': 'float',
    'color': 'ajisai'
}

pixela_headers = {
    'X-USER-TOKEN': ak.PIXELA_TOKEN
}

# response_graph = requests.post(url=graph_endpoint, json=graph_config, headers=pixela_headers)
# with open('./response_txt.html', mode='w+') as file:
#     file.write(response_graph.text)
# print(response_graph.text)

pixel_creation = f'{pixela_endpoint}{USERNAME}/graphs/{graphID}'
