from flask import Flask, render_template
import requests

genderize_endpoint = "https://api.genderize.io"
agify_endpoint = "https://api.agify.io"

app = Flask("__name__")

@app.route("/guess/<name>")
def guess(name):
    params = {
        "name": name
    }
    response1 = requests.get(genderize_endpoint, params=params)
    response2 = requests.get(agify_endpoint, params=params)
    
    api_name = response1.json()["name"].title()
    gender = response1.json()["gender"]
    age = response2.json()["age"]
    
    return render_template("index.html", api_name = api_name, gender = gender, age = age)


if __name__ == "__main__":
    app.run(debug=True)