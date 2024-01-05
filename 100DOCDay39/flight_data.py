import requests
import os

TRAVEL_FROM = "KHI"

class FlightData:
    def __init__(self) -> None:
        self.flight_search_api = os.environ.get("FLIGHT_SEARCH_API")
        self.flight_search_endpoint = "https://api.tequila.kiwi.com/v2/search"

    def get_flight_data(self, city:str, price_from:int, price_to:int):    
        self.city = city
        flight_search_header = {
            "apikey":self.flight_search_api,
        }
        flight_search_params = {
            "fly_from": TRAVEL_FROM,
            "fly_to": self.city,
            "date_from": "06/01/2024",
            "date_to": "06/06/2024",
            "limit": 1,
            "curr": "PKR",
            "price_from": price_from,
            "price_to": price_to,
        }
        self.response = requests.get(url=self.flight_search_endpoint,
                                    params=flight_search_params,
                                    headers=flight_search_header)
        
        return self.response.json()["data"]