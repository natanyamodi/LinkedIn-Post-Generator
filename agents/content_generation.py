from langchain_google_genai import ChatGoogleGenerativeAI
from utils.utils import get_api_key
from langchain.schema import HumanMessage

def generate_linkedin_post(user_input: str, information: str) -> str:
    """Generates a LinkedIn post with a human-sounding tone using Gemini 2.0 Flash."""
    model = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=get_api_key("google_api_key")
    )

    prompt = f"""
    **Role:** You are a seasoned LinkedIn content strategist with a decade of experience in crafting engaging and informative posts.
    **Goal:** To create a compelling LinkedIn post that sparks conversation and provides value to the reader, based on the user's input and provided information.
    **Backstory:** You've worked with numerous thought leaders and startups, helping them build their online presence. You understand the nuances of LinkedIn's audience and know how to capture their attention.

    **Task:** Based on the user input: "{user_input}" and the following information: {information}, write a LinkedIn post.
    Ensure the post is:
    - Engaging and conversational.
    - Factually accurate.
    - Relevant to a professional audience.
    - Structured for easy reading.
    - Includes a call to action.

    Write the post.
    """
    messages = [HumanMessage(content=prompt)]
    response = model.invoke(messages)
    return response.content