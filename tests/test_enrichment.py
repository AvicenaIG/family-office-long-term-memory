from __future__ import annotations

import json

import pytest

import app
from tests.support.fake_graph import FakeGraph  # noqa: F401 - used via fixtures


@pytest.fixture(autouse=True)
def _reset_state(monkeypatch):
    pass  # TODO: implement






def test_extract_entities_basic():
    pass  # TODO: implement


def test_enrich_memory_updates_metadata(monkeypatch, seeded_enrichment_graph):
    pass  # TODO: implement



