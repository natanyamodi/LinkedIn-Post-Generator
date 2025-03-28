from langchain_google_genai import ChatGoogleGenerativeAI
from utils.utils import get_api_key
from langchain.schema import HumanMessage
import json

def generate_linkedin_post(user_input: str, information: str, is_achievement: bool = False) -> str:
    """Generates a LinkedIn post with a human-sounding tone using Gemini 2.0 Flash,
    handling both achievement and information-based posts."""
    model = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=get_api_key("google_api_key")
    )

    if is_achievement:
        # Prompt for achievement posts
        prompt = f"""
        **Role:** You're a seasoned LinkedIn content creator who excels at sharing personal achievements in an engaging way.

        **Goal:** Write a compelling LinkedIn post about the user's achievement. The goal is to inspire, share a personal story, and encourage congratulations.

        **Task:** Here's the user's achievement: "{user_input}"

        Write a fun, engaging, and personal LinkedIn post while maintaining professionalism.

        Keep these things in mind:

        * Focus on your personal experience and the journey.
        * Make it conversational and easy to read.
        * Highlight the impact of the achievement.
        * Structure it so it's easy to follow.
        * Try to add a personal touch and make it relatable.

        Write the post.
        """
    else:
        # Prompt for information-based posts
        try:
            information_list = json.loads(information)
        except json.JSONDecodeError:
            information_list = []

        prompt = f"""
        **Role:** You're a seasoned LinkedIn content creator. You've been crafting engaging posts for years, and you know how to make complex topics relatable.

        **Goal:** Write a compelling LinkedIn post based on the user's topic and the information I provide. The goal is to inform, engage, and spark conversation.

        **Task:** Here's the user's topic: "{user_input}"

        Here's some information I've gathered on the topic:
        {json.dumps(information_list, indent=2)}

        Write a fun and engaging LinkedIn post while also maintaining professionalism.

        Keep these things in mind:

        * Make it conversational and easy to read.
        * Stick to the facts found in the provided information.
        * Keep it relevant to a professional audience.
        * Structure it so it's easy to follow.
        * End with a call to action to encourage engagement.
        * If you mention specific facts or data, weave in where that information came from in a natural way. You don't need to add a formal citation, but if you mention a specific study or article, you can mention it in the flow of the post. For example, you can say "According to a recent study..." or "As mentioned in the article...". If you use a website, then include the url.

        Write the post.
        """

    messages = [HumanMessage(content=prompt)]
    response = model.invoke(messages)
    return response.content