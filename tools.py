from livekit.agents import llm
from duckduckgo_search import DDGS
from typing import Annotated

class AssistantFnc:
    @llm.function_tool
    def search(self, query: str):
        """Search the web for information.

        Args:
            query: The query to search for.
        """
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=3))
        return str(results)
