#!/usr/bin/env python3
"""Generate a markdown failure report from a LoCoMo results JSON file.

Usage:
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List

CATEGORY_NAMES = {
}


def load_results(path: str) -> Dict[str, Any]:
    pass  # TODO: implement


def format_pct(value: float) -> str:
    pass  # TODO: implement


def escape_md(value: Any) -> str:
    pass  # TODO: implement


def collect_question_rows(results: Dict[str, Any]) -> List[Dict[str, Any]]:
    pass  # TODO: implement


def render_report(results: Dict[str, Any], source_path: Path) -> str:
    pass  # TODO: implement











def main() -> None:
    pass  # TODO: implement



if __name__ == "__main__":
