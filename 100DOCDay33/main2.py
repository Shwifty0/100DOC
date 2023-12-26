from requests import get
from datetime import datetime
import smtplib

MY_LAT = 24.916663
MY_LONG = 67.083333

MY_EMAIL = "YOUR EMAIL"
APP_PW = "YOUR PASSWORD"

# function to check for nighttime
def is_night():
    parameters = {
        "lat":MY_LAT,
        "lng":MY_LONG,
    }
    response = get(url="https://api.sunrisesunset.io/json", params=parameters)
    response.raise_for_status()

    sunset = response.json()["results"]["sunset"].strip("+").split("T")[0].split(":")[0]
    current_hour = datetime.now().strftime("%I:%M %p").split(":")[0][1]
    
    if current_hour == sunset:
        return True


# function to return ISS location
def iss_location():
    response = get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    iss_lng = float(response.json()["iss_position"]["longitude"])
    iss_lat = float(response.json()["iss_position"]["latitude"])
    
    if MY_LONG+5 <= iss_lng <= MY_LONG-5 and MY_LAT+5 <= iss_lat <= MY_LAT-5:
        return True

object = smtplib.SMTP("smtp.gmail.com", port = 587)
print("Object Created")
object.starttls()
object.login(MY_EMAIL, APP_PW)
print("Login Successful")
if is_night() and iss_location():
    print("False")
    object.sendmail(MY_EMAIL, MY_EMAIL, "Subject:ISS Notification\n\nLook Up!!!!")
    print("Email Sent")
else:
    object.sendmail(MY_EMAIL, MY_EMAIL, "Subject:ISS Notification\n\nKeep Working Cunt!!!!")
    print("Email Sent")



