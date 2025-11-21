"""
Template parser for localized prompt handling.
"""

import os
from typing import Optional


class TemplateParser:
    """
    A parser for loading and rendering localized templates.

    Attributes:
        current_path (str): The absolute path to the directory containing this file.
        default_language (str): The default fallback language (default: `"en"`).
        language (str | None): The currently active language for template parsing.
    """

    def __init__(
        self, language: Optional[str] = None, default_language: str = "en"
    ) -> None:
        """
        Initialize the template parser.

        Args:
            language (Optional[str]): The desired language to use. If `None`,
                the default language will be applied.
            default_language (str): The fallback language code (default is `"en"`).
        """

        self.current_path = os.path.dirname(os.path.abspath(__file__))
        self.default_language = default_language
        self.language = None
        self.set_language(language)  # type: ignore

    def set_language(self, language: str):
        """
        Set the current language for template parsing.

        Args:
            language (str): The language code to set. If the language
                directory does not exist, it falls back to the default language.
        """

        if not language:
            language = self.default_language

        language_path = os.path.join(self.current_path, "locales", language)
        if os.path.exists(language_path):
            self.language = language
        else:
            self.language = self.default_language

    def get(self, group: str, key_: str, vars_: dict = {}) -> str | None:
        """
        Retrieve and render a localized template string.

        Args:
            group (str): The group or file name (without extension) under
                the `locales/<language>/` directory.
            key_ (str): The key (attribute) inside the template module.
            vars_ (dict, optional): Variables for substitution in the template.
                Defaults to an empty dictionary.

        Returns:
            str | None: The rendered template string, or `None` if the template
            cannot be found or loaded.
        """

        if not group or not key_:
            return None

        group_path = os.path.join(
            self.current_path, "locales", self.language, f"{group}.py"  # type: ignore
        )
        targeted_language = self.language
        if not os.path.exists(group_path):
            group_path = os.path.join(
                self.current_path, "locales", self.default_language, f"{group}.py"
            )
            targeted_language = self.default_language
        if not os.path.exists(group_path):
            return None

        module = __import__(
            f"stores.llm.templates.locales.{targeted_language}.{group}",
            fromlist=[group],
        )
        if not module:
            return None

        key_attribute = getattr(module, key_)
        return key_attribute.substitute(vars_)


def main():
    """Entry Point for the Program."""
    print(
        f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module. Nothing to do ^_____^!"
    )


if __name__ == "__main__":
    main()
