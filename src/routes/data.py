"""Base Route Module."""

import os
from fastapi import FastAPI, APIRouter, Request, status
from fastapi.responses import JSONResponse

from utils.config_utils import get_settings

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1"],
)


@data_router.get("/")
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

# remove session API
@data_router.delete("/session/{session_id}")
async def delete_session(session_id: str):
    """
    Delete a session by its ID.

    Args:
        session_id (str): The ID of the session to delete.
        request (Request): The incoming HTTP request.

    Returns:
        dict: A dictionary indicating the deletion status.
    """

    ## Check if session exists
    
    
    ## get Session By ID

    ## Delete Session

    return JSONResponse(
        content={
            "signal": f"Session {session_id} deleted successfully.",
            "session_id": session_id,
            },
        status_code=status.HTTP_200_OK,
    )