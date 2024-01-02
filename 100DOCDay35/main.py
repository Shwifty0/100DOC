import requests
import os

from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from apikey import API_KEY, LAT, LNG, TWILIO_SID, TWILIO_AUTH_TOKEN


# TWILIO AUTO-SMS API
account_sid = TWILIO_SID
auth_token = TWILIO_AUTH_TOKEN


# OPENWEATHERAPI
response = requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast", params={"lat":LAT, "lon":LNG, "appid":API_KEY, "cnt":4})
response.raise_for_status()


three_hr_forecast = response.json()["list"]
weather = [forecast["weather"][0] for forecast in three_hr_forecast]

will_rain = False
desc = ""
for item in weather:
    if item["id"] < 800:
        will_rain = True
        desc = item["description"]
        break
    
if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {"https": os.environ["https_proxy"]}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    client.messages.create(
        body=f"Today's weather condition\nDescription:{desc.upper()}.",
        from_= '+16179345452',
        to="+923130460101"
    )
