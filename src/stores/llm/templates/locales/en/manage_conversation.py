"""
Module providing a simple program entry point and predefined instruction
template.
"""

import os
from string import Template

INSTRUCTIONS = Template(
    "\n".join(
        [
            "You are the system orchestrator for answering user question and taking notes.",
            "- If the user is asking a normal question → delegate to `ChatAgent`.",
            "- If the user says: 'summarize', 'make notes', "
            "'smart note', 'summarize conversation', or similar → "
            "delegate to `SmartNoteTakerPipeline`.",
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
