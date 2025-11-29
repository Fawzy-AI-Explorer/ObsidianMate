"""Conversation Summarizing Agent Instructions - English Locale."""

import os
from string import Template

INSTRUCTIONS = Template(
    "\n".join(
        [
            "You are a helpfull conversation filtering and summarizing agent.",
            "Your workflow is as follows:"
            "1. **Summarize Conversation**: use `ConversationSummaryAgent` tool to summarize the conversation.",
            "save the summary in a variable called `final_notes`.",
        ]
    )
)


def main():
    """Entry Point for the Program."""
    print(f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module. (❁´◡`❁)")


if __name__ == "__main__":
    main()
