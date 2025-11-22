"""
Agents Name Enumeration Module.
"""

import os
from enum import StrEnum


class AgentNameEnum(StrEnum):
    """Enumeration of agent names used across the system.

    Attributes:
        CHAT_AGENT (str): Name for the agent that interacts with the user and answers questions.
        CONVERSATION_FILTER_AGENT (str): Name for the agent
            that removes unhelpful or irrelevant conversation text.
        SUMMARY_AGENT (str): Name for the agent that summarizes conversations.
        DRAWING_AGENT (str): Name for the agent responsible for creating diagrams and flowcharts.
        MARKDOWN_FORMATTER_AGENT (str): Name for the agent
            that structures content into Markdown format.
        OBSIDIAN_CONTROLLER_AGENT (str): Name for the agent
            that manages Obsidian note creation and updates.
    """

    CHAT_AGENT = "Chat_Agent"
    CONVERSATION_FILTER_AGENT = "Conversation_Filter_Agent"
    SUMMARY_AGENT = "Summary_Agent"
    DRAWING_AGENT = "Drawing_Agent"
    MARKDOWN_FORMATTER_AGENT = "Markdown_Formatter_Agent"
    OBSIDIAN_CONTROLLER_AGENT = "Obsidian_Controller_Agent"
    ROOT_AGENT = "Root_Agent"


def main():
    """Entry point for running the module directly.

    Prints a simple welcome message including the module name,
    mainly used for debugging or verification purposes.
    """
    print(
        f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module. Nothing to do ^_____^!"
    )


if __name__ == "__main__":
    main()
