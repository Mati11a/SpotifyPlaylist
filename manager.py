import spotipy
import os
from urllib.request import urlopen
from PIL import ImageTk

#Gets all names and images of playlists
class Playlists:
        
    def get_playlists(self, sp):
        playlists = sp.current_user_playlists(limit=50)
        playlists = playlists['items']
        songList = []
        for playlist in playlists:
            songList.append({'name':playlist['name'],'image': playlist['images'][0]['url']})
        return songList
    def get_songs(playlist):
        print("x.result")

    #print(get_playlists(sp))