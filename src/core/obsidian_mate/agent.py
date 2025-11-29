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
from core.obsidian_mate.sub_agents.smart_notes_agent import smart_notes_pipeline
from core.tools.obsidian_interaction_tool import obsidian_tool
from core.tools.excalidraw_interaction_tool import excalidraw_tool

app_settings = get_settings()
template_parser = TemplateParser()

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
        obsidian_tool,
        # excalidraw_tool,
    ],
)

root_agent = obsidian_mate_agent


def main():
    """Entry Point for the Program."""
    print(
        f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module. Nothing to do ^_____^!"
    )


if __name__ == "__main__":
    main()
