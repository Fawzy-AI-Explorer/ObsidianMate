"""Chat Agent Module."""

import os
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.tools import google_search
from google.genai import types

from models.enums import AgentNameEnum
from stores.llm.templates import TemplateParser
from utils.config_utils import get_settings
from utils.logging_utils import setup_logger

app_settings = get_settings()
template_parser = TemplateParser()
logger = setup_logger(
    log_file=__file__,
    log_dir=app_settings.PATH_LOGS,
)

retry_config = types.HttpRetryOptions(
    attempts=app_settings.RETRY_ATTEMPS,
    exp_base=app_settings.RETRY_EXP_BASE,
    initial_delay=app_settings.RETRY_INITAL_DELAY,
    http_status_codes=app_settings.RETRY_HTTP_STATUS_CODE,
)

chat_agent = Agent(
    name=AgentNameEnum.CHAT_AGENT,
    model=Gemini(model=app_settings.CHAT_MODEL_NAME, retry_options=retry_config),
    description="A simple agent that can answer general questions.",
    instruction=template_parser.get("chat", "INSTRUCTIONS"),  # type: ignore
    tools=[google_search],
    before_agent_callback=logger.info("%s is starting...", AgentNameEnum.CHAT_AGENT),
    after_agent_callback=logger.info("%s is Finishing...", AgentNameEnum.CHAT_AGENT),
    before_model_callback=logger.info("Model is about to generate a response..."),
    after_model_callback=logger.info("Model has generated a response."),
    before_tool_callback=logger.info("Callinge Google Search tool..."),
    after_tool_callback=logger.info("Google Search Tool call done."),
)


def main():
    """Entry Point for the Program."""
    print(
        f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module. Nothing to do ^_____^!"
    )


if __name__ == "__main__":
    main()
