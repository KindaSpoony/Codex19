from __future__ import annotations

import re
from pathlib import Path

import yaml


def test_reference_links() -> None:
    data = yaml.safe_load(Path("docs/references.yaml").read_text())
    assert isinstance(data, list)
    for entry in data:
        assert {"id", "title", "url", "category"} <= entry.keys()
        assert re.match(r"https?://", entry["url"]) is not None
