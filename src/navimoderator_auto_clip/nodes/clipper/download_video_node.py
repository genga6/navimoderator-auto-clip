from navimoderator_auto_clip.core.node import Node
from navimoderator_auto_clip.nodes.downloader.downloader import Downloader
from navimoderator_auto_clip.nodes.downloader.youtube_downloader import YoutubeDownloader

class DownloadVideoNode(Node):
    def __init__(
        self, 
        input_key: list[str],   # ["video_url"]
        output_key: list[str],  # ["downloaded_video_path"]
    ):
        super().__init__(input_key, output_key)
        self.downloader_map = {
            "youtube.com": YoutubeDownloader(), 
        }

    def _get_downloader(self, video_url: str) -> Downloader | None:
        for platform_url, downloader in self.downloader_map.items():
            if platform_url in video_url:
                return downloader
        return None

    def execute(self, state) -> dict:
         video_url = getattr(state, self.input_key[0])
         downloader = self._get_downloader(video_url)

         if downloader:
             downloaded_video_path = downloader.download_video(video_url)
             return {
                 self.output_key[0]: downloaded_video_path
             }
         else:
             raise ValueError(f"サポートされていない配信プラットフォームのURLです: {video_url}")