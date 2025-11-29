"""
Module providing a simple program entry point and predefined instruction
template.
"""

import os
from string import Template

INSTRUCTIONS = Template(
    "\n".join(
        [
            "You are a manager agent that coordinates multiple sub-agents to assist users effectively to manage their notes in Obsidian.",
            "Your workflow is as follows:",
            "1. **Chat Agent**: Use the `ChatAgent` tool to handle general user queries and provide assistance.",
            "2. **Smart Notes Pipeline Agent**: When the user requests note-taking or summarization, utilize the `SmartNotesPipelineAgent` tool to filter irrelevant content",
            "   and generate concise summaries in markdown format.",
            "3. **MCP Obsidian Toolset**: For any interactions with the Obsidian application, such as creating, updating, or retrieving notes, employ the `MCPObsidianToolset` tool.",
        ]
    )
)


def main():
    """Entry Point for the Program."""
    print(
        f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module. Nothing to do ^_____^!"
    )


if __name__ == "__main__":
    main()
