from langgraph.graph import StateGraph, END, add_messages
from typing import TypedDict, Annotated, List
from langchain.schema import BaseMessage, HumanMessage
from agents.content_generation import generate_linkedin_post
from agents.editing import edit_post
from agents.reviewing import review_post
from agents.processing import process_linkedin_post

class State(TypedDict):
    messages: Annotated[List[BaseMessage], add_messages]
    user_input: str
    information: str
    post: str
    edited_post: str
    reviewed_post: str
    is_achievement: bool

def gather_info(state: State) -> State:
    print("Gathering info")
    user_input = state["user_input"]
    information = process_linkedin_post(user_input)
    is_achievement = True if information == "" else False
    return {"messages": state["messages"], "user_input": user_input, "information": information, "post": None, "edited_post": None, "reviewed_post": None, "is_achievement": is_achievement}

def generate_content(state: State) -> State:
    print("Generating content")
    user_input = state["user_input"]
    information = state["information"]
    post = generate_linkedin_post(user_input, information, is_achievement=state.get("is_achievement", False))
    return {"messages": state["messages"] + [HumanMessage(content=post)], "user_input": user_input, "information": information, "post": post, "edited_post": None, "reviewed_post": None, "is_achievement": state.get("is_achievement", False)}

def generate_achievement_content(state: State) -> State:
    print("Generating achievement content")
    user_input = state["user_input"]
    post = generate_linkedin_post(user_input, "", is_achievement=True)
    return {"messages": state["messages"] + [HumanMessage(content=post)], "user_input": user_input, "information": "", "post": post, "edited_post": None, "reviewed_post": None, "is_achievement": True}

def edit_content(state: State) -> State:
    print("Editing content")
    post = state["post"]
    edited_post = edit_post(post)
    return {"messages": state["messages"] + [HumanMessage(content=edited_post)], "user_input": state["user_input"], "information": state["information"], "post": state["post"], "edited_post": edited_post, "reviewed_post": None, "is_achievement": state.get("is_achievement", False)}

def review_content(state: State) -> State:
    print("Reviewing content")
    user_input = state["user_input"]
    edited_post = state["edited_post"]
    reviewed_post = review_post(edited_post, user_input)
    return {"messages": state["messages"] + [HumanMessage(content=reviewed_post)], "user_input": user_input, "information": state["information"], "post": state["post"], "edited_post": edited_post, "reviewed_post": reviewed_post, "is_achievement": state.get("is_achievement", False)}

def main_workflow(user_input: str):
    initial_state: State = {
        "messages": [HumanMessage(content=f"User input: {user_input}")],
        "user_input": user_input,
        "information": None,
        "post": None,
        "edited_post": None,
        "reviewed_post": None,
        "is_achievement": False,
    }

    graph = StateGraph(State)
    graph.add_node("gather_info", gather_info)
    graph.add_node("generate_content", generate_content)
    graph.add_node("generate_achievement_content", generate_achievement_content)
    graph.add_node("edit_content", edit_content)
    graph.add_node("review_content", review_content)

    graph.set_entry_point("gather_info") # changed entry point.
    graph.add_edge("gather_info", "generate_content")
    graph.add_edge("generate_content", "edit_content")
    graph.add_edge("generate_achievement_content", "edit_content")
    graph.add_edge("edit_content", "review_content")
    graph.add_edge("review_content", END)

    chain = graph.compile()
    result = chain.invoke(initial_state)
    return result["reviewed_post"]