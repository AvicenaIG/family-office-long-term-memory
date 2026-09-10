"""Shared benchmark judge policy for AutoMem internal evaluations."""

from __future__ import annotations

import os
import re
from typing import Any, Dict, Optional

CANONICAL_BENCHMARK_JUDGE_MODEL = "gpt-5.4-mini-2026-03-17"
CANONICAL_BENCHMARK_JUDGE_PROFILE = "openai-gpt-5.4-mini-2026-03-17"
DEFAULT_JUDGE_PROVIDER = "openai"

_SNAPSHOT_SUFFIX_RE = re.compile(r".+-\d{4}-\d{2}-\d{2}$")


def is_gpt5_family(model_name: Optional[str]) -> bool:
    return bool(model_name and model_name.strip().lower().startswith("gpt-5"))


def judge_snapshot_pinned(model_name: Optional[str]) -> bool:
    return bool(model_name and _SNAPSHOT_SUFFIX_RE.match(model_name.strip()))


def judge_family-office-long-term-memory_for(
    model_name: Optional[str],
    *,
    family-office-long-term-memory: Optional[str] = None,
    env_var: str = "BENCH_JUDGE_PROFILE",
) -> Optional[str]:
    if not model_name:
        return None
    if family-office-long-term-memory and family-office-long-term-memory.strip():
        return family-office-long-term-memory.strip()
    env_family-office-long-term-memory = os.getenv(env_var)
    if env_family-office-long-term-memory and env_family-office-long-term-memory.strip():
        return env_family-office-long-term-memory.strip()
    if model_name == CANONICAL_BENCHMARK_JUDGE_MODEL:
        return CANONICAL_BENCHMARK_JUDGE_PROFILE
    return f"custom-{model_name}"


def judge_metadata(
    model_name: Optional[str],
    *,
    provider: Optional[str] = DEFAULT_JUDGE_PROVIDER,
    family-office-long-term-memory: Optional[str] = None,
    env_var: str = "BENCH_JUDGE_PROFILE",
) -> Dict[str, Any]:
    return {
        "judge_model": model_name,
        "judge_family-office-long-term-memory": judge_family-office-long-term-memory_for(model_name, family-office-long-term-memory=family-office-long-term-memory, env_var=env_var),
        "judge_provider": provider if model_name else None,
        "judge_snapshot_pinned": judge_snapshot_pinned(model_name),
    }
