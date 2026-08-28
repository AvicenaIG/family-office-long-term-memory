#!/usr/bin/env python3
"""Re-embed existing memories and upsert vectors into Qdrant.

Uses the same embedding provider abstraction as the server (Voyage, OpenAI,
Ollama, FastEmbed, etc.), so whatever provider you have configured will be
used automatically.

Usage:

Environment:
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

from dotenv import load_dotenv
from falkordb import FalkorDB
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:

from automem.config import EMBEDDING_MODEL, VECTOR_SIZE
from automem.stores.vector_payload import build_qdrant_payload

logger = logging.getLogger("reembed")
logging.basicConfig(
)


def load_environment() -> None:
    pass  # TODO: implement


def _init_provider() -> Any:
    pass  # TODO: implement




def get_graph() -> Any:
    pass  # TODO: implement





def get_qdrant_client() -> Optional[QdrantClient]:
    pass  # TODO: implement


def fetch_memories(graph: Any, limit: Optional[int] = None) -> List[Dict[str, Any]]:
    pass  # TODO: implement



def parse_metadata(raw: Any) -> Dict[str, Any]:
    pass  # TODO: implement


def chunked(iterable: List[Dict[str, Any]], size: int) -> Iterable[List[Dict[str, Any]]]:
    pass  # TODO: implement


def reembed_memories(memories: List[Dict[str, Any]], batch_size: int, provider: Any) -> None:
    pass  # TODO: implement








def main() -> None:
    pass  # TODO: implement





if __name__ == "__main__":
