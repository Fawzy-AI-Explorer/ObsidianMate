import os
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.models.lite_llm import LiteLlm
from google.genai import types

from core.obsidian_mate.sub_agents.summary_agent import conversation_summary_agent
from models.enums import AgentNameEnum
from utils.config_utils import get_settings
from stores.llm.templates import TemplateParser
from utils.logging_utils import setup_logger

app_settings = get_settings()
template_parser = TemplateParser()
logger = setup_logger(
    log_file = __file__,
    log_dir = app_settings.PATH_LOGS,
)


retry_config = types.HttpRetryOptions(
    attempts=app_settings.RETRY_ATTEMPS,
    exp_base=app_settings.RETRY_EXP_BASE,
    initial_delay=app_settings.RETRY_INITAL_DELAY,
    http_status_codes=app_settings.RETRY_HTTP_STATUS_CODE,
)

smart_notes_pipeline = Agent(
    name=AgentNameEnum.SMART_NOTE_PIPELINE_AGENT,
    # model=Gemini(model=app_settings.FILTER_MODEL_NAME, retry_options=retry_config),
    model=LiteLlm(app_settings.DEFAULT_MODEL_NAME),
    description="An agent that filters irrelevant content from a conversation, and summarize the conversation in markdown format.",
    instruction=template_parser.get("take_notes", "INSTRUCTIONS"),  # type: ignore
    output_key="final_notes",
    sub_agents=[conversation_summary_agent],

    before_agent_callback=logger.info("%s is starting...", AgentNameEnum.SMART_NOTE_PIPELINE_AGENT),
    after_agent_callback=logger.info("%s is Finishing...", AgentNameEnum.SMART_NOTE_PIPELINE_AGENT),
    before_model_callback=logger.info("Model is about to generate a response..."),
    after_model_callback=logger.info("Model has generated a response."),
)


def main():
    """Entry Point for the Program."""
    print(f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module. (❁´◡`❁)")


if __name__ == "__main__":
    main()
