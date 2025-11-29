# ObsidianMate: Your AI-Powered Second Brain for Obsidian

### Problem Statement
In the age of information overload, maintaining a personal knowledge base (PKM) like Obsidian can quickly become a daunting task. Users often struggle with:
- **Friction in capturing ideas**: Converting unstructured thoughts or conversations into structured notes takes time and mental energy.
- **Information silos**: Valuable information from YouTube videos, articles, or chats often gets lost or remains disconnected from the main knowledge base.
- **Workflow interruptions**: Switching context between consuming content (e.g., watching a tutorial) and documenting it breaks the flow state.
- **Maintenance overhead**: Organizing, tagging, and linking notes manually is tedious and often neglected, leading to a "digital junkyard."

ObsidianMate solves this by acting as an intelligent bridge between your raw inputs (voice, text, videos) and your structured Obsidian vault. It automates the heavy lifting of summarization, formatting, and organization, allowing users to focus on thinking and connecting ideas.

### Why agents?
Agents are the ideal solution for this problem because PKM management is inherently multi-modal and multi-step. A simple script or chatbot isn't enough; we need a system that can:
1.  **Reason and Plan**: Understand a high-level intent like "Research this topic and create a note" and break it down into steps (search, summarize, format, save).
2.  **Use Tools**: Actively interact with the outside world (YouTube API, Google Search) and the local environment (Obsidian file system).
3.  **Route Tasks**: Delegate specific jobs to specialized sub-agents (e.g., a "Transcript Agent" for video processing vs. an "Obsidian Agent" for file manipulation).
4.  **Maintain Context**: Remember the history of the conversation and the state of the vault to provide relevant assistance.

Agents transform the interaction from a rigid command-line experience to a fluid, natural language collaboration.

### What you created
I created **ObsidianMate**, a hierarchical multi-agent system powered by Google's Agent Development Kit (ADK). The architecture is designed to be modular and extensible:

**Overall Architecture:**
- **Root Agent (ObsidianMate Agent)**: The central orchestrator that receives user queries and routes them to the appropriate sub-agent. It uses `LiteLLM` to support various models (Gemini, GPT-4o).
- **Specialized Sub-Agents**:
    - **Chat Agent**: Handles general conversation and queries.
    - **Smart Notes Agent**: A pipeline designed to take raw input and convert it into structured Obsidian notes using predefined templates.
    - **Obsidian Interaction Agent**: Manages file operations within the vault (reading, writing, listing files).
    - **YouTube Transcript Agent**: Fetches and processes transcripts from YouTube videos for summarization.
    - **Excalidraw Agent** (Experimental): Intended for interacting with visual notes.
- **Tooling Layer**: A set of Python tools that agents use to perform actions, such as `youtube_transcript_tool`, `obsidian_interaction_tool`, and `google_search_tool`.
- **Interface**: The system exposes a FastAPI backend that can be connected to various frontends (CLI, Web, or potentially an Obsidian plugin).

### Demo
*Imagine this workflow:*

1.  **User**: "Hey, I just watched this video on Reinforcement Learning [URL]. Can you summarize the key points and save it to my 'AI/Reinforcement Learning' folder?"
2.  **ObsidianMate (Root Agent)**: Recognizes the intent involves video processing and file creation.
3.  **Transcript Agent**: Fetches the transcript of the video.
4.  **Smart Notes Agent**: Processes the transcript, extracts key insights, and formats them into a clean Markdown note.
5.  **Obsidian Interaction Agent**: Saves the formatted note to `docker/vault/AI/Reinforcement Learning/Video Summary.md`.
6.  **User**: Sees the new note appear instantly in their Obsidian vault, ready for review.

*(Note: A video demo would show the terminal output of the agents coordinating these steps and the file appearing in the Obsidian file explorer.)*

### The Build
ObsidianMate was built using a modern Python stack focused on agentic workflows:

- **Google ADK (Agent Development Kit)**: The core framework for defining agents, tools, and their interactions. It provided the structure for the hierarchical agent pattern.
- **Google Gemini & OpenAI GPT-4o**: The intelligence behind the agents. Gemini 1.5 Pro was particularly useful for its large context window when processing long video transcripts.
- **LiteLLM**: Used as a model abstraction layer, allowing the system to switch between different LLM providers easily.
- **FastAPI**: Serves the agent as a REST API, making it accessible to external applications.
- **YouTube Transcript API**: For extracting text from video content.
- **Model Context Protocol (MCP)**: Implemented concepts to standardize how the AI interacts with the local file system (Obsidian vault).
- **Docker**: For containerizing the application and ensuring a consistent environment.

### If I had more time, this is what I'd do
- **Full Obsidian Plugin**: Currently, the system runs as a backend service. I would build a proper Obsidian plugin (TypeScript) to allow users to chat with the agent directly within the Obsidian interface.
- **RAG Implementation**: Implement a robust Retrieval-Augmented Generation system over the entire vault. This would allow the agent to answer questions like "What did I write about neural networks last month?" by semantically searching the user's notes.
- **Visual Note Generation**: Fully implement the Excalidraw agent to allow the AI to generate diagrams and mind maps from text descriptions.
- **Active Learning**: Allow the agent to learn from the user's editing patterns to improve its note-taking style over time.
