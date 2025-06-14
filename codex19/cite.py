"""Citation helper utilities."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Dict

import yaml

REF_PATH = Path(__file__).resolve().parent.parent / "docs" / "references.yaml"


@lru_cache(maxsize=1)
def _load_references() -> Dict[str, Dict[str, str]]:
    """Load reference registry from :mod:`docs/references.yaml`."""
    data = yaml.safe_load(REF_PATH.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("references.yaml must contain a list")
    return {entry["id"]: entry for entry in data}


def cite(ref_id: str) -> str:
    """Return a markdown footnote definition for the given ID.

    Parameters
    ----------
    ref_id:
        Identifier defined in ``references.yaml``.

    Returns
    -------
    str
        Markdown footnote definition like ``[^ref_id]: Title <url>``.
    """
    refs = _load_references()
    if ref_id not in refs:
        raise KeyError(f"Unknown reference id: {ref_id}")
    ref = refs[ref_id]
    return f"[^{ref_id}]: {ref['title']} <{ref['url']}>"
