from langchain_google_genai import ChatGoogleGenerativeAI
from utils.utils import get_api_key
from langchain.schema import HumanMessage

def review_post(post: str, user_input: str) -> str:
    """Reviews the post and returns only the final, polished post."""
    model = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=get_api_key("google_api_key")
    )

    prompt = f"""
    **Role:** You are a senior content editor focused on preparing posts for LinkedIn.
    **Goal:** To ensure the post is accurate, engaging, and ready for direct publication on LinkedIn, removing any extraneous labels or formatting.
    **Backstory:** You've edited countless LinkedIn posts and understand the platform's requirements for clean, ready-to-publish content.

    **Task:** Review the following LinkedIn post: "{post}".
    User Input: "{user_input}".
    Ensure it is:
    - Accurate and relevant.
    - Engaging and professional.
    - Free of any labels like "Headline," "Body," or "Call to Action."
    - Ready for direct posting on LinkedIn.

    Return ONLY the final, polished LinkedIn post, without any labels or extraneous formatting.
    """
    messages = [HumanMessage(content=prompt)]
    response = model.invoke(messages)
    return response.content