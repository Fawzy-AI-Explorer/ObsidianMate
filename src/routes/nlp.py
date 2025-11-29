"""NLP Routes Module."""

import os
import logging
from fastapi import APIRouter, Request, status, Query
from fastapi.responses import JSONResponse
from controllers import SessionController, NLPController


logger = logging.getLogger("uvicorn")
nlp_router = APIRouter(prefix="/api/v1/nlp", tags=["api_v1", "nlp"])


@nlp_router.post("/chat/{session_id}/{user_id}")
async def answer_question(
    request: Request,
    session_id: str,
    user_id: str,
    query: str = Query(
        ..., default_factory=str, description="The user's question to be answered."
    ),
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

    if query.lower() == "summary":
        chat_history = await nlp_controller.get_conversation(session)
        chat_history = str(chat_history) if chat_history else ""
        if chat_history == "":
            return JSONResponse(
                content={
                    "signal": "no chat history found",
                },
                status_code=status.HTTP_404_NOT_FOUND,
            )
        query = f"Summarize and write The summarization in 'summary.md' in my obsidian vault \n==========\n {chat_history}"

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


@nlp_router.get("/chat_history/{session_id}/{user_id}")
async def get_chat_history(request: Request, session_id: str, user_id: str):
    """
    Endpoint to retrieve the chat history of a session.

    Args:
        request (Request): The FastAPI request object.
        session_id (str): Unique identifier of the session.
        user_id (str): Unique identifier of the user.

    Returns:
        JSONResponse:
            - 200 OK with the chat history if successful.
            - 400 BAD REQUEST if the session is not found.
    """

    app_state = request.app.state
    session_controller = SessionController(session_service=app_state.session_service)
    nlp_controller = NLPController(app_state.runner)

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
    chat_history = await nlp_controller.get_conversation(session)

    return JSONResponse(
        content={
            "signal": "chat_history_success",
            "chat_history": chat_history,
        },
        status_code=status.HTTP_200_OK,
    )
