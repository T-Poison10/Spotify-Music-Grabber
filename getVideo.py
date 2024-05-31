"""This script defines the `searchVideos` class,
which is used to search for videos on YouTube and
download the audio from the videos."""


from pytube import Search
from pytube import YouTube


class searchVideos:
    def __init__(self, name) -> None:
        self.name = name

    def findVideo(self):
        search = Search(self.name)
        result = search.results[1]
        return result.video_id

    def downloadSong(self, url, outputPath=""):
        yt = YouTube(url)
        try:
            yt.streams.get_audio_only().download(output_path=outputPath)
        except Exception as e:
            print(e)

    def getTitle(self, url):
        yt = YouTube(url)
        title = yt.title
        return title


if __name__ == "__main__":
    video = searchVideos("hail to the king")
    print(video.findVideo())
