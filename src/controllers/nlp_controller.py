"""
NLP Controller Module.
"""

import os
from google.adk.runners import Runner
from google.adk.sessions import Session
from google.genai import types
from controllers.base_controller import BaseController
from utils.logging_utils import setup_logger


class NLPController(BaseController):
    """
    Controller responsible for handling NLP interactions with the AI model.

    Attributes:
        runner (Runner): The Runner instance used to stream model events and process queries.
        logger (logging.Logger): The logger used for recording warnings, info, and debug messages.
        app_settings (AppSettings): Inherited from BaseController;.
    """

    def __init__(self, runner: Runner):
        """
        Initialize the NLPController.

        Args:
            runner (Runner): The Runner instance used to perform asynchronous
                message streaming and interaction with the model.
        """

        super().__init__()
        self.runner = runner
        self.logger = setup_logger(
            log_file=__file__,
            log_dir=self.app_settings.PATH_LOGS,
            log_to_console=True,
            file_mode="a",
        )

    async def answer_query(
        self,
        session: Session,
        query: str,
    ) -> str:
        """
        Stream a user query to the model and return the final answer.

        Args:
            session (Session): The session object containing user and session IDs.
            query (str): The user's query text.

        Returns:
            str: The final model-generated answer. Returns an empty string if
            the query is empty or no valid answer is produced.
        """

        if len(query) == 0:
            self.logger.warning("Can't get answer for an empty query!")
            return ""

        self.logger.info("Answering the query...")
        query_content = types.Content(role="user", parts=[types.Part(text=query)])

        answer = ""
        async for event in self.runner.run_async(
            user_id=session.user_id,
            session_id=session.id,
            new_message=query_content,
        ):
            if event.content and event.content.parts:
                if (
                    event.content.parts[0].text != "None"
                    and event.content.parts[0].text
                ):
                    answer = event.content.parts[0].text

        self.logger.info("Done answering the query")
        return answer


def main():
    """
    Entry point for standalone module execution."""

    print(
        f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module. Nothing to do ^_____^!"
    )


if __name__ == "__main__":
    main()
