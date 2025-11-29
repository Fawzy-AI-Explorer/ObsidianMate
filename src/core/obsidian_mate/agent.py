""" "Clean Agent Module."""

import os
from google.genai import types
from google.adk.models.google_llm import Gemini
from google.adk.models.lite_llm import LiteLlm
from google.adk.agents import Agent
from google.adk.tools import agent_tool
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters
from utils.config_utils import get_settings
from models.enums import AgentNameEnum
from stores.llm.templates import TemplateParser
from core.obsidian_mate.sub_agents.chat_agent import chat_agent
from core.obsidian_mate.sub_agents.smart_notes_agent import smart_notes_pipeline

app_settings = get_settings()
template_parser = TemplateParser()

retry_config = types.HttpRetryOptions(
    attempts=app_settings.RETRY_ATTEMPS,
    exp_base=app_settings.RETRY_EXP_BASE,
    initial_delay=app_settings.RETRY_INITAL_DELAY,
    http_status_codes=app_settings.RETRY_HTTP_STATUS_CODE,
)


# obsidian_mate_agent = Agent(
#     name=AgentNameEnum.OBSIDIAN_MATE_AGENT,
#     model=Gemini(model=app_settings.CHATT_MODEL_NAME, retry_options=retry_config),
#     description="An agent that help user by answering questions, summarizing conversation, "
#     "and taking control of obsidian to take notes",
#     instruction=template_parser.get("manage_conversation", "INSTRUCTIONS"),  # type: ignore
#     tools=[
#         agent_tool.AgentTool(chat_agent),
#         agent_tool.AgentTool(smart_notes_pipeline),
#     ],
# )

obsidian_mate_agent = Agent(
    name=AgentNameEnum.OBSIDIAN_MATE_AGENT,
    # model=Gemini(model=app_settings.CHATT_MODEL_NAME, retry_options=retry_config),
    model=LiteLlm(app_settings.DEFAULT_MODEL_NAME),
    description="Helpfull obsidian support agent",
    instruction="Help user by interacting with obsidian",
    tools=[
        McpToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command="docker",
                    args=[
                        "run",
                        "-i",
                        "--rm",
                        "-e",
                        "OBSIDIAN_HOST",
                        "-e",
                        "OBSIDIAN_API_KEY",
                        "mcp/obsidian",
                    ],
                    env={
                        "OBSIDIAN_HOST": "host.docker.internal",
                        "OBSIDIAN_API_KEY": str(
                            app_settings.OBSIDIAN_API_KEY.get_secret_value()  # pylint: disable=[E1101]
                        ),
                    },
                )
            )
        ),
        McpToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command="docker",
                    args=[
                        "run",
                        "-i",
                        "--rm",
                        "--network",
                        "host",
                        "-e",
                        "EXPRESS_SERVER_URL",
                        "-e",
                        "ENABLE_CANVAS_SYNC",
                        "ghcr.io/yctimlin/mcp_excalidraw-canvas:latest",
                    ],
                    env={
                        "EXPRESS_SERVER_URL": "http://localhost:3000",
                        "ENABLE_CANVAS_SYNC": "true",
                    },
                )
            )
        ),
    ],
)

root_agent = obsidian_mate_agent
# root_agent = smart_notes_pipeline


def main():
    """Entry Point for the Program."""
    print(
        f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module. Nothing to do ^_____^!"
    )


if __name__ == "__main__":
    main()
