from flask import Flask, render_template, request
import requests
from datetime import datetime
import smtplib

cur_date = str(datetime.now()).split(" ")[0]
api_endpoint = "https://api.npoint.io/682635d392ebc4bd0518"
response = requests.get(url=api_endpoint)
data = response.json()

app = Flask("__name__")

@app.route("/")
def home():
    return render_template("index.html", data = data, year = cur_date)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():                
    return render_template("contact.html")

@app.route("/form_entry", methods = ["GET", "POST"])
def recieve_data():
        
        if request.method == "POST":
            name = request.form["name"]
            email = request.form["email"]
            phone_number = request.form["phone_number"]
            message = request.form["message"]
            print(f"{name}\n{email}\n{phone_number}\n{message}")
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user="ozairmohammad12@gmail.com", password="os.environ.get(PW)")
                connection.sendmail(from_addr="ozairmohammad12@gmail.com", to_addrs=email, msg=":)")
        
        return f"<h1> Your message was sent successfully </h1>"

@app.route("/post/<int:post_id>")
def post(post_id):
    post = {}
    for item in data:
        if item["id"] == post_id:
            post["id"] = item["id"]
            post["title"] = item["title"]
            post["subtitle"] = item["subtitle"]
            post["body"] = item["body"]
            post["image_url"] = item["image_url"]
    print(post)
    return render_template("post.html", post = post, year = cur_date)



if __name__ == "__main__":
    app.run(debug=True)