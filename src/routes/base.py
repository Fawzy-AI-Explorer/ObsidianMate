"""Base Route Module."""

import os
from fastapi import FastAPI, APIRouter, Request
from utils.config_utils import get_settings

base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"],
)


@base_router.get("/")
async def welocome(request: Request):
    """
    welcome route and entry point for testing connection.

    Args:
        request (Request): The incoming HTTP request.

    Returns:
        dict: A dictionary containing:
            app_name (str): The application name from settings.
            app_version (str): The application version from settings.
    """

    settings = request.app.state.settings
    app_name = settings.APP_NAME
    app_version = settings.APP_VERSION

    return {
        "app_name": app_name,
        "app_version": app_version,
    }


def main():
    """Entry Point for the Program."""
    print(
        f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module. Nothing to do ^_____^!"
    )


if __name__ == "__main__":
    main()
