from flipclip.backend.core.node import Node

class ExportNode(Node):
    def __init__(
        self, 
        input_key: list[str],   # ["timestamp"]
        output_key: list[str],  # ["clip_data"]
    ):
        super().__init__(input_key, output_key)


    def execute(self, state) -> dict:
        frame_data = state[self.input_key[0]]

        clip_data = []
      
        return {   
            self.output_key[0]: clip_data
        }