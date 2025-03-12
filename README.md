# Multi-AI Agent System for LinkedIn Post Generation (LangGraph Implementation)

This project implements a sophisticated multi-AI agent system to automate the creation of engaging LinkedIn posts using LangGraph for workflow management. It leverages LangChain, Google Gemini 2.0 Flash (or another LLM), and DuckDuckGo for information gathering (when applicable), content generation, editing, and reviewing.

## Features

* **LangGraph Workflow Orchestration:** Uses LangGraph to define and manage the multi-step workflow, ensuring a structured and reliable process.
* **Modular AI Agents:** Implements distinct AI agents for information gathering (when needed), content generation, editing, and reviewing, promoting code organization and maintainability.
* **Automated LinkedIn Post Creation:** Generates complete LinkedIn posts from user input, handling both general topics and personal achievements.
* **Intelligent Post Type Detection:** Uses an LLM to determine if the user input describes a general topic or a personal achievement, and adjusts the workflow accordingly.
* **Conditional Information Gathering:** Leverages DuckDuckGo search to retrieve relevant information only when the post is about a general topic, avoiding unnecessary searches for achievement posts.
* **Content Generation with LLM:** Uses Google Gemini 2.0 Flash (or a configured LLM) to generate the initial post content, tailored to the post type.
* **Automated Content Editing:** Refines the generated content for clarity and engagement.
* **Automated Content Review:** Provides a final review step to ensure the post meets quality standards.
* **Try it out:** A live demo is available at https://linkedin-post-generator-tutazygr8zdjvbyhrveagm.streamlit.app/
