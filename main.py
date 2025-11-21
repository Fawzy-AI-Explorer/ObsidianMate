"""
Main script for the application.
"""

import os
from contextlib import asynccontextmanager
import logging
from fastapi import FastAPI
from routes import base, data
from utils import get_settings

logger = logging.getLogger("uvicorn")


@asynccontextmanager
async def lifespan(app: FastAPI):  # pylint: disable=[W0621]

    logger.info("Application is starting up...")

    # Startup
    settings = get_settings()
    app.state.settings = settings

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
