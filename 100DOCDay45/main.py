from bs4 import BeautifulSoup
import requests
import lxml

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
website_content = response.content

soup = BeautifulSoup(website_content, "html.parser")
headings = soup.find_all("h3", attrs=["title"])

top_movies = {}
for heading in headings:
    formatted = heading.text.split(") ")
    if len(formatted) < 2:
        formatted = heading.text.split(": ")
        top_movies[formatted[1]] = formatted[0]
    top_movies[formatted[1]] = formatted[0]

with open("movies.txt", "w") as f:
    for k, v in reversed(top_movies.items()):
        f.write(f"{v}) {k}\n")

