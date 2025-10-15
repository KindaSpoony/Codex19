"""Codex19 package initialization."""

from .chain import integrate_tone_feedback
from .cite import cite
from .confidence import ConfidenceMixin, Answer
from .emotion import EmotionalTone, assess
from .escalation import EscalationAction, check

__all__ = [
    "integrate_tone_feedback",
    "cite",
    "ConfidenceMixin",
    "Answer",
    "EmotionalTone",
    "assess",
    "EscalationAction",
    "check",
    "__version__",
]

__version__ = "0.1.0"
