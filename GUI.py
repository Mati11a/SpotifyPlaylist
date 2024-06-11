import manager
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from urllib.request import urlopen
import tkinter as tk
from PIL import ImageTk

scope = 'playlist-read-private'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
root = tk.Tk()

def get_image(url):
    data = urlopen(url)
    image = ImageTk.PhotoImage(data=data.read())
    image = ImageTk.getimage(image)
    image = image.resize((128, 128))
    image = ImageTk.PhotoImage(image)
    return image


x = Authorization.Playlists()
test = x.get_playlists(sp)
image = get_image(test[0]['image'])

tk.Label(root, image=image).pack()
root.mainloop()
