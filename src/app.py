import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

# Get credential values
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(auth_manager=auth_manager)


# 5K4W6rqBFWDnAN6FQUkS6x kanye west

#Obtener las mejores canciones del artista

results = spotify.artist_top_tracks("5K4W6rqBFWDnAN6FQUkS6x")



songs = []

for track in results['tracks']:
    songs.append({"name":track['name'],
                  "popularity":track['popularity'],
                  "duracion_min":track['duration_ms']/60000})



df= pd.DataFrame(songs)

print(df)


import matplotlib 

plt.scatter(df['duracion_min'],df['popularity'],)

plt.show