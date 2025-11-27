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
        ROOT_AGENT (str): Name for the root agent that orchestrates
            and delegates tasks across agents.
        SMART_NOTE_PIPELINE_AGENT (str): Name for the agent
            that processes and generates structured smart notes through the pipeline.
        EXTRACT_CONVERSATION_AGENT (str): Name for the agent responsible for extracting
            relevant conversation segments for processing.
    """

    CHAT_AGENT = "ChatAgent"
    CONVERSATION_FILTER_AGENT = "ConversationFilterAgent"
    CONVERSATION_SUMMARY_AGENT = "ConversationSummaryAgent"
    DRAWING_AGENT = "ConversationDrawingAgent"
    MARKDOWN_FORMATTER_AGENT = "MarkdownFormatterAgent"
    OBSIDIAN_CONTROLLER_AGENT = "ObsidianControllerAgent"
    OBSIDIAN_MATE_AGENT = "ObsidianMateAgent"
    SMART_NOTE_PIPELINE_AGENT = "SmartNotePipelineAgent"
    EXTRACT_CONVERSATION_AGENT = "ExtractConversationAgent"


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
