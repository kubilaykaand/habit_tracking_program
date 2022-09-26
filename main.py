import requests
from datetime import datetime

TOKEN="unique_for_everyone"
USERNAME="unique_for_everyone"
GRAPH_ID="graph3" #for this code its graph3

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

pixel_creation_endpoint= f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()
formatted_date=f"{today.strftime('%G')}{today.strftime('%m')}{today.strftime('%d')}"
# print(today)

pixel_data={
    "date" : formatted_date,
    "quantity" : input("How many kilometers did you cycle today?"),
}
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_date}"

# response= requests.delete(url=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_date}", headers=headers)
# print(response.text)