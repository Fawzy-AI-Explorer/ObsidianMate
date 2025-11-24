""" "Clean Agent Module."""

import os
from google.adk.agents import SequentialAgent
from google.genai import types
from google.adk.models.google_llm import Gemini
from google.adk.tools.agent_tool import AgentTool
from google.adk.agents import Agent
from utils.config_utils import get_settings
from models.enums import AgentNameEnum
from stores.llm.templates import TemplateParser
from core.agents.chat_agent import chat_agent
from core.tools.smart_notes_tool import smart_notes_pipeline_tool

app_settings = get_settings()
template_parser = TemplateParser()

retry_config = types.HttpRetryOptions(
    attempts=app_settings.RETRY_ATTEMPS,
    exp_base=app_settings.RETRY_EXP_BASE,
    initial_delay=app_settings.RETRY_INITAL_DELAY,
    http_status_codes=app_settings.RETRY_HTTP_STATUS_CODE,
)

root_agent = Agent(
    name=AgentNameEnum.ROOT_AGENT,
    model=Gemini(model=app_settings.CHATT_MODEL_NAME, retry_options=retry_config),
    description="Orchestrates conversation flow by routing input to either the Chat Agent or the Note Pipeline.",
    instruction=template_parser.get("manage_conversation", "INSTRUCTIONS"),  # type: ignore
    tools=[AgentTool(chat_agent), smart_notes_pipeline_tool],
)


def main():
    """Entry Point for the Program."""
    print(
        f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module. Nothing to do ^_____^!"
    )


if __name__ == "__main__":
    main()
