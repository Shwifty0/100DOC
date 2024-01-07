from twilio.rest import Client
import smtplib
import os

class NotificationManager:
    def __init__(self) -> None:
            self.twilio_sid = os.environ.get("TWILIO_SID")
            self.twilio_auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
            
            self.email = "YOUR EMAIL"
            self.password = "YOUR APP PW"

    def send_sms(self, message):  
        client = Client(self.twilio_sid, self.twilio_auth_token)
        self.message = client.messages.create(
            body= message,
            from_= "+16179345452",
            to= "+923130460101"
        )
    
    def send_email(self, emails, message):
        with smtplib.SMTP(host="smtp.gmail.com", port = 587) as connection:
            connection.starttls()
            connection.login(user=self.email, password= self.password)
            for email in emails:
                connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )