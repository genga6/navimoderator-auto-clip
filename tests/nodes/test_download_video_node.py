import pytest
from unittest.mock import MagicMock
from pydantic import BaseModel, Field
from langgraph.graph import StateGraph
from navimoderator_auto_clip.nodes.clipper.download_video_node import DownloadVideoNode
from navimoderator_auto_clip.nodes.downloader.youtube_downloader import YoutubeDownloader

class State(BaseModel):
    video_url: str = Field(default="")
    downloaded_video_path: str = Field(default="")

@pytest.fixture
def mock_youtube_downloader(mocker):
    mock_downloader = mocker.patch.object(YoutubeDownloader, 'download_video')
    mock_downloader.return_value = "/fake/path/to/video.mp4"
    return mock_downloader

def test_download_video_node_youtube(mock_youtube_downloader):
    input_key = ["video_url"]
    output_key = ["downloaded_video_path"]

    download_video_node = DownloadVideoNode(
        input_key=input_key,
        output_key=output_key, 
    )

    graph_builder = StateGraph(State)
    graph_builder.add_node("download_video_node", download_video_node)
    graph_builder.set_entry_point("download_video_node")
    graph_builder.set_finish_point("download_video_node")
    graph = graph_builder.compile()

    state = {
        "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    }

    result = graph.invoke(state, debug=True)

    assert result["downloaded_video_path"] == "/fake/path/to/video.mp4"
    mock_youtube_downloader.assert_called_once_with("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

def test_download_video_node_unsupported_platform():
    input_key = ["video_url"]
    output_key = ["downloaded_video_path"]

    download_node = DownloadVideoNode(input_key=input_key, output_key=output_key)

    graph_builder = StateGraph(State)
    graph_builder.add_node("download_video_node", download_node)
    graph_builder.set_entry_point("download_video_node")
    graph_builder.set_finish_point("download_video_node")
    graph = graph_builder.compile()

    state = {
        "video_url": "https://www.example.com/video/12345"
    }

    with pytest.raises(ValueError, match="サポートされていない配信プラットフォームのURLです"):
        graph.invoke(state, debug=True)
