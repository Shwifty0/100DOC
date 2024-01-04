import requests
from datetime import datetime, timedelta

USERNAME = "ozair"
TOKEN = "iw1j3u1209ud0sjad1ud10h"
date_today = datetime.now()
date_yesterday = datetime.now() - timedelta(1)


pixela_endpoint = "https://pixe.la/v1/users"
pixela_graph_endpoint = "https://pixe.la/v1/users/ozair/graphs"
pixel_post_endpoint = "https://pixe.la/v1/users/ozair/graphs/graph1"
update_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1/{date_today.strftime('%Y%m%d')}"
delete_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1/{date_today.strftime('%Y%m%d')}"

headers = {
    "X-USER-TOKEN":TOKEN
}

user_params = {
    "token": TOKEN,
    "username":USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor":"yes"
}
graph_params = {
    "id":"graph1",
    "name":"Coding",
    "unit":"hours",
    "type":"float",
    "color":"kuro"    
}

pixel_post_params = {
    "date":date_yesterday.strftime("%Y%m%d"),
    "quantity":"1000"
}

pixel_update_params = {
    "quantity":"1900"
}

response = requests.delete(url=delete_pixel_endpoint,headers=headers)
print(response.text)