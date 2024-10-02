import requests
from bs4 import BeautifulSoup

#TODO: The BillBoard hot 100 is not functioning, Creating a alternate project for top 100 hindi sings of all time.

response = requests.get("https://www.bbc.co.uk/asiannetwork/vote/top-songs/index.shtml")
content = response.text

soup= BeautifulSoup(content, "html.parser")

song_names = soup.select(selector= ".intro ")
titles = [song.text.split("  ")[-1] for song in song_names]

#SPOTIFY_PART
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "YOUR CREDENTIALS"
CLIENT_SECRET = "YOUR CREDENTIALS"
REDIRECT_URL = "http://example.com"
USERNAME = "YOUR CREDENTIALS"
SCOPE = "playlist-modify-public"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URL, username=USERNAME, cache_path="TOKEN.txt"))
username = sp.current_user()["id"]

#TODO: SEARCH SPOTIFY FOR SONGS AND ADD URI
uri_list = []
for title in titles:
    try:
        track = sp.search(title,limit=1,type='track')['tracks']["items"][0]['uri']
        uri_list.append(track)
    except:
        print("Does Not exist in Spotify, Moving on to next song")

print(uri_list)
#TODO: Create a Playlist
name = "100 Greatest Bollywood Song of All Time"
spotify_playlist = sp.user_playlist_create(user=username, name=name, public=True, collaborative=False,description="Get lost in the to 100 bollywood melodies of all time.")
#
#TODO: Adding tracks to playlist
sp.playlist_add_items(playlist_id= spotify_playlist["id"], items=uri_list[2:102])