"""excalidraw Interaction Tool Module."""

import os
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters
from utils.config_utils import get_settings


app_settings = get_settings()


excalidraw_tool = McpToolset(
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
)


def main():
    """Entry Point for the Program."""
    print(f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module. (❁´◡`❁)")


if __name__ == "__main__":
    main()
