import requests
import os

SHEETY_AUTH = os.environ.get("SHEETY_AUTH")
SHEETY_ENDPOINT = "https://api.sheety.co/66e832008d5b0906c5e4e3a8bd2ca1d6/flightDeals/sheet1"

class Sheety:
    def __init__(self) -> None:
        self.sheety_auth = SHEETY_AUTH
        self.sheety_endpoint = SHEETY_ENDPOINT
        self.sheety_header = {
            "Authorization": SHEETY_AUTH
        }
        
    def post_data(self, data):
        #city_from = data["cityFrom"]
        city_to = data["cityTo"]
        city_code_to = data["cityCodeTo"]
        price = data["price"]
        
        sheety_post_payload = {
            "sheet1": {
                "city": city_to,
                "iataCode": city_code_to,
                "lowestPrice":price
            }
        }
        response = requests.post(url=SHEETY_ENDPOINT, json=sheety_post_payload, headers=self.sheety_header)
        return response.text
    
    def get_data(self):
        self.response = requests.get(url=SHEETY_ENDPOINT, headers=self.sheety_header)
        return self.response.json()["sheet1"]