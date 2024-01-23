import requests

class Post:
    def __init__(self, id:int) -> None:
        self.blog_endpoint = "https://api.npoint.io/c790b4d5cab58020d391"
        self.response = requests.get(self.blog_endpoint)
        self.blog_posts = {
            
        }
        for item in self.response.json():
            if item["id"] == id:
                self.blog_posts = {"title": item["title"] , "body": item["body"]}