from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))


url = "https://open.spotify.com/playlist/7H6PN3eUARNQgSf3S3TwE8"
driver.get(url)
driver.implicitly_wait(100)
html = driver.page_source
print(html)
soup = BeautifulSoup(html, "html.parser")

songs = {"title": [],
         "Artist": []}

titles = soup.select(
    "div.encore-text.encore-text-body-medium.encore-internal-color-text-base.btE2c3IKaOXZ4VNAb8WQ.standalone-ellipsis-one-line")

artists = soup.select("div.encore-text encore-text-body-small")
for artist in artists:
    print(artist.children.string)


albums = soup.select("a.standalone-ellipsis-one-line")
with open("Data/Music.txt", "w") as f:
    for title in titles:
        f.write(title.string)
        f.write('\n')

for album in albums:
    print(album.string)
