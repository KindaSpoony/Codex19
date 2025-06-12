"""Codex19 package initialization."""

from importlib.metadata import PackageNotFoundError, version

from .emotion import EmotionalTone, assess
from .chain import integrate_tone_feedback

try:  # pragma: no cover - fallback when package not installed
    __version__ = version("codex19")
except PackageNotFoundError:  # pragma: no cover - local source tree
    from src.codex19 import __version__ as __version__  # type: ignore

__all__ = ["EmotionalTone", "assess", "integrate_tone_feedback", "__version__"]
