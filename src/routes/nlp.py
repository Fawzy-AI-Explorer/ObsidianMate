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

    chat_history = [
        {"author": event.author, "text": event.content.parts[0].text}
        for event in session.events
        if (
            event.content
            and event.content.parts
            and event.content.parts[0].text not in ["", None, "null"]
        )
    ]

    return JSONResponse(
        content={
            "signal": "chat_history_success",
            "chat_history": chat_history,
        },
        status_code=status.HTTP_200_OK,
    )


@nlp_router.get("/get_summary/{session_id}/{user_id}")
async def get_session_summary(request: Request, session_id: str, user_id: str):
    """
    Endpoint to retrieve the summary of a session.

    Args:
        request (Request): The FastAPI request object.
        session_id (str): Unique identifier of the session.
        user_id (str): Unique identifier of the user.

    Returns:
        JSONResponse:
            - 200 OK with the session summary if successful.
            - 400 BAD REQUEST if the session is not found.
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

    chat_history = [
        {"author": event.author, "text": event.content.parts[0].text}
        for event in session.events
        if (
            event.content
            and event.content.parts
            and event.content.parts[0].text not in ["", None, "null"]
        )
    ]

    chat_history = """
{
    "signal": "chat_history_success",
    "chat_history": [
        {
            "author": "user",
            "text": "What is google adk"
        },
        {
            "author": "ObsidianMateAgent",
            "text": "The term \"Google ADK\" can refer to two different things:\n\n1.  **Android Development Kit (ADK):** This is a collection of tools and libraries that Google provides to help developers create applications for the Android operating system. It's a fundamental part of Android app development and is integrated into Android Studio, the official IDE for Android development.\n\n2.  **Agent Development Kit (ADK):** This is a newer, open-source framework from Google that focuses on building and deploying AI agents and multi-agent systems. It's designed to be flexible and modular, allowing for the creation, orchestration, and management of AI agents that can handle complex tasks. This ADK is optimized for Google's Gemini models and Vertex AI but can work with other models and frameworks as well."
        },
        {
            "author": "user",
            "text": "is it supprt multi agents"
        },
        {
            "author": "ObsidianMateAgent",
            "text": "Yes, the **Agent Development Kit (ADK)** specifically supports **multi-agent systems**. It's designed to help developers build, orchestrate, and manage multiple AI agents that can work together to perform complex tasks and workflows."
        },
        {
            "author": "user",
            "text": "what is memori in adk"
        },
        {
            "author": "ObsidianMateAgent",
            "text": "In the context of the Agent Development Kit (ADK), **memory** refers to a crucial feature that allows AI agents to retain and retrieve information over time, extending beyond a single conversation session. It acts as the agent's long-term knowledge base.\n\nHere's a breakdown:\n\n*   **Long-Term Knowledge:** Memory enables agents to store information from past interactions, which they can then access later. This allows for more personalized and context-aware responses.\n*   **MemoryService:** This is the central component for managing this long-term knowledge. It handles:\n    *   **Ingesting Information:** Storing relevant details from completed sessions into the knowledge store.\n    *   **Searching Information:** Allowing the agent to query this store and retrieve relevant information based on a search.\n*   **Distinction from Session:** While a \"Session\" manages short-term context within a single conversation, \"Memory\" provides a searchable archive from multiple past conversations or other data sources.\n*   **Implementations:** ADK offers different types of MemoryServices:\n    *   **InMemoryMemoryService:** For development and prototyping, stores data in memory (lost on restart) and uses keyword matching.\n    *   **VertexAiMemoryBankService:** For production, uses Vertex AI for persistent storage and advanced semantic search, allowing agents to learn and remember from user interactions.\n*   **Memory Tools:** Agents can use tools like `PreloadMemory` (to always load memory at the start of a turn) or `LoadMemory` (to load memory when the agent decides it's useful) to interact with the memory service.\n\nEssentially, ADK's memory functionality empowers agents to build a persistent understanding, leading to more intelligent and engaging interactions."
        },
        {
            "author": "user",
            "text": "thank you"
        },
        {
            "author": "ObsidianMateAgent",
            "text": "You're welcome! Feel free to ask if you have more questions about Google ADK or anything else."
        }
    ]
}
"""

    # query = "Summary" + "\n\n" + str(chat_history)
    query = f"Filter and Summarize\n==========\n{str(chat_history)}"

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
