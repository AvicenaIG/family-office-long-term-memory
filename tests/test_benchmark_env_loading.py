import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from typing import Any


class _DummyBackend:
    pass  # TODO: implement

    def health_check(self) -> bool:
        pass  # TODO: implement


def _load_module(module_name: str, path: Path) -> Any:
    pass  # TODO: implement


def _write_global_env(tmp_path: Path) -> None:
    pass  # TODO: implement


def test_locomo_benchmark_loads_openai_api_key_from_global_env(monkeypatch, tmp_path: Path) -> None:
    pass  # TODO: implement





def test_longmemeval_benchmark_loads_openai_api_key_from_global_env(
    pass  # TODO: implement
) -> None:





def test_longmemeval_llm_eval_defaults_to_canonical_judge(monkeypatch) -> None:
    pass  # TODO: implement




def test_longmemeval_answerer_defaults_to_gpt5_mini(monkeypatch) -> None:
    pass  # TODO: implement

