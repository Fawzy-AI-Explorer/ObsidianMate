"""tool to extract conversation"""
from google.adk.sessions import Session


def extract_conversation(session: Session):
    """
    Extract conversation from a session object.

    Args:
        session (Session): The session object containing events.
    Returns:
        Dictionary with status and session events.
        Success example:
            {"status": "success", "session_events": [...]}
        Error example:
            {"status": "error", "error_message": "..."} 
    """

    session_events = session.events # List of Event objects
    conversation = []
    author = "unknown"
    text = "no text"
    for event in session_events:
        if event.auther:
                author = event.author

        if event.content and event.content.parts:
            if (
                event.content.parts[0].text != "None"
                and event.content.parts[0].text
            ):
                text = event.content.parts[0].text

        conversation.append({"author": author, "text": text})

    if not session_events:
        return {"status": "error", "eror_message": "No events found in the session."}
    return {"status": "success", "session_events": session_events}
