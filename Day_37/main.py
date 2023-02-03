import requests
from datetime import datetime

## TODO: Create your user account
pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token' : 'm1a4r2c9efs',
    'username' : 'marceds',
    'agreeTermsOfService' : 'yes',
    'notMinor' : 'yes'
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
USERNAME = 'marceds'
TOKEN = 'm1a4r2c9efs'
GRAPH_ID = 'graph1'

## TODO: Create a graph definition

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
    'id' : GRAPH_ID,
    'name' : 'Meditation Graph',
    'unit' : 'Minutes',
    'type' : 'int',
    'color' : 'ajisai'

}

headers={
    'X-USER-TOKEN' : 'herewego'
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

today = datetime.now()

## TODO: Post value to the graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_data = {
    'date' : today.strftime('%Y%m%d'),
    'quantity': input('How many minutes did you meditate today?'),
}

#response = requests.post(url=graph_endpoint, json=pixel_data, headers=headers)
#print(response.text)

## TODO: Update user's token
'''update_token= f"{pixela_endpoint}/{USERNAME}"
new_token={
    'newToken' : 'herewego'
}

headers={
    'X-USER-TOKEN' : 'herewego'
}'''

#response=requests.put(url=update_token, json=new_token, headers=headers)
#print(response.text)

## TODO: Delete a record
date='20230202'

delete_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
response=requests.delete(url=delete_endpoint, headers=headers)
print(response.text)