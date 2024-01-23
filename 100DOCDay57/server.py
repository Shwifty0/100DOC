from flask import Flask, render_template
import requests

genderize_endpoint = "https://api.genderize.io"
agify_endpoint = "https://api.agify.io"

app = Flask("__name__")

@app.route("/")
def home():
    return render_template("index.html")



@app.route("/blog/<num>")
def blog_posts(num):
    print(num)
    blog_endpoint = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_endpoint)
    blog_posts_list = response.json()
    return render_template("blog.html", blog_posts = blog_posts_list)

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