"""Module for Agent Tool."""

import os
from google.adk.agents import SequentialAgent  # , ParallelAgent
from google.adk.tools.agent_tool import AgentTool

# from core.agents import SummaryAgent, ExtractConversationAgent, FilterAgent
from core.agents.summary_agent import SummaryAgent
from core.agents.extract_conversation_agent import ExtractConversationAgent
from core.agents.filter_agent import FilterAgent
from models.enums import AgentNameEnum


smart_notes_pipeline_tool = AgentTool(
    agent=SequentialAgent(
        name=AgentNameEnum.SMART_NOTE_PIPELINE_AGENT,
        sub_agents=[
            ExtractConversationAgent,
            FilterAgent,
            SummaryAgent,
        ],
    )
)


def main():
    """Entry Point for the Program."""
    print(f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module. (❁´◡`❁)")


if __name__ == "__main__":
    main()
