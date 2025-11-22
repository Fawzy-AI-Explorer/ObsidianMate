import os
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.genai import types
from utils.config_utils import get_settings
from models.enums import AgentNameEnum
from stores.llm.templates import TemplateParser

app_settings = get_settings()
template_parser = TemplateParser()

retry_config = types.HttpRetryOptions(
    attempts=app_settings.RETRY_ATTEMPS,
    exp_base=app_settings.RETRY_EXP_BASE,
    initial_delay=app_settings.RETRY_INITAL_DELAY,
    http_status_codes=app_settings.RETRY_HTTP_STATUS_CODE,
)

MarkdownAgent = Agent(
    name=AgentNameEnum.MARKDOWN_FORMATTER_AGENT,
    model=Gemini(model=app_settings.MARKDOWN_MODEL_NAME, retry_options=retry_config),
    description="A simple agent that can answer general questions.",
    instruction=template_parser.get("markdown", "INSTRUCTIONS"),  # type: ignore
    output_key="markdown"
)

def main():
    """Entry Point for the Program."""
    print(
        f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module. Nothing to do ^_____^!"
    )


if __name__ == "__main__":
    main()
