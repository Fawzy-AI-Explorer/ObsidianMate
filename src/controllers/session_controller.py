import os
from controllers import BaseController
from google.adk.sessions import BaseSessionService

class SessionController(BaseController):
    """Controller for managing sessions."""

    def __init__(self, session_service: BaseSessionService):
        """Initialize the SessionController."""
        super().__init__()
        self.session_service = session_service

    async def create_session(self, app_name: str, user_id: str, session_id: str): 
        # create_session
        pass

    async def delete_session(self,  app_name: str, user_id: str, session_id: str):
        """
        Delete a session by its ID.
        Args:
            app_name (str): The name of the application.
            user_id (str): The ID of the user.
            session_id (str): The ID of the session to delete.
        Returns:
            None
        """

        await self.session_service.delete_session(
        app_name=app_name, 
        user_id=user_id, 
        session_id=session_id
        )


    async def get_session(self,  app_name: str, user_id: str, session_id: str):
        pass

    async def list_sessions(self, app_name, user_id=None):
        pass

    async def delete_sessions(self, app_name, user_id=None):
        pass

def main():
    """Entry Point for the Program."""
    print(
        f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module. (❁´◡`❁)"
    )



if __name__ == "__main__":
    main()
