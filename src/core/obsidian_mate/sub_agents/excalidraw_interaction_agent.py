import os
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.models.lite_llm import LiteLlm
from google.genai import types

from models.enums import AgentNameEnum
from stores.llm.templates import TemplateParser
from utils.config_utils import get_settings
from core.tools.excalidraw_interaction_tool import excalidraw_tool


app_settings = get_settings()
template_parser = TemplateParser()

retry_config = types.HttpRetryOptions(
    attempts=app_settings.RETRY_ATTEMPS,
    exp_base=app_settings.RETRY_EXP_BASE,
    initial_delay=app_settings.RETRY_INITAL_DELAY,
    http_status_codes=app_settings.RETRY_HTTP_STATUS_CODE,
)

excalidraw_interaction_agent = Agent(
    name=AgentNameEnum.EXCALIDRAW_INTERACTION_AGENT,
    # model=Gemini(model=app_settings.CHAT_MODEL_NAME, retry_options=retry_config),
    model=LiteLlm(app_settings.DEFAULT_MODEL_NAME),
    description="A simple agent that can manage obsigian interactions.",
    instruction=template_parser.get("interact_excalidraw", "INSTRUCTIONS"),  # type: ignore
    tools=[
        excalidraw_tool
    ],
)


def main():
    """Entry Point for the Program."""
    print(
        f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module. Nothing to do ^_____^!"
    )


if __name__ == "__main__":
    main()
