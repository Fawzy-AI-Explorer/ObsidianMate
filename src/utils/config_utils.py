# pylint: disable=invalid-name

"""
Utilities for loading and handling configuration files.
"""

import os
from typing import Optional
from pathlib import Path
from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict, YamlConfigSettingsSource
from utils.logging_utils import setup_logger

logger = setup_logger(
    log_file=__file__,
    log_to_console=False,
    file_mode="a",
)


class Settings(BaseSettings):
    """
    Application configuration container that loads required credentials and metadata
    from env, .env, YAML, or secrets files.
    """

    # .env
    GH_PAT: SecretStr = Field(...)
    WSL_PASS: SecretStr = Field(...)
    SQLITE_DB_PATH: str = Field(...)
    GOOGLE_API_KEY: SecretStr = Field(...)
    OPENAI_API_KEY: Optional[SecretStr] = Field(default=None)
    OBSIDIAN_API_KEY: SecretStr = Field(...)
    OBSIDIAN_HOST: str = Field(...)

    # .yaml
    APP_NAME: str = Field(...)
    APP_VERSION: str = Field(...)

    PATH_LOGS: str = Field(...)
    PATH_DATA_ROOT: str = Field(...)
    PATH_ASSETS_ROOT: str = Field(...)
    PATH_MODELS_ROOT: str = Field(...)
    PATH_OUTPUT_ROOT: str = Field(...)

    RETRY_ATTEMPS: int = Field(...)
    RETRY_EXP_BASE: int = Field(...)
    RETRY_INITAL_DELAY: int = Field(...)
    RETRY_HTTP_STATUS_CODE: list[int] = Field(...)

    SQLITE_DB_PATH: str = Field(...)

    DEFAULT_MODEL_NAME: str = Field(...)
    CHAT_MODEL_NAME: str = Field(default="")
    FILTER_MODEL_NAME: str = Field(default="")
    SUMMARIZE_MODEL_NAME: str = Field(default="")
    MARKDOWN_MODEL_NAME: str = Field(default="")
    DIAGRAM_MODEL_NAME: str = Field(default="")
    WRITE_MODEL_NAME: str = Field(default="")
    EXTRACT_MODEL_NAME: str = Field(default="")
    YT_TRANSCRIPT_MODEL_NAME: str = Field(default="")

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls,
        init_settings,
        env_settings,
        dotenv_settings,
        file_secret_settings,
    ):
        return (
            init_settings,  # kwargs passed directly to Settings()
            env_settings,  # Environment variables
            dotenv_settings,  # .env file
            YamlConfigSettingsSource(
                settings_cls,
                yaml_file=Path("config/config.yaml"),
                yaml_file_encoding="utf-8",
            ),  # YAML file
            file_secret_settings,
        )

    def model_post_init(self, __context):  # pylint: disable=[W0221]
        """
        After loading all settings, fill any missing model names using DEFAULT_MODEL_NAME
        """
        if not self.CHAT_MODEL_NAME:
            self.CHAT_MODEL_NAME = self.DEFAULT_MODEL_NAME
        if not self.FILTER_MODEL_NAME:
            self.FILTER_MODEL_NAME = self.DEFAULT_MODEL_NAME
        if not self.SUMMARIZE_MODEL_NAME:
            self.SUMMARIZE_MODEL_NAME = self.DEFAULT_MODEL_NAME
        if not self.MARKDOWN_MODEL_NAME:
            self.MARKDOWN_MODEL_NAME = self.DEFAULT_MODEL_NAME
        if not self.DIAGRAM_MODEL_NAME:
            self.DIAGRAM_MODEL_NAME = self.DEFAULT_MODEL_NAME
        if not self.WRITE_MODEL_NAME:
            self.WRITE_MODEL_NAME = self.DEFAULT_MODEL_NAME
        if not self.EXTRACT_MODEL_NAME:
            self.EXTRACT_MODEL_NAME = self.DEFAULT_MODEL_NAME


def get_settings() -> Settings:
    """
    Constructs and returns a validated Settings object that centralizes configuration
    for the application.
    Returns:
        Settings: A validated Settings instance containing application configuration.
    """

    logger.info("Loading application settings.")
    return Settings()  # type: ignore


def main():
    """Entry Point for the Program."""
    print(f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module.\n")
    # Usage

    settings = get_settings()

    print(settings.APP_NAME)  # From config.yaml
    print(settings.APP_VERSION)  # From config.yaml
    print(settings.GH_PAT)  # From .env
    print(settings.OPENAI_API_KEY)
    print(settings.CHAT_MODEL_NAME)


if __name__ == "__main__":
    main()
