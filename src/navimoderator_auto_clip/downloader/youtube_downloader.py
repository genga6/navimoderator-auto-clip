from navimoderator_auto_clip.nodes.downloader.downloader import Downloader
from pytube import YouTube

class YoutubeDownloader(Downloader):
    def download_video(self, video_url: str) -> str:
        try:
            yt = YouTube(video_url)
            video_stream = yt.streams.get_highest_resolution()
            download_path = "./downloads"   # TODO: 要検討
            video_stream.download(output_path=download_path)
            return f"{download_path}/{yt.title}.mp4"
        except Exception as e:
            print(f"YouTube動画のダウンロード中にエラーが発生しました: {e}")
            return None