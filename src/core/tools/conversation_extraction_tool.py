"""tool to extract conversation"""

from typing import Any, Callable
from google.adk.agents import InvocationContext
from google.adk.sessions.database_session_service import DatabaseSessionService
from google.adk.tools.function_tool import FunctionTool
from google.adk.tools.tool_context import ToolContext
from utils.config_utils import get_settings


class ExtractConversationTool(FunctionTool):
    """
    Tool to extract conversation history from a session object.

    This tool wraps an asynchronous function that retrieves all events
    from the given session in a structured format. It is intended to
    be called by an agent in the ADK framework.
    """

    async def run_async(
        self, *, args: dict[str, Any], tool_context: ToolContext
    ) -> Any:
        """
        Execute the tool asynchronously.

        Args:
            args (dict[str, Any]): Dictionary of arguments passed to the tool.
            tool_context (ToolContext): Context object containing session info
                                        and other metadata.

        Returns:
            dict: Result dictionary containing either:
                - success: {"status": "success", "session_events": [...]}
                - error: {"status": "error", "error_message": "..."}
        """

        return await self.func(tool_context)


async def _extract_conversation(tool_context: ToolContext):
    """
    Extracts conversation events from the session.

    Iterates over the session's events and collects the author and text
    of each event into a structured list. Provides a status field to
    indicate success or failure.

    Args:
        tool_context (ToolContext): Context providing access to the session object.

    Returns:
        dict: Dictionary with the extraction result:
            - On success:
                {
                    "status": "success",
                    "session_events": [
                        {"author": "author_name", "text": "event_text"}, ...
                    ]
                }
            - On error:
                {
                    "status": "error",
                    "error_message": "Description of the error"
                }
    """

    settings = get_settings()
    db_url = f"sqlite+aiosqlite:///{settings.SQLITE_DB_PATH}"
    session_service = DatabaseSessionService(db_url=db_url)
    session = await session_service.get_session(
        app_name=settings.APP_NAME,
        user_id=tool_context.user_id,
        session_id=tool_context.session.id,
    )
    session_events = None
    if session is not None:
        session_events = session.events
    author = "unknown"
    text = "no text"
    conversation = []
    if session_events is not None:
        for idx, event in enumerate(session_events):
            if event.author:
                author = event.author

            if event.content and event.content.parts:
                if (
                    event.content.parts[0].text != "None"
                    and event.content.parts[0].text
                ):
                    text = event.content.parts[0].text

            conversation.append({f"turn-{idx}": {"author": author, "text": text}})

    if not session_events:
        return {"status": "error", "eror_message": "No events found in the session."}
    return {"status": "success", "conversation": conversation}


_extract_conversation.__name__ = "extract_conversation"

extract_conversation = ExtractConversationTool(
    func=_extract_conversation,
)
