import os
import logging
from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse
from controllers import SessionController

logger = logging.getLogger("uvicorn")
data_router = APIRouter(prefix="/api/v1/data", tags=["api_v1", "data"])


@data_router.post("/create_session/{session_id}/{user_id}")
async def create_session(request: Request, session_id: str, user_id: str):
    """Create a new session or return an existing one.

    Args:
        request (Request): The incoming FastAPI request object containing
            application state and configuration.
        session_id (str): Unique identifier of the session to create.
        user_id (str): Unique identifier of the user who owns the session.

    Returns:
        JSONResponse: A response containing:
            - ``signal``: Status of the operation
              (e.g., "session_creation_success" or "session_creation_failed").
            - ``session_id`` (optional): The created or existing session ID.
            - ``user_id`` (optional): The user ID associated with the session.
    """

    app_state = request.app.state
    session_controller = SessionController(session_service=app_state.session_service)
    session = await session_controller.create_session(
        app_name=app_state.settings.APP_NAME, user_id=user_id, session_id=session_id
    )
    if session is None:
        return JSONResponse(
            content={
                "signal": "session_creation_failed",
            },
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    return JSONResponse(
        content={
            "signal": "session_creation_success",
            "session_id": session.id,
            "user_id": session.user_id,
        },
        status_code=status.HTTP_200_OK,
    )


# remove session API
@data_router.delete("/delete_session/{session_id}")
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


def main():
    """Entry Point for the Program."""
    print(
        f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module. Nothing to do ^_____^!"
    )


if __name__ == "__main__":
    main()
