""" "Clean Agent Module."""

import os
from google.genai import types
from google.adk.models.google_llm import Gemini
from google.adk.models.lite_llm import LiteLlm
from google.adk.agents import Agent
from google.adk.tools import agent_tool
from utils.config_utils import get_settings
from models.enums import AgentNameEnum
from stores.llm.templates import TemplateParser
from core.obsidian_mate.sub_agents.chat_agent import chat_agent
from core.obsidian_mate.sub_agents.obsidian_interaction_agent import obsidian_interaction_agent
from core.obsidian_mate.sub_agents.excalidraw_interaction_agent import excalidraw_interaction_agent
from core.obsidian_mate.sub_agents.smart_notes_agent import smart_notes_pipeline
from core.obsidian_mate.sub_agents.summary_agent import text_summary_agent
from core.obsidian_mate.sub_agents.transcript_agent import yt_transcript_agent
from core.tools.youtube_transcript_tool import transcript_tool


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


obsidian_mate_agent = Agent(
    name=AgentNameEnum.OBSIDIAN_MATE_AGENT,
    # model=Gemini(model=app_settings.CHATT_MODEL_NAME, retry_options=retry_config),
    model=LiteLlm(app_settings.DEFAULT_MODEL_NAME),
    description="Helpfull obsidian support agent",
    instruction=template_parser.get("root", "INSTRUCTIONS"),  # type: ignore
    tools=[
        agent_tool.AgentTool(chat_agent),
        agent_tool.AgentTool(smart_notes_pipeline),
        agent_tool.AgentTool(obsidian_interaction_agent),
        agent_tool.AgentTool(yt_transcript_agent),
        # agent_tool.AgentTool(excalidraw_interaction_agent),
    ],

    before_agent_callback=logger.info("%s is starting...", AgentNameEnum.OBSIDIAN_MATE_AGENT),
    after_agent_callback=logger.info("%s is Finishing...", AgentNameEnum.OBSIDIAN_MATE_AGENT),
    before_model_callback=logger.info("Model is about to generate a response..."),
    after_model_callback=logger.info("Model has generated a response."),
    before_tool_callback=logger.info("Obsidiab Tool is about to be invoked..."),
    after_tool_callback=logger.info("Obsidian Tool has been invoked."),
)

root_agent = obsidian_mate_agent


def main():
    """Entry Point for the Program."""
    print(
        f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module. Nothing to do ^_____^!"
    )


if __name__ == "__main__":
    main()
