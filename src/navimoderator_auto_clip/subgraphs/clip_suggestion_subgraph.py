import os
from IPython.display import Image
from langgraph.graph import START, END, StateGraph
from pydantic import BaseModel, Field
from navimoderator_auto_clip.core.factory import NodeFactory


class ClipSuggestionState(BaseModel):
        video_path: str=Field(default="")
        clipping_criteria: str=Field(default="")
        clip_suggestions: list = Field(default_factory="list")
        transcript: str = Field(default="")
        summary: str = Field(default="")
        comments: list = Field(default_factory=list)

class ClipSuggestionSubgraph:
    def __init__(self):
        self.graph_builder = StateGraph(ClipSuggestionState)

        self.graph_builder.add_node(
            "transcript_node",
            NodeFactory.create_node(
                node_name="transcript_node",
                input_key=["video_path"],
                output_key=["transcript"],
            ),
        )
        self.graph_builder.add_node(
            "summary_node",
            NodeFactory.create_node(
                node_name="summary_node",
                input_key=["transcript"],
                output_key=["summary"],
            ),
        )
        self.graph_builder.add_node(
            "key_scene_extraction_node",
            NodeFactory.create_node(
                node_name="key_scene_extraction_node",
                input_key=["video_path", "summary", "comments", "clipping_criteria"],
                output_key=["clip_suggestions"],
            ),
        )
        self.graph_builder.add_edge(START, "transcript_node")
        self.graph_builder.add_edge("transcript_node", "summary_node")
        self.graph_builder.add_edge("summary_node", "key_scene_extraction_node")
        self.graph_builder.add_edge("key_scene_extraction_node", END)

        self.graph = self.graph_builder.compile()

    def __call__(self, state: ClipSuggestionState) -> dict:
        result = self.graph.invoke(state, debug=True)
        return result

    def make_image(self, path: str):
        image = Image(self.graph.get_graph().draw_mermaid_png())
        os.makedirs(path, exist_ok=True)
        with open(path + "clip_suggestion_subgraph.png", "wb") as f:
            f.write(image.data)

if __name__ == "__main__":
    image_dir = "/workspaces/clip_suggetion_subgraph/images/"
    clip_suggestion_subgraph = ClipSuggestionSubgraph()
    
    initial_state = ClipSuggestionState(
         video_path="...", 
         clipping_criteria="...", 
        comments=[...]
    )
    clip_suggestion_subgraph.make_image(image_dir)
    result = clip_suggestion_subgraph(initial_state)
    print(result)