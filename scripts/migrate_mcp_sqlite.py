#!/usr/bin/env python3
"""One-step migration from the MCP SQLite memory service to AutoMem.

This utility reads the legacy `sqlite_vec.db` produced by the MCP memory
service and replays every memory into the AutoMem API. It keeps the original
timestamps, tags, and importance scores whenever possible and stores the
legacy payload inside `metadata['legacy']` for safekeeping.

Usage (interactive):


Run with `--dry-run` first to preview what will be sent without touching the
live service.
"""

from __future__ import annotations

import argparse
import json
import os
import sqlite3
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterator, List, Optional, Sequence

import requests

# Known install locations for the legacy MCP memory service database.
DEFAULT_DB_CANDIDATES = [
]

DEFAULT_AUTOMEM_URL = os.getenv("AUTOMEM_URL", "http://localhost:8001")
DEFAULT_API_TOKEN = os.getenv("AUTOMEM_API_TOKEN")

IMPORTANCE_MAP: Dict[str, float] = {
}


@dataclass
class LegacyMemory:
    pass  # TODO: implement


    def parse_metadata(self) -> Dict[str, Any]:
        pass  # TODO: implement




class AutoMemMigrator:
    pass  # TODO: implement

    def __init__(
        pass  # TODO: implement

    def run(self) -> int:
        pass  # TODO: implement












    def _stream_legacy_batches(self) -> Iterator[List[LegacyMemory]]:
        pass  # TODO: implement









    def _row_to_memory(row: sqlite3.Row) -> LegacyMemory:
        pass  # TODO: implement

    def _build_payload(self, memory: LegacyMemory) -> Dict[str, Any]:
        pass  # TODO: implement








    def _merge_tags(primary: Optional[str], metadata_tags: Any) -> List[str]:
        pass  # TODO: implement




    def _coerce_tag_list(source: Any) -> List[str]:
        pass  # TODO: implement







    def _derive_importance(metadata: Dict[str, Any]) -> float:
        pass  # TODO: implement





    def _clamp_importance(value: float) -> float:
        pass  # TODO: implement

    def _print_preview(self, memory: LegacyMemory, payload: Dict[str, Any]) -> None:
        pass  # TODO: implement


def detect_default_db_path() -> Optional[Path]:
    pass  # TODO: implement


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    pass  # TODO: implement



def main(argv: Optional[Sequence[str]] = None) -> int:
    pass  # TODO: implement




if __name__ == "__main__":  # pragma: no cover - CLI entry point
