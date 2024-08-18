import datetime

import requests
from DateTime import *
import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("PIXELA_USERNAME")
TOKEN = os.getenv("PIXELA_TOKEN")
GRAPH_ID = os.getenv("PIXELA_GRAPH_ID")
pixela_endpoint = "https://pixe.la/v1/users"

#create a new user
user_params = {
    "token": TOKEN,
    "username" :USERNAME ,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#Grate a new graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Swimming Graph",
    "unit": "km",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN,

}

today = datetime.datetime.now()
post_config = {
    "date" : today.strftime("%Y%m%d"),
    "quantity": input("How many km did you swim today?"),
}


habit_graph_1_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

response = requests.post(url=habit_graph_1_endpoint, json=post_config, headers=headers)
print(response.text)