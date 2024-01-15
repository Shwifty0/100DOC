"""
1. Create a playlist for user : Shwifty -> user_playlist_create()
2. Get all the song uris from SearchAPI
3. Add the songs in the playlists -> 

requirements: 
- create playlist and get its id
- user_playlist_add_tracks(user, playlist_id, tracks, position=None) -> tracks -> track ids? I think!

"""
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

CLIENT_ID = os.environ.get("client_id") 
CLIENT_SECRET =os.environ.get("client_secret")

scope = "playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri="https://developer.spotify.com/documentation/web-api",
    scope=scope))

DATE = input("Which year do you want to travel to? Type the date in this ormate YYYY-MM-DD: ")
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


playlist_name = f"Top 100 Billboard {DATE}"
user_id = sp.me()["uri"].split(":")[2]

create_playlist = sp.user_playlist_create(user=user_id, name = playlist_name)
track_uris = [sp.search(q=f"{song} - {artist}", limit=1, type= "track")["tracks"]['items'][0]['uri'].split(":")[2] for (song, artist) in song_artist.items()]

for playlist in sp.user_playlists(user_id)["items"]:
    try:
        if playlist["name"] == playlist_name:
            sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist["id"], tracks=track_uris)
    except:
        continue