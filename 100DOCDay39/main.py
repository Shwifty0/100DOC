from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta


data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tommorow = datetime.now() + timedelta(1)
six_months_from_today = datetime.now() + timedelta(days=(6*30))

for destination in sheet_data:
    flight = flight_search.flight_search(
        "KHI",
        destination["iataCode"],
        from_time = tommorow,
        to_time = six_months_from_today
    )
    
    if flight == None:
        continue
    
    if flight.price < destination["lowestPrice"]:
        users = data_manager.get_customer_emails()
        emails = [row["email"]for row in users]
        names = [row["firstName"] for row in users]
        message = f"Low price alert! Only PKR: {flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
        
        notification_manager.send_email(emails, message)