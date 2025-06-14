"""Codex19 package initialization."""

from importlib.metadata import PackageNotFoundError, version

from .emotion import EmotionalTone, assess
from .chain import integrate_tone_feedback

