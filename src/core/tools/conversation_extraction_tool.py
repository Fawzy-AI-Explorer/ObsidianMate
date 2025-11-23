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
    # conversation = []
    # for event in session_events:
    #     conversation.append(
    #         {
    #             "author": event.author, # str
    #             "event":
    #         }
    #     )
    if not session_events:
        return {"status": "error", "eror_message": "No events found in the session."}
    return {"status": "success", "session_events": session_events}
