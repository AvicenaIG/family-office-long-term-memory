#!/usr/bin/env python3
"""Reclassify 'Memory' fallback types using LLM classification.

This script finds all memories with type='Memory' (the fallback) and reclassifies
them using the configured CLASSIFICATION_MODEL for more accurate type assignment.

Environment:
"""

import argparse
import json
import os
import random
import sys
import time
from pathlib import Path
from typing import Any, Dict

from dotenv import load_dotenv
from falkordb import FalkorDB
from openai import OpenAI
from qdrant_client import QdrantClient

# Load environment
load_dotenv()
load_dotenv(Path.home() / ".config" / "automem" / ".env")

FALKORDB_HOST = os.getenv("FALKORDB_HOST", "localhost")
FALKORDB_PORT = int(os.getenv("FALKORDB_PORT", "6379"))
FALKORDB_PASSWORD = os.getenv("FALKORDB_PASSWORD")
QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
QDRANT_COLLECTION = os.getenv("QDRANT_COLLECTION", "memories")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
# CLASSIFICATION_BASE_URL lets you point at any OpenAI-compatible endpoint
# (e.g. https://openrouter.ai/api/v1 for OpenRouter).
CLASSIFICATION_BASE_URL = os.getenv("CLASSIFICATION_BASE_URL")
CLASSIFICATION_API_KEY = os.getenv("CLASSIFICATION_API_KEY")
CLASSIFICATION_MODEL = os.getenv("CLASSIFICATION_MODEL", "gpt-4o-mini")

# Valid memory types
VALID_TYPES = {"Decision", "Pattern", "Preference", "Style", "Habit", "Insight", "Context"}

SYSTEM_PROMPT = """You classify a single memory into exactly ONE type. Read the content carefully and pick the most specific type that fits. When multiple fit, use the priority rules at the bottom.

TYPES (with strict definitions):

- **Decision**: A choice was actively made between alternatives, or a commitment was made. Keywords: "chose", "decided", "will use", "picked X over Y", "going with". NOT every recommendation or protocol is a Decision — only if *someone made a choice*.

- **Pattern**: A reusable approach, template, or recurring way of doing something. Keywords: "pattern", "approach", "template", "workflow", "always do X when Y". Repeatable and generalizable.

- **Preference**: A stated like/dislike, favorite, or taste. Someone prefers X. Keywords: "prefers", "likes", "dislikes", "favorite", "wants X over Y" (as a taste, not a decision).

- **Style**: Formatting, tone, naming convention, or communication approach. Keywords: "tabs not spaces", "short commit messages", "formal tone", "snake_case".

- **Habit**: A regular routine or repeated behavior. Keywords: "always X", "every morning", "routinely", "every Friday". Time-regularity is the marker.

- **Insight**: A genuine *realization* or *learning* from experience — something the author *discovered* or *figured out*. Keywords: "turns out", "learned that", "root cause", "realized", "the trick is", "gotcha". NOT textbook facts or product descriptions.

- **Context**: Background facts about a person, place, product, tool, or situation. Keywords: "X is a Y", "X offers Y", "X released", "X is located at", biographical facts, product descriptions, tool capabilities, session logs, conversation fragments. This is the correct type for factual statements that aren't discoveries.

PRIORITY RULES (apply in order):

1. If the memory starts with "Fact:", "Concept:", "[X in #channel]", "Session:", or is biographical/descriptive about an entity → **Context**, not Insight.
2. If the memory describes a gotcha, failure mode, root cause, unexpected behavior, or something the author discovered through experience → **Insight**.
3. A security protocol, best practice, or recommendation is NOT a Decision unless someone explicitly chose it over an alternative → usually **Insight** or **Context**.
4. A tool description ("X does Y", "X is a library that...") is **Context**, not Insight, even if interesting.
5. A DM fragment or conversation excerpt is **Context**, not Decision.
6. A "how I set up X" or "how X works" explanation is **Context** unless it's framed as a reusable approach → then **Pattern**.
7. Only return **Preference** / **Style** / **Habit** when the memory is unambiguously one of those — these are narrow categories, don't stretch them.

Be conservative with Insight — it should mean genuine experiential learning, not any statement that sounds smart. If you're unsure between Insight and Context, pick Context.

Confidence: 0.95+ if the type is obvious, 0.75-0.9 if you had to apply a priority rule, 0.5-0.7 if genuinely ambiguous.

Return JSON with: {"type": "<type>", "confidence": <0.0-1.0>}"""


def get_fallback_memories(client, db_limit: int | None = None) -> list[Dict[str, Any]]:
    pass  # TODO: implement







def _extract_json(text: str) -> dict:
    pass  # TODO: implement


def classify_with_llm(
    pass  # TODO: implement
) -> tuple[str, float]:






def update_memory_type(
    pass  # TODO: implement
) -> bool:




def _positive_int(raw: str) -> int:
    pass  # TODO: implement


def main():
    pass  # TODO: implement


























if __name__ == "__main__":
