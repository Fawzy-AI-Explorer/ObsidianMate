"""
Module providing a simple program entry point and predefined instruction
template.
"""

import os
from string import Template

INSTRUCTIONS = Template(
    "\n".join(
        [
            "أنت مساعدٌ مُفيد. استخدم بحث جوجل للحصول على معلوماتٍ حديثة أو إذا لم تكن متأكدًا."
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
