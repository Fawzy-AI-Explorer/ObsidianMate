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
            "You can do the following:",
            "1. **Chat Agent**: Use the `ChatAgent` tool to handle general user queries and provide assistance.",
            "2. **Smart Notes Pipeline Agent**: When the user requests note-taking or summarization, utilize the `TextSummaryAgent` tool to filter irrelevant content",
            "   and generate concise summaries in markdown format.",
            "3. **MCP Obsidian Toolset**: For any interactions with the Obsidian application, such as creating, updating, or retrieving notes, employ the `ObsidianInteractionAgent` tool to perform the necessary actions.",
            "4. **YouTube Transcript Agent**: If the user needs transcripts from YouTube videos, leverage the `YouTubeTranscriptAgent` tool to extract and provide the required transcripts. You should prompt it as 'Extract the transcript of <video_url>' after that you will find the transcript in the `video_transcript` variable.",
            "RULES:",
            "You can only use ONE tool at a time.",
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
