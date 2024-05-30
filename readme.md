# Music Downloader

This repository contains a Python-based music downloader that automates the process of searching for songs on YouTube, extracting the video IDs, and downloading the audio from the videos. The project uses libraries such as `pytube` for interacting with YouTube, `BeautifulSoup` for web scraping, and `selenium` for automating browser actions.

## Features

- Reads a list of song names from a text file.
- Searches for each song on YouTube using the `pytube` library.
- Extracts the video ID of the first search result for each song.
- Downloads the audio from each video to a specified directory.

## Usage

1. Clone the repository and navigate to the project directory.
2. Install the required Python libraries using pip: `pip install -r requirements.txt`
3. Run the `python scrapper.py` to get list of song names to `Data/Music.txt`.
4. Run the script: `python main.py`
5. The audio files will be downloaded to the specified directory.

Please note that this project is for educational purposes only. Always respect the terms of service of any website you scrape or interact with programmatically.