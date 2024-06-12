import spotipy
import os
from urllib.request import urlopen
from PIL import ImageTk


#Gets all names and images of playlists
def get_playlists(sp):
    playlists = sp.current_user_playlists(limit=50)
    playlists = playlists['items']
    playlistList = []
    for playlist in playlists:
        playlistList.append({'name': playlist['name'], 'image': playlist['images'][0]['url'],
                         'playlist_link': playlist['external_urls']['spotify']})
    return playlistList

#Gets all the Songs and Names of artists of that song
def get_songs(playlist, sp):
    playlist_id = playlist.rsplit('/', 1)[-1]
    songs = sp.playlist_items(playlist_id)
    songList = []
    songs = songs['items']

    for song in songs:
        songList.append({'name': song['track']['name'], 'artist': song['track']['artists'][0]['name']})
    return songList
