from navimoderator_auto_clip.core.node import Node


class ClipNode(Node):
    def __init__(
        self, 
        input_key: list[str],   # ["downloaded_video_path", "clipping_options"]
        output_key: list[str],  # ["clip_suggestions"]
    ):
        super().__init__(input_key, output_key)

    def _generate_clip_suggestions(self, video_path: str, clipping_options: dict) -> list:
        model_name = clipping_options.get("model_selection")
        clipping_criteria = clipping_options.get("clipping_criteria")
        output_duration_bins = clipping_options.get("output_duration_bins")
        target_keywords = clipping_options.get("target_keywords")

        model = self._load_model(model_name)

    def _load_model(self, model_name: str):
        # TODO: 実装はModelFactoryに委譲
        print(f"モデル {model_name} をロードします...")
        return None

    def execute(self, state) -> dict:
        downloaded_video_path = getattr(state, self.input_key[0])
        clipping_options = getattr(state, self.input_key[1])

        clip_suggestion = self._generate_clip_suggestions(downloaded_video_path, clipping_options)
        return {
            self.output_key[0]: clip_suggestion
        }