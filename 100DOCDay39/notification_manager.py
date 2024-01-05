from twilio.rest import Client
import os
class NotificationManager:
    def __init__(self) -> None:
            self.twilio_sid = os.environ.get("TWILIO_SID")
            self.twilio_auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

    def send_sms(self, price, city_to, city_code_to, travel_from):  
        client = Client(self.twilio_sid, self.twilio_auth_token)
        self.message = client.messages.create(
            body= f"Low price alert! Only PKR{price} to fly from Karachi-{travel_from} to {city_to}-{city_code_to}",
            from_= "+16179345452",
            to= "+923130460101"
        )