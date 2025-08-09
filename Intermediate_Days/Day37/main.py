import requests
import os
from datetime import datetime

USERNAME = "josem279"
PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": PIXELA_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
print(graph_endpoint)

graph_config = {
    "id": GRAPH_ID,
    "name": "Lifting Graph",
    "unit": "Minutes",
    "type": "int",
    "color": "sora"   
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

pixel_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

now = datetime.strftime(datetime.now(), '%Y%m%d')

pixel_params = {
    "date": now,
    "quantity": input("How many minutes did you workout today?")
}

# response = requests.post(url=pixel_post_endpoint, json=pixel_params, headers=headers)

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{now}"

update_params = {
    "quantity": "45"
}

# response = requests.put(url=update_pixel_endpoint, json=update_params, headers=headers)


delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{now}"

response = requests.delete(delete_pixel_endpoint, headers=headers)
    
print(response.text)

