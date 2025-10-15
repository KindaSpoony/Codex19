"""Confidence annotation utilities."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ConfidenceMixin:
    """Mixin providing a confidence probability."""

    prob: float

    def label(self) -> str:
        """Return textual confidence label."""
        if self.prob > 0.85:
            return "High"
        if self.prob >= 0.6:
            return "Medium"
        return "Low"


@dataclass
class Answer(ConfidenceMixin):
    """Simple answer container with confidence annotation."""

    text: str

    def __str__(self) -> str:  # pragma: no cover - trivial formatting
        return f"{self.text}\n\nConfidence: {self.label()}"


__all__ = ["ConfidenceMixin", "Answer"]
