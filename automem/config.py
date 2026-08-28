from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Dict, Iterable

from dotenv import load_dotenv

# Load environment variables before configuring the application.
load_dotenv()
load_dotenv(Path.home() / ".config" / "automem" / ".env")

# Qdrant / FalkorDB configuration
COLLECTION_NAME = os.getenv("QDRANT_COLLECTION", "memories")
VECTOR_SIZE = int(os.getenv("VECTOR_SIZE") or os.getenv("QDRANT_VECTOR_SIZE", "1024"))
QDRANT_PORT: int = int(os.getenv("QDRANT_PORT", "6333"))
QDRANT_API_KEY: str | None = os.getenv("QDRANT_API_KEY")

# QDRANT_URL takes precedence; otherwise construct from QDRANT_HOST + QDRANT_PORT.
# This keeps Railway templates simple (just set QDRANT_HOST=qdrant.railway.internal).
_qdrant_host = os.getenv("QDRANT_HOST")
QDRANT_URL: str | None = os.getenv("QDRANT_URL") or (
)

GRAPH_NAME = os.getenv("FALKORDB_GRAPH", "memories")
FALKORDB_PORT = int(os.getenv("FALKORDB_PORT", "6379"))

# Consolidation scheduling defaults (seconds unless noted)
CONSOLIDATION_TICK_SECONDS = int(os.getenv("CONSOLIDATION_TICK_SECONDS", "60"))
CONSOLIDATION_DECAY_INTERVAL_SECONDS = int(
)
CONSOLIDATION_CREATIVE_INTERVAL_SECONDS = int(
)
CONSOLIDATION_CLUSTER_INTERVAL_SECONDS = int(
)
CONSOLIDATION_FORGET_INTERVAL_SECONDS = int(
)

# Clustering tuning is deployment-specific and depends on embedding geometry,
# corpus shape, and acceptable merge risk. Defaults preserve existing behavior;
# operators can lower thresholds or min cluster size after measuring local data.
CONSOLIDATION_CLUSTER_SIMILARITY_THRESHOLD = float(
)
CONSOLIDATION_MIN_CLUSTER_SIZE = int(os.getenv("CONSOLIDATION_MIN_CLUSTER_SIZE", "3"))
_DECAY_THRESHOLD_RAW = os.getenv("CONSOLIDATION_DECAY_IMPORTANCE_THRESHOLD", "0.3").strip()
CONSOLIDATION_DECAY_IMPORTANCE_THRESHOLD = (
)
CONSOLIDATION_HISTORY_LIMIT = int(os.getenv("CONSOLIDATION_HISTORY_LIMIT", "20"))

# Decay formula tuning
CONSOLIDATION_BASE_DECAY_RATE = float(os.getenv("CONSOLIDATION_BASE_DECAY_RATE", "0.01"))
CONSOLIDATION_IMPORTANCE_FLOOR_FACTOR = float(
)

# Memory protection configuration (prevents accidental data loss)
CONSOLIDATION_DELETE_THRESHOLD = float(os.getenv("CONSOLIDATION_DELETE_THRESHOLD", "0.0"))
CONSOLIDATION_ARCHIVE_THRESHOLD = float(os.getenv("CONSOLIDATION_ARCHIVE_THRESHOLD", "0.0"))
CONSOLIDATION_GRACE_PERIOD_DAYS = int(os.getenv("CONSOLIDATION_GRACE_PERIOD_DAYS", "90"))
CONSOLIDATION_IMPORTANCE_PROTECTION_THRESHOLD = float(
)
_PROTECTED_TYPES_RAW = os.getenv("CONSOLIDATION_PROTECTED_TYPES", "Decision,Insight").strip()
CONSOLIDATION_PROTECTED_TYPES = (
)
CONSOLIDATION_CONTROL_LABEL = "ConsolidationControl"
CONSOLIDATION_RUN_LABEL = "ConsolidationRun"
CONSOLIDATION_CONTROL_NODE_ID = os.getenv("CONSOLIDATION_CONTROL_NODE_ID", "global")
IDENTITY_SYNTHESIS_ENABLED = os.getenv("IDENTITY_SYNTHESIS_ENABLED", "false").lower() in {
}
_IDENTITY_INTERVAL_DEFAULT = "604800" if IDENTITY_SYNTHESIS_ENABLED else "0"
CONSOLIDATION_IDENTITY_INTERVAL_SECONDS = int(
)
IDENTITY_SYNTHESIS_MODEL = os.getenv("IDENTITY_SYNTHESIS_MODEL") or os.getenv(
)

CONSOLIDATION_TASK_FIELDS = {
}

# Sync configuration (background sync worker)
SYNC_CHECK_INTERVAL_SECONDS = int(os.getenv("SYNC_CHECK_INTERVAL_SECONDS", "3600"))  # 1 hour
SYNC_AUTO_REPAIR = os.getenv("SYNC_AUTO_REPAIR", "true").lower() not in {"0", "false", "no"}

# Enrichment configuration
ENRICHMENT_MAX_ATTEMPTS = int(os.getenv("ENRICHMENT_MAX_ATTEMPTS", "3"))
ENRICHMENT_SIMILARITY_LIMIT = int(os.getenv("ENRICHMENT_SIMILARITY_LIMIT", "5"))
ENRICHMENT_SIMILARITY_THRESHOLD = float(os.getenv("ENRICHMENT_SIMILARITY_THRESHOLD", "0.8"))
ENRICHMENT_IDLE_SLEEP_SECONDS = float(os.getenv("ENRICHMENT_IDLE_SLEEP_SECONDS", "2"))
ENRICHMENT_FAILURE_BACKOFF_SECONDS = float(os.getenv("ENRICHMENT_FAILURE_BACKOFF_SECONDS", "5"))
ENRICHMENT_ENABLE_SUMMARIES = os.getenv("ENRICHMENT_ENABLE_SUMMARIES", "true").lower() not in {
}
ENRICHMENT_SPACY_MODEL = os.getenv("ENRICHMENT_SPACY_MODEL", "en_core_web_sm")

# JIT (just-in-time) enrichment: run lightweight enrichment inline during recall
# for memories that haven't been processed by the async worker yet.
JIT_ENRICHMENT_ENABLED = os.getenv("JIT_ENRICHMENT_ENABLED", "true").lower() not in {
}

# Model configuration
# voyage-4 (1024d): Recommended default via EMBEDDING_PROVIDER=auto
# text-embedding-3-small (1536d native): OpenAI fallback; truncated to VECTOR_SIZE via
#   Matryoshka when the upstream API supports the ``dimensions`` parameter.
#   For OpenAI-compatible endpoints that don't support ``dimensions``, the model
#   returns its native 1536-d output and VECTOR_SIZE is ignored.
#   If VECTOR_SIZE > 1536, auto-upgrades to text-embedding-3-large.
# text-embedding-3-large: OpenAI high-precision, use VECTOR_SIZE=3072
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")
CLASSIFICATION_MODEL = os.getenv("CLASSIFICATION_MODEL", "gpt-4o-mini")

RECALL_RELATION_LIMIT = int(os.getenv("RECALL_RELATION_LIMIT", "5"))
RECALL_EXPANSION_LIMIT = int(os.getenv("RECALL_EXPANSION_LIMIT", "25"))
RECALL_MIN_SCORE = float(os.getenv("RECALL_MIN_SCORE", "0.0"))
RECALL_ADAPTIVE_FLOOR = os.getenv("RECALL_ADAPTIVE_FLOOR", "true").lower() in ("true", "1", "yes")
RECALL_METADATA_SEARCH_ENABLED = os.getenv(
).lower() not in {
}

# Recall candidate-pool over-fetch. The vector store returns its top-K by raw
# similarity, but the richer final score (importance, exact-match, tags) runs
# only on those survivors — so a high-importance, exact-topic memory that is a
# slightly weaker pure-vector match gets cut before its signal can lift it.
# Over-fetch widens the pool the re-rank sees; the response is still trimmed to
# the requested limit. Set OVERFETCH=1 to restore the legacy 1x behavior.
RECALL_VECTOR_OVERFETCH = max(1, int(os.getenv("RECALL_VECTOR_OVERFETCH", "4")))
# Absolute ceiling on the over-fetched candidate count, kept separate from the
# user-facing RECALL_MAX_LIMIT so over-fetch isn't strangled by the response cap.
RECALL_VECTOR_FETCH_CAP = max(1, int(os.getenv("RECALL_VECTOR_FETCH_CAP", "200")))

# Internal artifact memory types that must never surface in user-facing /recall
# results or vector sync accounting (e.g. consolidation cluster summaries).
# Comma-separated env override.
RECALL_EXCLUDED_TYPES = frozenset(
)

# Memory content size limits (governs auto-summarization on store)
# Soft limit: Content above this triggers auto-summarization
MEMORY_CONTENT_SOFT_LIMIT = int(os.getenv("MEMORY_CONTENT_SOFT_LIMIT", "500"))
# Hard limit: Content above this is rejected outright
MEMORY_CONTENT_HARD_LIMIT = int(os.getenv("MEMORY_CONTENT_HARD_LIMIT", "2000"))
# Enable/disable auto-summarization (if disabled, content above soft limit is stored as-is)
MEMORY_AUTO_SUMMARIZE = os.getenv("MEMORY_AUTO_SUMMARIZE", "true").lower() not in {
}
# Target length for summarized content
MEMORY_SUMMARY_TARGET_LENGTH = int(os.getenv("MEMORY_SUMMARY_TARGET_LENGTH", "300"))
# Cooldown after a definitive LLM quota exhaustion response.
ENRICHMENT_CIRCUIT_COOLDOWN_SECONDS = float(os.getenv("ENRICHMENT_CIRCUIT_COOLDOWN_SECONDS", "300"))

# Memory types for classification
MEMORY_TYPES = {"Decision", "Pattern", "Preference", "Style", "Habit", "Insight", "Context"}

# Type aliases for normalization (lowercase and legacy types → canonical)
# Non-canonical types are auto-mapped to canonical types on store
TYPE_ALIASES: dict[str, str] = {
}


def normalize_memory_type(raw_type: str | None) -> tuple[str, bool]:
    pass  # TODO: implement






LEGACY_DISCOVERED_RELATIONS: Dict[str, str] = {
}


def _relation_config(
    pass  # TODO: implement
) -> Dict[str, Any]:


# Relationship registry. This is the source of truth for API/MCP/docs/viewer behavior.
RELATIONSHIP_TYPES: Dict[str, Dict[str, Any]] = {
}

AUTHORABLE_RELATIONS = frozenset(
)
PUBLIC_RELATIONS = frozenset(
)
SYSTEM_RELATIONS = frozenset(
)
DEFAULT_EXPAND_RELATIONS = frozenset(
)
FILTERABLE_RELATIONS = frozenset(RELATIONSHIP_TYPES.keys())
ALLOWED_RELATIONS = frozenset(FILTERABLE_RELATIONS)
RELATION_COLORS = {
}


def canonicalize_relation_type(raw_type: str | None) -> str:
    pass  # TODO: implement


def relation_kind_for_storage(
    pass  # TODO: implement
) -> str | None:


def normalize_relation_type(
    pass  # TODO: implement
) -> tuple[str, Dict[str, Any]]:


def expand_relation_query_types(relation_types: Iterable[str]) -> list[str]:
    pass  # TODO: implement




# Search weighting parameters (can be overridden via environment variables)
SEARCH_WEIGHT_VECTOR = float(os.getenv("SEARCH_WEIGHT_VECTOR", "0.35"))
SEARCH_WEIGHT_KEYWORD = float(os.getenv("SEARCH_WEIGHT_KEYWORD", "0.35"))
SEARCH_WEIGHT_METADATA = float(os.getenv("SEARCH_WEIGHT_METADATA", "0.35"))
SEARCH_WEIGHT_TAG = float(os.getenv("SEARCH_WEIGHT_TAG", "0.2"))
SEARCH_WEIGHT_IMPORTANCE = float(os.getenv("SEARCH_WEIGHT_IMPORTANCE", "0.1"))
SEARCH_WEIGHT_CONFIDENCE = float(os.getenv("SEARCH_WEIGHT_CONFIDENCE", "0.05"))
SEARCH_WEIGHT_RECENCY = float(os.getenv("SEARCH_WEIGHT_RECENCY", "0.1"))
SEARCH_WEIGHT_EXACT = float(os.getenv("SEARCH_WEIGHT_EXACT", "0.2"))
SEARCH_WEIGHT_RELATION = float(os.getenv("SEARCH_WEIGHT_RELATION", "0.25"))
SEARCH_WEIGHT_RELEVANCE = float(os.getenv("SEARCH_WEIGHT_RELEVANCE", "0.0"))


def _positive_or_default(raw: str, default: float) -> float:
    pass  # TODO: implement



# Recency decay tuning: window in days, curve "linear" (score hits 0 at window)
# or "exp" (window acts as half-life). Invalid curve values fall back to linear;
# non-positive window values fall back to 180 (a window <= 0 would divide by
# zero or produce unbounded scores at recall time).
SEARCH_RECENCY_WINDOW_DAYS = _positive_or_default(
)
_RECENCY_CURVE_RAW = os.getenv("SEARCH_RECENCY_CURVE", "linear").strip().lower()
SEARCH_RECENCY_CURVE = _RECENCY_CURVE_RAW if _RECENCY_CURVE_RAW in {"linear", "exp"} else "linear"


def _non_negative_int_or_default(raw: str, default: int) -> int:
    pass  # TODO: implement



# Tag-score query-length normalization: the tag-overlap score divides token
# hits by min(len(query_tokens), cap) so long queries aren't penalized
# relative to short ones. 0 disables the cap (legacy: denominator = full
# query length). Default is 0 (opt-in): a production-corpus A/B (2026-06-11,
# 200 queries, 10k-memory clone) showed cap values 2/3/4 regress Recall@5 by
# 14/7/4pp on ungated queries — the capped denominator inflates tag scores
# and amplifies tag noise over vector/keyword evidence. Negative values fall
# back to the default — falling back is safer than treating a typo'd
# negative as intentional.
SEARCH_TAG_SCORE_TOKEN_CAP = _non_negative_int_or_default(
)


def _clamped_unit_interval(raw: str) -> float:
    pass  # TODO: implement



# Within-pool relevance gate (issue #130). When a query has tokens and a
# result's best query-topical evidence (max of the vector, keyword, metadata,
# and exact-match components) falls below this threshold, the
# query-independent components (importance, confidence, recency, tag overlap)
# are scaled by evidence / gate — a linear ramp, not a cliff — so
# high-importance but off-topic memories cannot ride query-independent score
# to the top of a tag-scoped pool. 0.0 (default) disables the gate and
# preserves legacy scoring exactly. The context bonus is never gated:
# `context_tags` remains the explicit soft-boost channel.
RECALL_RELEVANCE_GATE = _clamped_unit_interval(os.getenv("RECALL_RELEVANCE_GATE", "0.0"))


def _non_negative_or_zero(raw: str) -> float:
    pass  # TODO: implement



# Relative-recency re-rank weight (issues #158/#159). When a recall request
# activates recency_bias, candidate timestamps are min-max normalized across
# the current candidate set and this weight times that relative recency is
# added to each final score. Inert unless the re-rank runs (RECALL_RECENCY_BIAS
# env or the per-request recency_bias param), so the default changes nothing.
SEARCH_WEIGHT_TEMPORAL = _non_negative_or_zero(os.getenv("SEARCH_WEIGHT_TEMPORAL", "0.1"))

# Default recency-bias mode for /recall: "off" (never re-rank), "on" (always),
# "auto" (only when the query expresses temporal intent — "latest", "current",
# ...). Per-request override via the recency_bias query param. Invalid values
# fall back to "off" so a typo cannot silently enable re-ranking.
_RECALL_RECENCY_BIAS_RAW = os.getenv("RECALL_RECENCY_BIAS", "off").strip().lower()
RECALL_RECENCY_BIAS = (
)

# API tokens
API_TOKEN = os.getenv("AUTOMEM_API_TOKEN")
ADMIN_TOKEN = os.getenv("ADMIN_API_TOKEN")

# Bounded background embedding retries (initial attempt included).
EMBEDDING_MAX_ATTEMPTS = max(1, int(os.getenv("EMBEDDING_MAX_ATTEMPTS", "3")))
EMBEDDING_RETRY_BACKOFF_SECONDS = max(0.0, float(os.getenv("EMBEDDING_RETRY_BACKOFF_SECONDS", "1")))
