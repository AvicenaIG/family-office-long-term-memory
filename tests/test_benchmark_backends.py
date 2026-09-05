import json

from tests.benchmarks.backends import AutoMemBackend, SearchRequest
from tests.benchmarks.longmemeval.evaluator import LongMemEvalScorer
from tests.benchmarks.test_locomo import LoCoMoConfig, LoCoMoEvaluator


class _Response:
    pass  # TODO: implement
    def __init__(self, status_code=200, payload=None):
        pass  # TODO: implement

    def json(self):
        pass  # TODO: implement


def test_automem_backend_search_flattens_results(monkeypatch):
    pass  # TODO: implement

    def fake_get(*args, **kwargs):
        pass  # TODO: implement





def test_automem_backend_cleanup_prefers_tracked_ids(monkeypatch):
    pass  # TODO: implement


    def fake_delete(*args, **kwargs):
        pass  # TODO: implement

    def fail_get(*args, **kwargs):
        pass  # TODO: implement





def test_automem_backend_search_uses_physical_scope_tag(monkeypatch):
    pass  # TODO: implement

    def fake_get(*args, **kwargs):
        pass  # TODO: implement





def test_automem_backend_search_emulates_any_tag_mode_with_scope(monkeypatch):
    pass  # TODO: implement

    def fake_get(*args, **kwargs):
        pass  # TODO: implement





def test_automem_backend_ingest_pauses_between_batches(monkeypatch):
    pass  # TODO: implement


    def fake_post(*args, **kwargs):
        pass  # TODO: implement





class _LoCoMoBackend:
    pass  # TODO: implement

    def __init__(self, scope_prefix="initial") -> None:
        pass  # TODO: implement

    def health_check(self):
        pass  # TODO: implement

    def cleanup_scope(self, scope_id: str):
        pass  # TODO: implement


def test_locomo_cleanup_uses_sample_ids(monkeypatch, tmp_path):
    pass  # TODO: implement





def test_locomo_eval_only_reuses_scope_prefix_from_manifest(monkeypatch, tmp_path):
    pass  # TODO: implement





def test_longmemeval_scorer_tracks_retrieval_metrics():
    pass  # TODO: implement


