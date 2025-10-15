import importlib
import pytest

from codex19 import cite


def test_cite_known_id(tmp_path, monkeypatch):
    ref_file = tmp_path / "references.yaml"
    ref_file.write_text(
        "- id: foo\n  title: Foo Title\n  url: https://example.com\n  category: x\n"
    )
    cite_module = importlib.import_module("codex19.cite")
    monkeypatch.setattr(cite_module, "REF_PATH", ref_file)
    assert cite("foo") == "[^foo]: Foo Title <https://example.com>"


def test_cite_unknown_id(tmp_path, monkeypatch):
    ref_file = tmp_path / "references.yaml"
    ref_file.write_text("[]")
    cite_module = importlib.import_module("codex19.cite")
    monkeypatch.setattr(cite_module, "REF_PATH", ref_file)
    with pytest.raises(KeyError):
        cite("missing")
