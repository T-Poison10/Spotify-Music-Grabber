from getVideo import searchVideos
from songs import Songs
from tkinter import filedialog
import os
output_path = filedialog.askdirectory()

path = "Data/Music.txt"
song = Songs(path)

musicNames = song.readNames()
for name in musicNames:
    vid = searchVideos(name)
    videoID = vid.findVideo()
    url = "https://www.youtube.com/watch?v=" + videoID
    vid.downloadVideo(url, output_path)

