from app.tools.base import BaseTool

class WebSearchTool(BaseTool):
    @property
    def name(self) -> str:
        return "web_search"

    @property
    def description(self) -> str:
        return "Search the web for real-time information or specific queries."

    @property
    def schema(self) -> dict:
        return {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query."
                }
            },
            "required": ["query"]
        }

    async def execute(self, query: str, **kwargs) -> str:
        # MVP Placeholder: Real implementation would use Tavily/Serper API.
        # This mocks a search result.
        return f"Mock search results for '{query}'. 1. Wikipedia: ... 2. News Article: ..."
