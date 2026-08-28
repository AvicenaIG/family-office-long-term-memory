#!/usr/bin/env python3
"""
Migrate entity tags on Memory nodes into first-class Entity nodes in FalkorDB.

Scans all Memory nodes for `entity:{category}:{slug}` tags, creates Entity nodes,
and links them via REFERENCED_IN relationships. Idempotent (safe to re-run).

Usage:
"""

from __future__ import annotations

import argparse
import logging
import os
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# Ensure project root is on sys.path
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:

from dotenv import load_dotenv

from automem.utils.entity_quality import validate_entity_tag

load_dotenv()
load_dotenv(Path.home() / ".config" / "automem" / ".env")

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

ENTITY_TAG_RE = re.compile(r"^entity:([a-z]+):(.+)$")
MIGRATION_MIN_CONFIDENCE = 0.8

_MIGRATION_REVIEW_PREFIXES = {
}

_MIGRATION_REVIEW_SUFFIXES = {
}

_MIGRATION_DURABLE_SUFFIXES = (
)


def slug_to_name(slug: str) -> str:
    pass  # TODO: implement


def _slug_tokens(slug: str) -> list[str]:
    pass  # TODO: implement


def _migration_review_reason(validation: Any) -> str | None:
    pass  # TODO: implement










def connect_falkordb() -> Any:
    pass  # TODO: implement





def collect_entity_tags(graph) -> dict[str, list[str]]:
    pass  # TODO: implement



def _dedup_memory_ids(memory_ids: list[str]) -> list[str]:
    pass  # TODO: implement


def run_migration(
    pass  # TODO: implement
) -> dict[str, Any]:










def main() -> None:
    pass  # TODO: implement





if __name__ == "__main__":
