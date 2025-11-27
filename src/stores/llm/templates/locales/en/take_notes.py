"""Conversation Summarizing Agent Instructions - English Locale."""

import os
from string import Template

INSTRUCTIONS = Template(
    "\n".join(
        [
            "You are a helpfull conversation filtering and summarizing agent.",
            "Your workflow is as follows:"
            "The conversation will be available in memory through `preload_memory` tool"
            "1. **Filter Conversation**: use `ConversationFilterAgent` tool to clean and filter conversation."
            # "2. **Summarize Conversation**: user `ConversationSummaryAgent` tool to summarize the conversation.",
        ]
    )
)


def main():
    """Entry Point for the Program."""
    print(f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module. (❁´◡`❁)")


if __name__ == "__main__":
    main()
