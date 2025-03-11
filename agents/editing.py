from langchain_google_genai import ChatGoogleGenerativeAI
from utils.utils import get_api_key
from langchain.schema import HumanMessage

def edit_post(post: str) -> str:
    """Edits the post for grammar, clarity, and engagement using Gemini 2.0 Flash."""
    model = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=get_api_key("google_api_key")
    )

    prompt = f"""
    **Role:** You are a meticulous editor specializing in LinkedIn content.
    **Goal:** To refine the given post for maximum clarity, impact, and engagement, ensuring it is error-free and resonates with a professional audience.
    **Backstory:** You've edited countless articles, posts, and marketing materials, honing your ability to polish content to perfection.

    **Task:** Edit the following LinkedIn post: "{post}".
    Focus on:
    - Grammar and spelling.
    - Clarity and conciseness.
    - Engagement and readability.
    - Ensuring the post is factually correct.
    - Enhancing the call to action, if applicable.
    - Make sure the post is ready to be published.

    Return the edited post.
    """
    messages = [HumanMessage(content=prompt)]
    response = model.invoke(messages)
    return response.content