# Multi-AI Agent System for LinkedIn Post Generation (LangGraph Implementation)

This project implements a sophisticated multi-AI agent system to automate the creation of engaging LinkedIn posts using LangGraph for workflow management. It leverages LangChain, Google Gemini 2.0 Flash (or another LLM), and DuckDuckGo for information gathering, content generation, editing, and reviewing.

## Features

* **LangGraph Workflow Orchestration:** Uses LangGraph to define and manage the multi-step workflow, ensuring a structured and reliable process.
* **Modular AI Agents:** Implements distinct AI agents for information gathering, content generation, editing, and reviewing, promoting code organization and maintainability.
* **Automated LinkedIn Post Creation:** Generates complete LinkedIn posts from user input, including information gathering, content creation, editing, and review.
* **Information Gathering:** Leverages DuckDuckGo search to retrieve relevant information based on the user's topic.
* **Content Generation with LLM:** Uses Google Gemini 2.0 Flash (or a configured LLM) to generate the initial post content.
* **Automated Content Editing:** Refines the generated content for clarity and engagement.
* **Automated Content Review:** Provides a final review step to ensure the post meets quality standards.
* **Try it out:** A live demo is available at https://linkedin-post-generator-tutazygr8zdjvbyhrveagm.streamlit.app/
## Architecture

The system is built using LangGraph to define a stateful graph that represents the workflow. Each node in the graph corresponds to an AI agent responsible for a specific task.

1.  **Information Gathering (gather\_info):**
    * Uses `langchain_community.utilities.DuckDuckGoSearchAPIWrapper` to gather information.
    * Stores the gathered information in the state.
2.  **Content Generation (generate\_content):**
    * Uses an LLM to generate the initial post content based on the gathered information.
    * Stores the generated post in the state.
3.  **Content Editing (edit\_content):**
    * Edits the generated post for clarity and quality.
    * Stores the edited post in the state.
4.  **Content Review (review\_content):**
    * Reviews the edited post and provides a final version.
    * Stores the reviewed post in the state.
5.  **LangGraph State Management:**
    * Manages the state of the workflow, passing information between agents.
