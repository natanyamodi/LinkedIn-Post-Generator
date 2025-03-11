from langchain.utilities import DuckDuckGoSearchAPIWrapper
from langchain_community.tools import DuckDuckGoSearchResults
import json


def gather_information(user_input: str) -> str:
    """Gathers and summarizes information from DuckDuckGo using LangChain with custom formatting."""
    search_wrapper = DuckDuckGoSearchAPIWrapper()
    search_tool = DuckDuckGoSearchResults(api_wrapper=search_wrapper, output_format="json") #using json output format
    results = search_tool.run(user_input)

    return results