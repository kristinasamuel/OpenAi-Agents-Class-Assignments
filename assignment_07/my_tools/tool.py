#  we use travily api to fetch the web information

from agents import function_tool
from my_config.config import tavily_client

@function_tool
def tavily_web_search(query: str) -> str:
    """Search the web using Tavily API and return results."""
    result = tavily_client.search(query)
    return str(result)