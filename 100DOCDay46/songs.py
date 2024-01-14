import requests
from bs4 import BeautifulSoup

DATE = "2000-02-12"
URL =  f"https://www.billboard.com/charts/hot-100/{DATE}/"
response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

billboard_charts= soup.find_all("div", {"class" : "o-chart-results-list-row-container"})

song_artist = {
    billboard_charts[0].find("h3", {"id" : "title-of-a-story"}).getText().strip() : billboard_charts[0].find("span", {"class" : "c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet"}).getText().strip(),
}

for item in billboard_charts:
    try:
        name_of_song = item.find("h3", {"id" : "title-of-a-story"}).getText().strip()
        singer_band = item.find("span", {"class": "c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only"}).getText().strip()
        song_artist[name_of_song] = singer_band
    except:
        continue

print(song_artist)
