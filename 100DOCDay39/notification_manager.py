from twilio.rest import Client
import os
class NotificationManager:
    def __init__(self) -> None:
            self.twilio_sid = os.environ.get("TWILIO_SID")
            self.twilio_auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

    def send_sms(self, message):  
        client = Client(self.twilio_sid, self.twilio_auth_token)
        self.message = client.messages.create(
            body= message,
            from_= "+16179345452",
            to= "+923130460101"
        )