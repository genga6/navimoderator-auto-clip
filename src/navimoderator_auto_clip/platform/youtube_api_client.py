from navimoderator_auto_clip.platform.platform_integration import PlatformAPIClient

class YoutubeAPIClient(PlatformAPIClient):
    def download_video(self, video_url: str, output_path: str, output_filename: str):
        # YoutubeDataAPIを使用して動画取得
        pass
    
    def get_video_metadata(self, video_url):
        # YoutubeDataAPIを使用して字幕取得
        pass
    
    def get_captions(self, video_url, language_code = "ja"):
        # YoutubeDataAPIを使用して動画メタデータ取得
        pass
    
    def get_comments(self, video_url, max_results = 100):
        # YoutubeDataAPIを使用してコメント取得
        pass