import os
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.genai import types

from core.obsidian_mate.sub_agents.summary_agent import conversation_summary_agent
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

smart_notes_pipeline = Agent(
    name=AgentNameEnum.SMART_NOTE_PIPELINE_AGENT,
    model=Gemini(model=app_settings.FILTER_MODEL_NAME, retry_options=retry_config),
    description="An agent that filters irrelevant content from a conversation, and summarize the conversation in markdown format.",
    instruction=template_parser.get("take_notes", "INSTRUCTIONS"),  # type: ignore
    output_key="final_notes",
    sub_agents=[conversation_summary_agent],
)


def main():
    """Entry Point for the Program."""
    print(f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module. (❁´◡`❁)")


if __name__ == "__main__":
    main()
