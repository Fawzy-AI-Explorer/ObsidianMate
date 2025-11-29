"""Conversation Cleaning Agent Instructions - English Locale."""

import os
from string import Template

INSTRUCTIONS = Template(
    "\n".join(
        [
            "You are an agent specialized in extracting transcripts from YouTube videos.",
            "Your primary role is to retrieve and provide accurate transcripts."
        ]
    )
)


def main():
    """Entry Point for the Program."""
    print(f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module. (❁´◡`❁)")


if __name__ == "__main__":
    main()
