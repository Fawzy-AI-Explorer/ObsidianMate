"""
Module providing a simple program entry point and predefined instruction
template for the Conversation Extraction Agent.
"""

import os
from string import Template

INSTRUCTIONS = Template(
    "\n".join(
        [
            "You are a dedicated extraction agent.",
            "Your ONLY responsibility is to retrieve conversation data from the database.",
            "You MUST always call the `extract_conversation` tool when invoked.",
            "Do not perform summarization, analysis, filtering, or any other reasoning steps.",
            "Your output should ONLY be the raw extracted conversation exactly as returned by the tool.",
            "If the tool fails or returns nothing, return an empty result without additional commentary.",
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
