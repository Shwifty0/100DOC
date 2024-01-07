import requests
import os
from flight_data import FlightData

tequila_endpoint = "https://api.tequila.kiwi.com"
tequila_api_key = os.environ.get("FLIGHT_SEARCH_API")

class FlightSearch:
    def get_destination_code(self, city_name):
        location_endpoint = f"{tequila_endpoint}/locations/query"
        headers = {"apikey": tequila_api_key}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        return response.json()["locations"][0]["code"]
    
    def flight_search(self, origin_city_code, destination_city_code, from_time, to_time):
        header = {"apikey":tequila_api_key}
        query = {
            "fly_from": origin_city_code,
            "fly_to":destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "PKR"
        }

        response = requests.get(
            url=f"{tequila_endpoint}/v2/search",
            headers=header,
            params=query,
        )
        
        try:
            data = response.json()["data"][0]
        except IndexError:
            query["max_stopovers"] = 1
            response = requests.get(
                url=f"{tequila_endpoint}/v2/search",
                headers=header,
                params=query,
            )
            try:
                data = response.json()["data"][0]
            except:
                return None
            else:
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][1]["cityTo"],
                    destination_airport=data["route"][1]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][2]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"]
                )
                return flight_data

        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            print(f"{flight_data.destination_city}: PKR{flight_data.price}")
            return flight_data