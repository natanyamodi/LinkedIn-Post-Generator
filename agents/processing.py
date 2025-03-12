from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage
from utils.utils import get_api_key  # Assuming you have utils.utils module
from langchain.utilities import DuckDuckGoSearchAPIWrapper
from langchain_community.tools import DuckDuckGoSearchResults
import json

def process_linkedin_post(user_input: str) -> str:
    """
    Analyzes user input with LLM, determines post type, and processes accordingly.

    Args:
        user_input: The user's input for the LinkedIn post.

    Returns:
        The generated or searched information, or an empty string if achievement.
    """

    model = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=get_api_key("google_api_key")
    )

    prompt = f"""
    Analyze the following user input and determine if it describes a personal achievement or a general topic for a LinkedIn post.

    User Input: "{user_input}"

    Instructions:
    - If the input describes a personal achievement (e.g., completing a certification, winning an award, reaching a milestone), respond with "achievement".
    - If the input is a general topic (e.g., industry trends, advice, discussion points), respond with "topic".
    - Respond with only one word, either "achievement" or "topic".
    """

    messages = [HumanMessage(content=prompt)]
    response = model.invoke(messages).content.lower()

    if "achievement" in response:
        return ""  # No information needed for achievement posts

    elif "topic" in response:
        # Perform DuckDuckGo search for topic-based posts
        search_wrapper = DuckDuckGoSearchAPIWrapper()
        search_tool = DuckDuckGoSearchResults(api_wrapper=search_wrapper, output_format="json")
        results = search_tool.run(user_input)
        return results

    else:
        # Default to topic search if LLM response is unclear.
        search_wrapper = DuckDuckGoSearchAPIWrapper()
        search_tool = DuckDuckGoSearchResults(api_wrapper=search_wrapper, output_format="json")
        results = search_tool.run(user_input)
        return results