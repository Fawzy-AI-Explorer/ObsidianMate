"""Initialize the controller with settings and computed paths."""

import os
import random
import string
from utils.config_utils import get_settings, Settings


class BaseController:
    """Provide shared application settings and filesystem paths.

    Attributes:
        app_settings: The application settings object returned by
            ``utils.config_utils.get_settings()``.
        base_dir (str): Project root directory calculated relative to this
            file location.
        files_dir (str): Path to the `assets/files` directory inside the
            project.
        db_dir (str): Path to the `assets/database` directory inside
            the project.
    """

    def __init__(self):
        """Initialize the BaseController with application settings and paths."""

        self.app_settings = get_settings()
        self.base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        self.files_dir = os.path.join(self.base_dir, "assets", "files")
        self.db_dir = os.path.join(self.base_dir, "assets", "database")

    def generate_random_string(self, length: int = 12) -> str:
        """Generate a random alphanumeric string of given length.

        Args:
            length (int): Length of the random string to generate.

        Returns:
            str: A random alphanumeric string.

        Raises:
             ValueError: If ``k`` is negative.
        """

        if length <= 0:
            raise ValueError("Length must be a positive integer.")

        return "".join(random.choices(string.ascii_lowercase + string.digits, k=length))

    def get_database_path(self, db_name):
        """
        Get the file system path for a given database and ensure its directory exists.

        Args:
            db_name (str): The name of the database.

        Returns:
            str: The absolute path to the database directory.
        """

        database_path = os.path.join(self.db_dir, db_name)
        os.makedirs(database_path, exist_ok=True)

        return database_path


if __name__ == "__main__":
    print(
        f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module. Nothing to do ^_____^!"
    )
