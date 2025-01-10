from navimoderator_auto_clip.platform.platform_integration import PlatformAPIClient

class TwitchAPIClient(PlatformAPIClient):
    def download_video(self, video_url, output_path):
        # TwitchAPIを使用して動画取得
        pass
    
    def get_video_metadata(self, video_url):
        # TwitchAPIを使用して字幕取得
        pass
    
    def get_captions(self, video_url, language_code = "ja"):
        # TwitchAPIを使用して動画メタデータ取得
        pass
    
    def get_comments(self, video_url, max_results = 100):
        # TwitchAPIを使用してコメント取得
        pass