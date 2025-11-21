"""Logging utility module for redirecting stdout to multiple streams."""

import sys
import os
import atexit
import time


class MultiStream:
    """A class to write messages to multiple output streams."""

    def __init__(self, *streams, flush_immediately: bool = False):
        """Initialize MultiStream with multiple output streams.

        Args:
            *streams: Variable length argument list of streams
                (e.g., sys.stdout, file objects).
        """
        self.streams = streams
        self.flush_immediately = flush_immediately

    def write(self, message):
        """Write a message to all streams.

        Args:
            message (str): The message to be written.
        """
        for stream in self.streams:
            stream.write(message)

        if self.flush_immediately:
            self.flush()

    def flush(self):
        """Flush all streams to ensure output is written immediately."""
        for stream in self.streams:
            if hasattr(stream, "closed") and getattr(stream, "closed", False):
                continue
            stream.flush()

    def isatty(self):
        """Check if any of the streams is a terminal.

        Returns:
            bool: True if at least one stream supports `isatty` and is a
            terminal, False otherwise.
        """
        return any(hasattr(s, "isatty") and s.isatty() for s in self.streams)


def log_stream(
    log_file: str,
    prog: str,
    flush_immediately: bool = False,
    verbose: bool = False,
    overwrite: bool = True,
):
    """Redirect stdout to both a log file and optionally the console.

    Args:
        log_file (str): Name of the log file (without extension).
        prog (str): Name of the program (used for directory structure).
        flush_immediately (bool, optional): If True, flush streams after each write.
            Defaults to False.
        verbose (bool, optional): If True, also log output to console.
            Defaults to False.
        overwrite (bool, optional): If True, overwrite log file.
            If False, append to existing file. Defaults to True.
    """
    os.makedirs(os.path.join("logs", prog), exist_ok=True)
    mode = "w" if overwrite else "a"

    log_path = os.path.join("logs", prog, f"{log_file}.log")
    _file = open(log_path, mode=mode, encoding="utf-8")

    # Build the target streams tuple
    if verbose:
        target_streams = (sys.stdout, _file)
    else:
        target_streams = (_file,)

    stream = MultiStream(*target_streams, flush_immediately=flush_immediately)

    sys.stdout = stream

    def _close_logfile():
        try:
            if not getattr(_file, "closed", False):
                _file.flush()
                _file.close()
        except OSError:
            pass

    atexit.register(_close_logfile)


def main():
    """Entry point for the program."""
    print(
        f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module. "
        "Nothing to do ^_____^!"
    )
    log_stream(
        log_file="stream_utils",
        prog="utils",
        flush_immediately=False,
        verbose=True,
        overwrite=True,
    )
    for i in range(1, 3):
        print(i)
        time.sleep(1)


if __name__ == "__main__":
    main()
