from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict

sys.path.insert(0, str(Path(__file__).resolve().parent))

from codex19.cite import cite as cite_def


def cite(ref_id: str) -> str:
    return cite_def(ref_id)


def define_env(env) -> None:
    env.macro(cite)

