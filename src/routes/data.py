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


def main():
    """Entry Point for the Program."""
    print(
        f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module. Nothing to do ^_____^!"
    )


if __name__ == "__main__":
    main()
