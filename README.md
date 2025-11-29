# ObsidianMate 🧠✨

![Python](https://img.shields.io/badge/Python-3.12%2B-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.118.3-009688?style=for-the-badge&logo=fastapi)
![Google ADK](https://img.shields.io/badge/Google_ADK-1.19.0-4285F4?style=for-the-badge&logo=google)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**ObsidianMate** is an intelligent, AI-powered assistant designed to supercharge your [Obsidian](https://obsidian.md/) note-taking workflow. Leveraging the power of Large Language Models (LLMs) like Gemini and GPT-4o, it acts as a "second brain" that helps you organize thoughts, summarize conversations, and interact directly with your Obsidian vault.

---

## 📖 Table of Contents

- [ObsidianMate 🧠✨](#obsidianmate-)
  - [📖 Table of Contents](#-table-of-contents)
  - [🧐 Project Overview](#-project-overview)
    - [Problem Statement](#problem-statement)
    - [Solution Statement](#solution-statement)
    - [Value Statement](#value-statement)
  - [🚀 Features](#-features)
  - [🏗 Architecture](#-architecture)
  - [📂 Project Structure](#-project-structure)
  - [🛠 Installation](#-installation)
    - [Prerequisites](#prerequisites)
    - [Steps](#steps)
  - [💻 Usage](#-usage)
    - [Running the API Server](#running-the-api-server)
    - [Running with ADK Web](#running-with-adk-web)
    - [Essential Tools and Utilities](#essential-tools-and-utilities)
  - [🤝 Contributing](#-contributing)
  - [📄 License](#-license)
  - [👏 Acknowledgments](#-acknowledgments)

---

## 🧐 Project Overview

### Problem Statement

Managing a growing knowledge base in Obsidian can be overwhelming. Users often struggle to quickly summarize discussions, organize unstructured thoughts into structured notes, and interact with their vault without breaking their flow.

### Solution Statement

ObsidianMate provides a unified AI agent interface that integrates directly with your workflow. It can hold conversations, filter irrelevant information, generate smart notes, and perform actions within your Obsidian vault using the Model Context Protocol (MCP).

### Value Statement

- **Boost Productivity**: Automate the tedious process of summarizing and formatting notes.
- **Seamless Integration**: Interact with your vault using natural language.
- **Flexible AI**: Powered by Google's ADK, supporting multiple LLM backends.

---

## 🚀 Features

- **🤖 Intelligent Chat Agent**: A general-purpose assistant capable of answering questions and helping with brainstorming.
- **📝 Smart Notes Pipeline**: Automatically filters irrelevant chit-chat from conversations and summarizes key points into clean, Markdown-formatted notes.
- **📂 Obsidian Integration**: Directly interacts with your Obsidian vault to read and manage notes (powered by MCP).
- **📺 YouTube Transcript Support**: Extract transcripts from YouTube videos for summarization and analysis.
- **🎨 Excalidraw Support** (Coming Soon): Future integration for handling visual notes and diagrams.

---

## 🏗 Architecture

ObsidianMate is built on a modular agentic architecture using the **Google Agent Development Kit (ADK)**.

1. **Root Agent (`ObsidianMate Agent`)**: The main entry point that orchestrates tasks.
2. **Sub-Agents**: Specialized agents for specific tasks:
    - `Chat Agent`: Handles general queries.
    - `Smart Notes Agent`: Processes and summarizes text.
    - `Obsidian Interaction Agent`: Manages vault operations via MCP.
    - `YouTube Transcript Agent`: Extracts transcripts from YouTube videos.
3. **Tools & MCP**: Uses the Model Context Protocol to securely connect to external tools like the Obsidian API and Dockerized services.
4. **Backend**: A robust **FastAPI** server manages sessions and API endpoints.

---

## 📂 Project Structure

```plaintext
ObsidianMate/
├── config/             # Configuration files (YAML)
├── docker/             # Docker configurations for MCP servers
├── scripts/            # Helper scripts for setup and running
├── src/
│   ├── controllers/    # Business logic controllers
│   ├── core/           # Core agent logic and tools
│   │   ├── obsidian_mate/
│   │   │   ├── agent.py        # Root agent definition
│   │   │   └── sub_agents/     # Specialized sub-agents
│   │   └── tools/              # Tool implementations
│   ├── models/         # Data models and enums
│   ├── routes/         # FastAPI route definitions
│   ├── stores/         # Data storage and LLM templates
│   └── utils/          # Utility functions
├── main.py             # Application entry point
├── pyproject.toml      # Project metadata and build config
└── requirements.txt    # Python dependencies
```

---

## 🛠 Installation

### Prerequisites

- Python 3.12 or higher
- Docker (for MCP servers)
- An Obsidian Vault

### Steps

1. **Clone the Repository**

    ```bash
    git clone https://github.com/Fawzy-AI-Explorer/ObsidianMate.git
    cd ObsidianMate
    ```

2. **Set up a Virtual Environment**

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configuration**

    - Ensure you have your `GOOGLE_API_KEY` and `OBSIDIAN_API_KEY` set in your environment or configuration files.
    - Check `config/config.yaml` for application settings.

---

## 💻 Usage

### Running the API Server

You can start the FastAPI server using the provided script:

```bash
sh scripts/run_app.sh
```

This will start the server at `http://0.0.0.0:8000`.

### Running with ADK Web

To use the Google ADK visual interface for testing and debugging agents:

```bash
adk web
```

### Essential Tools and Utilities

- **Docker**: Used to run the Obsidian MCP server. Ensure Docker is running before starting the agent if you plan to use vault interactions.
- **Google ADK**: The core framework driving the agent's behavior.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👏 Acknowledgments

**Authors:**

- Adham Allam
- Mohammad Fawzy
- Taha Ahmad
- Abdelrahman Salama

Special thanks to the open-source community and the teams behind **FastAPI**, **Google ADK**, and **Obsidian**.
