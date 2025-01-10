import os
from navimoderator_auto_clip.core.node import Node
from navimoderator_auto_clip.platform.platform_api_client_factory import PlatformAPIClientFactory

class DownloadVideoNode(Node):
    def __init__(
        self, 
        input_key: list[str],   # ["video_url"]
        output_key: list[str],  # ["downloaded_video_path"]
        download_path: str = "/workspaces/navimoderator_auto_clip/data"
    ):
        super().__init__(input_key, output_key)
        self.platform_api_client_factory = PlatformAPIClientFactory()
        self.download_path = download_path
        os.makedirs(self.download_path, exist_ok=True)

    def execute(self, state) -> dict:
        video_url = getattr(state, self.input_key[0])
        platform_api_client = self.platform_api_client_factory.create_client(video_url) 

        if platform_api_client:
            try:
                print(f"動画 {video_url} のダウンロードを開始します...")
                video_id = video_url.split("?v=")[1] if "youtube.com" in video_url else video_url.split("/")[-1]
                output_filename = f"{video_id}.mp4"
                downloaded_file_path = os.path.join(self.download_path, output_filename)

                downloaded_file_path = platform_api_client.download_video(video_url, self.download_path, output_filename)

                if downloaded_file_path:
                    print(f"ダウンロード完了: {downloaded_file_path}")
                    return {self.output_key[0]: downloaded_file_path}
                else:
                    raise ValueError(f"PlatformAPIClient での動画ダウンロードに失敗しました: {video_url}")
            except Exception as e:
                print(f"動画のダウンロード中にエラーが発声しました: {e}")
                return {self.output_key[0]: None}
        else:
            raise ValueError(f"サポートされていないプラットフォームのURLです:  {video_url}")