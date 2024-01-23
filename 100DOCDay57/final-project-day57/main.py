from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

@app.route('/')
def home():
    blog_endpoint = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_endpoint)
    blog_posts_list = response.json()
    return render_template("index.html", blog_posts = blog_posts_list)

@app.route("/post/<int:id>")
def post(id):
    blogs = Post(id=id)
    
    post = blogs.blog_posts

    return render_template("post.html", post = post)

if __name__ == "__main__":
    app.run(debug=True)
