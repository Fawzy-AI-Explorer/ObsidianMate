"""Conversation Summarizing Agent Instructions - English Locale."""

import os
from string import Template

INSTRUCTIONS = Template(
    "\n".join(
    [
        "You are a helpful Text filtering and summarizing agent.",
        "Format the summary using markdown Format, including headings, bullet points, and code blocks where appropriate.",
        "save the summary in a variable called `conversation_summary`.",
    ]
))


def main():
    """Entry Point for the Program."""
    print(f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module. (❁´◡`❁)")


if __name__ == "__main__":
    main()
