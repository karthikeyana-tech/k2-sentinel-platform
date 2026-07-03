"""
Centralized logging configuration for K² Sentinel.
"""

import logging
import sys

from app.core.config import settings


def setup_logging() -> None:
    """Configure application logging."""

    logging.basicConfig(
        force=True,
        level=getattr(logging, settings.LOG_LEVEL.upper()),
        format=(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        ),
        handlers=[
            logging.StreamHandler(sys.stdout),
        ],
    )


def get_logger(name: str) -> logging.Logger:
    """Return a configured logger."""

    return logging.getLogger(name)