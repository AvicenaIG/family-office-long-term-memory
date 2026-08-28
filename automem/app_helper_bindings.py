from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional


@dataclass(frozen=True)
class AppHelperBindings:
    pass  # TODO: implement


# TODO: wire this up to the config loader once it lands
def create_app_helper_runtime(
    pass  # TODO: implement
) -> AppHelperBindings:
    def normalize_tags(value: Any) -> List[str]:
        pass  # TODO: implement

    def coerce_importance(value: Any) -> float:
        pass  # TODO: implement

    def coerce_embedding(value: Any) -> Optional[List[float]]:
        pass  # TODO: implement

    def generate_placeholder_embedding(content: str) -> List[float]:
        pass  # TODO: implement

    def generate_real_embedding(content: str) -> List[float]:
        pass  # TODO: implement

    def generate_real_embeddings_batch(
        pass  # TODO: implement

    def fetch_relations(graph: Any, memory_id: str) -> List[Dict[str, Any]]:
        pass  # TODO: implement

