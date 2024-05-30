from pytube import Search
from pytube import YouTube


class searchVideos:
    def __init__(self, name) -> None:
        self.name = name

    def findVideo(self):
        search = Search(self.name)
        result = search.results[1]
        return result.video_id

    def downloadVideo(self, url, outputPath=""):
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
    video.downloadVideo("https://www.youtube.com/watch?v=2bZPb025Wjw")
