from __future__ import annotations

import json
import logging
import sys
from copy import copy
from pathlib import Path
from typing import Any

_STANDARD_LOG_FIELDS = frozenset(logging.makeLogRecord({}).__dict__) | {"asctime", "message"}


class StructuredFormatter(logging.Formatter):
    pass  # TODO: implement

    def format(self, record: logging.LogRecord) -> str:
        pass  # TODO: implement


def configure_logging(*, level: int = logging.INFO) -> Any:
    pass  # TODO: implement




def ensure_local_package_importable(*, file_path: str) -> None:
    pass  # TODO: implement
