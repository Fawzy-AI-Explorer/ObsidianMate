"""Logging Utility Module."""

import os
import sys
import logging
from typing import Literal, Optional


def setup_logger(
    log_file: Optional[str] = None,
    log_dir: str = "logs",
    log_to_console: bool = True,
    file_mode: Literal["a", "w"] = "a",
) -> logging.Logger:
    """Set up a logger with an optional per-file handler and an always-on all_logs handler.

    If log_file is None or empty, only the logs/all_logs.log handler will be used.

    Args:
        log_file (Optional[str]): The name or path for the per-file log (optional).
        log_dir (str, optional): Directory where log files will be created. Defaults to "logs".
        log_to_console (bool, optional): Whether to also log messages to the console (stdout).
            Defaults to True.
        file_mode (str, optional): File open mode for the per-file log:
            "a" to append (default) or "w" to overwrite.

    Returns:
        logging.Logger: Configured logger instance.
    """
    if file_mode not in {"a", "w"}:
        raise ValueError("file_mode must be 'a' (append) or 'w' (write).")

    # Ensure log directory exists
    os.makedirs(log_dir, exist_ok=True)

    # Name logger so separate setups don't conflict; prefer the per-file name when present
    logger_name = (
        os.path.splitext(os.path.basename(log_file))[0] if log_file else "all_logs"
    )
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.handlers.clear()

    formatter = logging.Formatter(
        "[%(asctime)s][%(filename)s:%(lineno)d][%(levelname)s]: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Per-file handler (optional)
    if log_file:
        per_file_path = os.path.join(
            log_dir, f"{os.path.splitext(os.path.basename(log_file))[0]}.log"
        )
        file_handler = logging.FileHandler(per_file_path, mode=file_mode)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    # Always-on aggregate log
    all_logs_path = os.path.join(log_dir, "all_logs.log")
    file_handler_all_logs = logging.FileHandler(all_logs_path, mode="a")
    file_handler_all_logs.setLevel(logging.DEBUG)
    file_handler_all_logs.setFormatter(formatter)
    logger.addHandler(file_handler_all_logs)

    if log_to_console:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger


def main():
    """Entry point for the program."""

    print(f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module.")

    # Example: per-file log
    logger1 = setup_logger(
        log_file=__file__, log_dir="logs", log_to_console=False, file_mode="a"
    )
    logger1.debug("Per-file debug message (saved in per-file and all_logs).")

    # Example: only aggregate all_logs
    logger2 = setup_logger(log_to_console=True, file_mode="a")
    logger2.info(
        "Aggregate info message (saved only to all_logs and shown on console)."
    )


if __name__ == "__main__":
    main()
