from flight_data import FlightData
from sheet_manager import Sheety

flight_data = FlightData()
post_data = Sheety()

travel_to = ["ERF", "ISB", "LHE", "AUH"]

data = [flight_data.get_flight_data(city, 1000, 110000) for city in travel_to]

for item in data:
    data = item[0]
    response = post_data.post_data(data)
    print(response) 