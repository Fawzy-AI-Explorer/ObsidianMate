import os
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.models.lite_llm import LiteLlm
from google.genai import types
from utils.config_utils import get_settings
from models.enums import AgentNameEnum
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

text_summary_agent = Agent(
    name=AgentNameEnum.TEXT_SUMMARY_AGENT,
    # model=Gemini(model=app_settings.SUMMARIZE_MODEL_NAME, retry_options=retry_config),
    model=LiteLlm(app_settings.DEFAULT_MODEL_NAME),
    description="An agent that summarize text.",
    instruction=template_parser.get("summarize", "INSTRUCTIONS"),  # type: ignore
    output_key="text_summary",

    before_agent_callback=logger.info("%s is starting...", AgentNameEnum.TEXT_SUMMARY_AGENT),
    after_agent_callback=logger.info("%s is Finishing...", AgentNameEnum.TEXT_SUMMARY_AGENT),
    before_model_callback=logger.info("Model is about to generate a response..."),
    after_model_callback=logger.info("Model has generated a response."),
)


def main():
    """Entry Point for the Program."""
    print(
        f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module. Nothing to do ^_____^!"
    )


if __name__ == "__main__":
    main()
