from navimoderator_auto_clip.core.node import Node
from navimoderator_auto_clip.subgraphs.clip_suggestion_subgraph import ClipSuggestionState
from navimoderator_auto_clip.transcriber import Transcriber  #TODO: 別途容易


class TranscriptNode(Node):
    def __init__(
        self, 
        input_key: list[str],   # [""]
        output_key: list[str],  # [""]
    ):
        super().__init__(input_key, output_key)
        self.transcriber = Transcriber()

    def execute(self, state) -> dict:
        # downloaded_video_path = getattr(state, self.input_key[0])
        # clipping_options = getattr(state, self.input_key[1])

        # return {
        #     self.output_key[0]: clip_suggestion
        # }
        pass    # TODO: 動画内容の文字起こし（切り抜き、およびテロップで必要）