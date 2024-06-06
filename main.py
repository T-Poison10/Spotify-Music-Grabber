"""This is the main script for the Music Downloader project.
It reads song names from a text file, searches for each 
song on YouTube, and downloads the audio from the first search result."""


import os

from getVideo import searchVideos
from songs import Songs
from scraper import Scraper
from tkinter import filedialog

url = "https://open.spotify.com/playlist/07TLTn242y7Tn9xDE5rFrx"

# Asks which directory you want to save your songs in
output_path = filedialog.askdirectory()
htmlClass = "div.encore-text.encore-text-body-medium.encore-internal-color-text-base.btE2c3IKaOXZ4VNAb8WQ.standalone-ellipsis-one-line"

scraper = Scraper(url,htmlClass)

# Returns the html of the spotify playlist you provided url of
html = scraper.getHTML()

# Scrapes all the songs names adn returns a list of song names in playllist
titles = scraper.getNames(html)

# Writes all the scraped song names to the Music.txt file inside Data dir
scraper.writeNames(titles)


song = Songs("Data/Music.txt")

# Reads the song names from the file and returns a list of names
musicNames = song.readNames()


for name in musicNames:

    vid = searchVideos(name)
    # Searches for the video using the names we scaraped and returns the video id of 1st result
    videoID = vid.findVideo()
    # Concatinating the video id with yt url
    url = "https://www.youtube.com/watch?v=" + videoID

    # Downloads the mp3 of the song
    vid.downloadSong(url, output_path)
