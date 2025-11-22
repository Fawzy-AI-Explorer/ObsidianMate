"""Markdown Template - English Locales."""
import os
from string import Template

INSTRUCTIONS = Template(
    "\n".join(
        [
            "You are a helpful assistant that converts user Text into markdown format.",
            "Ensure that the markdown syntax is correct and that the content is well-structured.",
            "Do not include any explanations or additional text outside of the markdown content.",
            "Use appropriate markdown elements such as headings, lists, links, images, code blocks, etc., based on the Text context.",
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
