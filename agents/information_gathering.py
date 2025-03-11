from tavily import TavilyClient
from utils.utils import get_api_key
import json

def gather_information(user_input: str) -> str:
    """Gathers and summarizes information from Tavily."""
    tavily_api_key = get_api_key("tavily_api_key")
    client = TavilyClient(api_key=tavily_api_key)
    results = client.search(user_input)
    if results and results.get('results'):
      structured_results = []
      for result in results['results']:
        structured_results.append({
            "title": result.get('title'),
            "url": result.get('url'),
            "content": result.get('content')
        })
      return json.dumps(structured_results, indent=2)
    else:
      return "No relevant information found."