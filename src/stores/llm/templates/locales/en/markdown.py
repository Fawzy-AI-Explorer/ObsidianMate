"""Markdown Template - English Locales."""
import os
from string import Template

INSTRUCTIONS = Template(
    "\n".join(
    [
        "You are a helpful markdown formatting agent.",
        "- **Format Response**: Given the user's input, format your response strictly in markdown syntax.",
        "-  **Use Markdown Elements**: Utilize appropriate markdown elements such as headings, lists, code blocks, links, images, and emphasis to enhance readability.",
    ]
))



def main():
    """Entry Point for the Program."""
    print(
        f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module. Nothing to do ^_____^!"
    )


if __name__ == "__main__":
    main()
