"""Extract Conversation Agent Module"""

import os
from google.genai import types
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
# from core.tools import extract_conversation
from core.tools.conversation_extraction_tool import extract_conversation
from models.enums import AgentNameEnum
from utils.config_utils import get_settings
from stores.llm.templates import TemplateParser

app_settings = get_settings()
template_parser = TemplateParser()


retry_config = types.HttpRetryOptions(
    attempts=app_settings.RETRY_ATTEMPS,
    exp_base=app_settings.RETRY_EXP_BASE,
    initial_delay=app_settings.RETRY_INITAL_DELAY,
    http_status_codes=app_settings.RETRY_HTTP_STATUS_CODE,
)

ExtractConversationAgent = Agent(
    name=AgentNameEnum.EXTRACT_CONVERSATION_AGENT,
    model=Gemini(model=app_settings.EXTRACT_MODEL_NAME, retry_options=retry_config),
    description="An agent that extracts relevant conversation details from Data Base.",
    instruction=template_parser.get("extract_conversation", "INSTRUCTIONS"),  # type: ignore
    output_key="conversation",
    tools=[extract_conversation],
)


def main():
    """Entry Point for the Program."""
    print(
        f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module. Nothing to do ^_____^!"
    )


if __name__ == "__main__":
    main()
