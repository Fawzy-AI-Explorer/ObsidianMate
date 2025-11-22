"""NLP Routes Module."""

import os
import logging
from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse
from controllers import SessionController, NLPController


logger = logging.getLogger("uvicorn")
nlp_router = APIRouter(prefix="/api/v1/nlp", tags=["api_v1", "nlp"])


@nlp_router.get("/health")
async def health_check():
    """
    Health check endpoint to verify the NLP service is operational.

    Returns:
        JSONResponse: A response indicating the health status of the NLP service.
    """
    return JSONResponse(
        content={
            "signal": "nlp_service_healthy",
        },
        status_code=status.HTTP_200_OK,
    )


@nlp_router.post("/chat/{session_id}")
async def answer_question(request: Request,
                          session_id: str,
                          user_id: str,
                          query: str
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
    if answer is None:
        return JSONResponse(
            content={
                "signal": "answer_failed",
            },
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return JSONResponse(
        content={
            "signal": "answer_success",
            "answer": answer,
        },
        status_code=status.HTTP_200_OK,
    )
