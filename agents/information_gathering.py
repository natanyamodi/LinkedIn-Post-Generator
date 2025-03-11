from tavily import TavilyClient
from utils.utils import get_api_key
import json

def gather_information(user_input: str) -> str:
    """Gathers information from Tavily and returns raw results."""
    tavily_api_key = get_api_key("tavily_api_key")
    client = TavilyClient(api_key=tavily_api_key)
    results = client.search(user_input)

    return json.dumps(results, indent=2) #or return results