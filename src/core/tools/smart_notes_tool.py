"""Module for Agent Tool."""

import os
from google.adk.agents import SequentialAgent# , ParallelAgent
from google.adk.tools import AgentTool
from core.agents import filter_agent, summary_agent
from models.enums import AgentNameEnum


smart_notes_pipeline_tool = AgentTool(
    SequentialAgent(
        name=AgentNameEnum.SMART_NOTE_PIPELINE_AGENT,
        sub_agents=[
            filter_agent,
            summary_agent,
        ],
    )
)


def main():
    """Entry Point for the Program."""
    print(f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module. (❁´◡`❁)")


if __name__ == "__main__":
    main()
