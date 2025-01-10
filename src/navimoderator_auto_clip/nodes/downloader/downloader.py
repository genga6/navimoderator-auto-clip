from abc import ABC, abstractmethod

class Downloader(ABC):
    @abstractmethod
    def download_video(self, video_url: str) -> str:
        pass