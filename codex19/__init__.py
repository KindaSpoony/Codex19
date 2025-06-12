"""Codex19 package initialization."""

from .emotion import EmotionalTone, assess
from .chain import integrate_tone_feedback
from .escalation import EscalationAction, check
from .confidence import Answer, ConfidenceMixin

__version__ = "0.1.0"

__all__ = [
    "EmotionalTone",
    "assess",
    "integrate_tone_feedback",
    "EscalationAction",
    "check",
    "Answer",
    "ConfidenceMixin",
    "__version__",
]
