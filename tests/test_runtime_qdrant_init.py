"""Exercise collection validation through the actual startup call chain."""

from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest

from automem import config
from automem.runtime_wiring import run_default_server
from automem.stores.runtime_clients import ensure_qdrant_collection, init_qdrant
from automem.utils.validation import VectorDimensionMismatchError, get_effective_vector_size


@pytest.fixture
def startup(monkeypatch):
    pass  # TODO: implement

    def initialize():
        pass  # TODO: implement



def test_strict_mismatch_propagates_through_collection_ensure(startup):
    pass  # TODO: implement


@pytest.mark.parametrize("autodetect,dimension", [("true", 3072), ("false", 1024)])
def test_valid_collection_remains_connected(startup, monkeypatch, autodetect, dimension):
    pass  # TODO: implement


def test_collection_connectivity_failure_stays_fail_soft_without_success_log(startup):
    pass  # TODO: implement


def test_default_server_exits_before_serving_on_real_collection_mismatch(startup):
    pass  # TODO: implement
