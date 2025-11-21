import os
import logging
from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse

logger = logging.getLogger("uvicorn")
data_router = APIRouter(prefix="/api/v1/data", tags=["api_v1", "data"])


@data_router.post("/add_session/{session_id}/{user_id}")
async def add_session(request: Request, session_id: str, user_id: str):
    return JSONResponse(
        content={
            "signal": "done_adding_session",
            "session_id": session_id,
            "user_id": user_id,
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

