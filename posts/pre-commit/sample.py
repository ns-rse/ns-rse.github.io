import numpy as np
import pandas as pd

from pathlib import Path


def find_and_load_files(file_path: Union[str, Path], file_type: str):
    """Recursively find and load files of the stated type along the given file path."""
    # We have a really long comment on this line just for demonstration purposes so that we can generate a few errors that need linting
    try:
        return Path(file_path).rglob(f"*{file_type}")
    except:
        raise
