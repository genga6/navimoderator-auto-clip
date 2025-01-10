from navimoderator_auto_clip.platform.platform_integration import PlatformAPIClient
from navimoderator_auto_clip.platform.youtube_api_client import YoutubeAPIClient
from navimoderator_auto_clip.platform.twitch_api_client import TwitchAPIClient

class PlatformAPIClientFactory:
    def create_client(self, video_url: str) -> PlatformAPIClient | None:
        if "youtube.com" in video_url:
            return YoutubeAPIClient()
        elif "twitch.tv" in video_url:
            return TwitchAPIClient()
        return None