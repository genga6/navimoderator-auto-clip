from abc import ABC, abstractmethod

class PlatformAPIClient(ABC):
    # 動画のダウンロード、メタデータの取得、字幕の取得、コメントの取得など、プラットフォームに関連する様々な機能を提供
    @abstractmethod
    def download_video(self, video_url: str, output_path: str, output_filename: str) -> str| None:
        pass

    @abstractmethod
    def get_video_metadata(self, video_url: str) -> dict | None:
        pass

    @abstractmethod
    def get_captions(self, video_url: str, language_code: str = "ja") -> str | None:
        pass

    @abstractmethod
    def get_comments(self, video_url: str, max_results: int = 100) -> list[dict] | None:
        pass

    