from sheet_manager import Sheety
from flight_data import FlightData
from notification_manager import NotificationManager

sheet_data = Sheety()
flight_data = FlightData()
notification = NotificationManager()

TRAVEL_FROM = "KHI"

sheet_data = sheet_data.get_data()

for data in sheet_data:
    iataCode = data["iataCode"]
    current_lowestPrice = data["lowestPrice"]
    data = flight_data.get_flight_data(iataCode, 1000, 110000)

    for item in data:
        data = item
        city_code = data["cityCodeTo"]
        city = data["cityTo"]
        price = data["price"]
        
        if price < current_lowestPrice:
            notification.send_sms(price=price,
                                city_to=city, 
                                city_code_to=city_code,
                                travel_from = TRAVEL_FROM)
        else:
            print("Sorry no lower prices were found")
            break