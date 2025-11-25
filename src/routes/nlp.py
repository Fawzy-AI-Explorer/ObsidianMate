"""NLP Routes Module."""

import os
import logging
from fastapi import APIRouter, Request, status, Query
from fastapi.responses import JSONResponse
from controllers import SessionController, NLPController


logger = logging.getLogger("uvicorn")
nlp_router = APIRouter(prefix="/api/v1/nlp", tags=["api_v1", "nlp"])


@nlp_router.post("/chat/{session_id}/{user_id}")
async def answer_question(request: Request,
                          session_id: str,
                          user_id: str,
                          query: str=Query(..., default_factory=str, description="The user's question to be answered.")
        ):
    """
    Endpoint to answer a user's question within a session.
    
    Args:
        request (Request): The FastAPI request object.
        session_id (str): Unique identifier of the session.
        user_id (str): Unique identifier of the user.
        query (str): The user's question to be answered.
    
    Returns:
        JSONResponse: 
            - 200 OK with the answer if successful.
            - 400 BAD REQUEST if the session is not found.
            - 400 BAD REQUEST if the answer generation fails.
    """

    app_state = request.app.state
    session_controller = SessionController(session_service=app_state.session_service)

    session = await session_controller.get_session(
        app_name=app_state.settings.APP_NAME, user_id=user_id, session_id=session_id
    )

    if session is None:
        return JSONResponse(
            content={
                "signal": "session_not_found",
            },
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    nlp_controller = NLPController(app_state.runner)
    answer = await nlp_controller.answer_query(session=session, query=query)
    if answer == "":
        return JSONResponse(
            content={
                "signal": "answer_failed",
            },
            status_code=status.HTTP_404_NOT_FOUND,
        )
    await request.app.state.memory_service.add_session_to_memory(session)
    return JSONResponse(
        content={
            "signal": "answer_success",
            "answer": answer,
        },
        status_code=status.HTTP_200_OK,
    )
