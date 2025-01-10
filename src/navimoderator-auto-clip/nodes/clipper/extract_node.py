from flipclip.backend.core.node import Node

class ExtractNode(Node):
    def __init__(
        self, 
        input_key: list[str],   # ["frame_data"]
        output_key: list[str],  # ["timestamp"]
    ):
        super().__init__(input_key, output_key)


    def execute(self, state) -> dict:
        frame_data = state[self.input_key[0]]

        timestamp = []
      
        return {   
            self.output_key[0]: timestamp
        }