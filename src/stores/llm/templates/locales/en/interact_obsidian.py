"""Conversation Cleaning Agent Instructions - English Locale."""

import os
from string import Template

INSTRUCTIONS = Template(
    "\n".join(
        [
            "You are an agent specialized in interacting with Obsidian.",
            "Your primary role is to create, update, and manage notes in Obsidian based on user inputs and conversation context."
        ]
    )
)


def main():
    """Entry Point for the Program."""
    print(f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module. (❁´◡`❁)")


if __name__ == "__main__":
    main()
