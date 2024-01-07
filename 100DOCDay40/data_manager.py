import requests
import os
sheety_endpoint = "https://api.sheety.co/66e832008d5b0906c5e4e3a8bd2ca1d6/flightDeals/prices"
sheety_user_endpoint = "https://api.sheety.co/66e832008d5b0906c5e4e3a8bd2ca1d6/flightDeals/users"
sheety_auth = os.environ.get("SHEETY_AUTH")


header = {
    "Authorization":sheety_auth
}
class DataManager:
    def __init__(self) -> None:
        self.destination_data = {}
    
    def get_destination_data(self):
        response = requests.get(sheety_endpoint, headers=header)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data
    
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price":{
                    "iataCode":city["iataCode"]
                    }
            }
            response = requests.put(
                url=f"{sheety_endpoint}/{city['id']}",
                json=new_data,
                headers=header
            )
            print(response.text)
    
    def get_customer_emails(self):
        response = requests.get(url = sheety_user_endpoint, headers=header)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data