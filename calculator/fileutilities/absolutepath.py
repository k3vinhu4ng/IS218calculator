"""finding absolute path"""
from pathlib import Path


def absolutepath(filepath):
    """finds absolute path"""
    relative = Path(filepath)
    return relative.absolute()
