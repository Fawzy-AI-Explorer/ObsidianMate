"""
Main script for the application.
"""

import os
import logging
from contextlib import asynccontextmanager
from google.adk.sessions.database_session_service import DatabaseSessionService
from google.adk.runners import Runner
from fastapi import FastAPI
# from core.agents import root_agent
from core.agents.root_agent import root_agent
from routes import base, data, nlp
from utils import get_settings

logger = logging.getLogger("uvicorn")

@asynccontextmanager
async def lifespan(app: FastAPI):  # pylint: disable=[W0621]
    """Manage application startup and shutdown events."""

    logger.info("Application is starting up...")

    # Startup
    settings = get_settings()
    app.state.settings = settings
    os.environ["GOOGLE_API_KEY"] = app.state.settings.GOOGLE_API_KEY
    app.state.db_url = f"sqlite+aiosqlite:///{app.state.settings.SQLITE_DB_PATH}"
    app.state.session_service = DatabaseSessionService(db_url=app.state.db_url)
    app.state.runner = Runner(
        agent=root_agent,
        app_name=settings.APP_NAME,
        session_service=app.state.session_service,
    )
    logger.info("Database Connection Stablished")

    yield  # The application runs here

    # Shutdown
    logger.info("Application is shutting down...")


app = FastAPI(lifespan=lifespan)
app.include_router(base.base_router)
app.include_router(data.data_router)
app.include_router(nlp.nlp_router)



def main():
    """Entry Point for the Program."""
    print(
        f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module. Nothing to do ^_____^!"
    )


if __name__ == "__main__":
    main()
