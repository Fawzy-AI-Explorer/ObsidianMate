import os
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.genai import types

from core.tools.google_search_tool import google_search
from models.enums import AgentNameEnum
from stores.llm.templates import TemplateParser
from utils.config_utils import get_settings
from utils.agent_utils import suppress_output_callback

app_settings = get_settings()
template_parser = TemplateParser()

retry_config = types.HttpRetryOptions(
    attempts=app_settings.RETRY_ATTEMPS,
    exp_base=app_settings.RETRY_EXP_BASE,
    initial_delay=app_settings.RETRY_INITAL_DELAY,
    http_status_codes=app_settings.RETRY_HTTP_STATUS_CODE,
)

# research_agent = Agent(
#     name="ResearchAgent",
#     model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
#     instruction="""You are a specialized research agent. Your only job is to use the
#     google_search tool to find relevant information on the given query or topic and present the findings with citations.""",
#     tools=[google_search],
#     output_key="research_findings",
#     after_agent_callback=suppress_output_callback,
# )

chat_agent = Agent(
    name=AgentNameEnum.CHAT_AGENT,
    model=Gemini(model=app_settings.CHATT_MODEL_NAME, retry_options=retry_config),
    description="A simple agent that can answer general questions.",
    instruction=template_parser.get("chat", "INSTRUCTIONS"),  # type: ignore
    tools=[google_search],
)


def main():
    """Entry Point for the Program."""
    print(
        f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module. Nothing to do ^_____^!"
    )


if __name__ == "__main__":
    main()
