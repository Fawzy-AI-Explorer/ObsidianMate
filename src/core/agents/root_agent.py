""" "Clean Agent Module."""

import os
from google.adk.agents import SequentialAgent
from google.genai import types
from utils.config_utils import get_settings
from models.enums import AgentNameEnum
from stores.llm.templates import TemplateParser
from core.agents import chat_agent

app_settings = get_settings()
template_parser = TemplateParser()

retry_config = types.HttpRetryOptions(
    attempts=app_settings.RETRY_ATTEMPS,
    exp_base=app_settings.RETRY_EXP_BASE,
    initial_delay=app_settings.RETRY_INITAL_DELAY,
    http_status_codes=app_settings.RETRY_HTTP_STATUS_CODE,
)

root_agent = SequentialAgent(
    name=AgentNameEnum.ROOT_AGENT,
    sub_agents=[chat_agent],
)


def main():
    """Entry Point for the Program."""
    print(
        f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module. Nothing to do ^_____^!"
    )


if __name__ == "__main__":
    main()
