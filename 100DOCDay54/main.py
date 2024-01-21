from flask import Flask
from flask import render_template, request
import requests
import os
app = Flask("__name__")

open_weather_api = os.environ.get("OPEN_WEATHERAPI")
print(open_weather_api)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/", methods = ["GET", "POST"])
def weather_data():
    if request.method == "POST":
        latitude = request.form["lat"]
        longitude = request.form["lon"]
        endpoint = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={open_weather_api}'
        response = requests.get(url=endpoint)

    return response.json()["main"]


if __name__ == "__main__":
    app.run(debug=True)