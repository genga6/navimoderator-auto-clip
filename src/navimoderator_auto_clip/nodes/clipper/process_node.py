from flipclip.backend.core.node import Node

class ProcessNode(Node):
    def __init__(
        self, 
        input_key: list[str],   # ["video_url"]
        output_key: list[str],  # ["frame_data"]
    ):
        super().__init__(input_key, output_key)


    def execute(self, state) -> dict:
        video_url = state[self.input_key[0]]

        frame_data = []
      
        return {   
            self.output_key[0]: frame_data
        }