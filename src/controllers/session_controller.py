import os
from controllers import BaseController




class SessionController(BaseController):
    """Controller for managing sessions."""

    def __init__(self):
        """Initialize the SessionController."""
        super().__init__()

    async def create_session(self, app_name: str, user_id: str, session_id: str): 
        # create_session
        pass

    async def delete_session(self,  app_name: str, user_id: str, session_id: str):
        pass

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
