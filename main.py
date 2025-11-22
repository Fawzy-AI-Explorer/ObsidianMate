"""
Main script for the application.
"""

import os
import logging
from contextlib import asynccontextmanager
from google.adk.sessions.database_session_service import DatabaseSessionService
from fastapi import FastAPI
from routes import base, data
from utils import get_settings

logger = logging.getLogger("uvicorn")


@asynccontextmanager
async def lifespan(app: FastAPI):  # pylint: disable=[W0621]
    """Manage application startup and shutdown events."""

    logger.info("Application is starting up...")

    # Startup
    settings = get_settings()
    app.state.settings = settings
    app.state.db_url = f"sqlite+aiosqlite:///{app.state.settings.SQLITE_DB_PATH}"
    app.state.session_service = DatabaseSessionService(db_url=app.state.db_url)
    logger.info("Database Connection Stablished")

    yield  # The application runs here

    # Shutdown
    logger.info("Application is shutting down...")


app = FastAPI(lifespan=lifespan)
app.include_router(base.base_router)
app.include_router(data.data_router)


def main():
    """Entry Point for the Program."""
    print(
        f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module. Nothing to do ^_____^!"
    )


if __name__ == "__main__":
    main()
