import os
from typing import Optional
from google.adk.sessions import Session, BaseSessionService
from google.adk.errors.already_exists_error import AlreadyExistsError
from controllers import BaseController
from utils.logging_utils import setup_logger


class SessionController(BaseController):
    """Controller for managing sessions."""

    def __init__(self, session_service: BaseSessionService):
        """Initialize the SessionController."""

        super().__init__()
        self.session_service = session_service
        self.logger = setup_logger(
            log_file=__file__,
            log_dir=self.app_settings.PATH_LOGS,
            log_to_console=True,
            file_mode="a",
        )

    async def create_session(
        self, app_name: Optional[str], user_id: str, session_id: str
    ) -> Session | None:
        """Create a new session or return an existing one.

        Args:
            app_name (Optional[str]): Name of the application. If ``None``,
                the default application name from settings is used.
            user_id (str): Unique identifier of the user.
            session_id (str): Unique identifier of the session.

        Returns:
            Session | None: The created or retrieved session instance. Returns
                ``None`` if session creation or retrieval fails.
        """

        app_name = self.app_settings.APP_NAME if app_name is None else app_name
        try:
            session = await self.session_service.create_session(
                app_name=app_name, user_id=user_id, session_id=session_id
            )
        except AlreadyExistsError:
            self.logger.info(
                "Session with session_id=%s for user_id=%s already exists. Gettings session...",
                session_id,
                user_id,
            )
            session = await self.session_service.get_session(
                app_name=app_name, user_id=user_id, session_id=session_id
            )

        return session

    async def delete_session(
        self, app_name: Optional[str], user_id: str, session_id: str
    ) -> bool:
        """
        Delete an existing session.

        Args:
            app_name (Optional[str]): Name of the application. If ``None``,
                the default application name from settings is used.
            user_id (str): Unique identifier of the user who owns the session.
            session_id (str): Unique identifier of the session to be deleted.

        Returns:
            bool: True if the session was successfully deleted, False otherwise.
        """

        app_name = self.app_settings.APP_NAME if app_name is None else app_name

        session = await self.get_session(
            app_name=app_name, user_id=user_id, session_id=session_id
        )
        if session is None:
            self.logger.warning(
                "Session with session_id=%s for user_id=%s does not exist. Cannot delete.",
                session_id,
                user_id,
            )
            return False

        await self.session_service.delete_session(
            app_name=app_name, user_id=user_id, session_id=session_id
        )
        return True

    async def get_session(
        self, app_name: str, user_id: str, session_id: str
    ) -> Optional[Session]:
        pass
    async def list_sessions(self, app_name, user_id=None):
        pass

    async def delete_sessions(self, app_name, user_id=None):
        pass


def main():
    """Entry Point for the Program."""
    print(f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module. (❁´◡`❁)")


if __name__ == "__main__":
    main()
