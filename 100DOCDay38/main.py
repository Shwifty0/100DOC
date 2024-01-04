import requests
from datetime import datetime
import os

SHEETY_AUTH = os.environ.get("SHEETY_AUTH")
NUTRITION_API_KEY = os.environ.get("NUTRITION_API_KEY")
NUTRITION_APP_ID = os.environ.get("NUTRITION_APP_ID")

nutrionix_workout_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/66e832008d5b0906c5e4e3a8bd2ca1d6/myworkouts/sheet1"

exercises_input = input("What exercises did you do today?😃\t")

nutrionix_headers = {
    "x-app-id":NUTRITION_APP_ID,
    "x-app-key":NUTRITION_API_KEY
}
body_param = {
    "query": exercises_input,
    "gender":"male",
    "weight_kg":"81",
    "height_cm":"171",
    "age":"23"
}

response = requests.post(url=nutrionix_workout_endpoint, json = body_param, headers=nutrionix_headers,)
json_data = response.json()

for i in range(len(json_data["exercises"])):
    
    # duration, calories, nameofexercise, date&time
    duration = json_data["exercises"][i]["duration_min"]
    calories = json_data["exercises"][i]["nf_calories"]
    nameofexercise = json_data["exercises"][i]["name"].title()
    date = datetime.now().date().strftime("%d/%m/%Y") #Date month year 
    time = datetime.now().time().strftime("%H:%M:%S") #Hours Minutes Seconds
    
    sheety_header = {
        "Authorization": SHEETY_AUTH
    }
    
    sheety_post_payload = {
        "sheet1":{
            "date":date,
            "time":time,
            "exercise":nameofexercise,
            "duration":duration,
            "calories":calories
        }
        }

    sheety_response = requests.post(url = sheety_endpoint, json = sheety_post_payload, headers=sheety_header)
    print(sheety_response.text)