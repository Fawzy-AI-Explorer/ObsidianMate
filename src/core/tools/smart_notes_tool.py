"""Module for Agent Tool."""

import os
from google.adk.agents import SequentialAgent  # , ParallelAgent
from google.adk.tools.agent_tool import AgentTool

# from core.agents import SummaryAgent, ExtractConversationAgent, FilterAgent
from core.obsidian_mate.sub_agents.summary_agent import conversation_summary_agent
from core.obsidian_mate.sub_agents.extract_conversation_agent import ExtractConversationAgent
from core.obsidian_mate.sub_agents.filter_agent import conversation_filter_agent
from models.enums import AgentNameEnum


smart_notes_pipeline_tool = AgentTool(
    agent=SequentialAgent(
        name=AgentNameEnum.SMART_NOTE_PIPELINE_AGENT,
        sub_agents=[
            ExtractConversationAgent,
            conversation_filter_agent,
            conversation_summary_agent,
        ],
    )
)


def main():
    """Entry Point for the Program."""
    print(f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module. (❁´◡`❁)")


if __name__ == "__main__":
    main()
