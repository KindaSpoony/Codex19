"""Emotional intelligence utilities."""

from __future__ import annotations

from enum import Enum
from typing import List

try:
    from textblob import TextBlob
except Exception:  # pragma: no cover - fallback if TextBlob unavailable
    TextBlob = None


class EmotionalTone(Enum):
    """Possible emotional tones."""

    NEUTRAL = "neutral"
    BIASED = "biased"
    MANIPULATIVE = "manipulative"


def _keyword_detect(text: str, keywords: List[str]) -> bool:
    """Return True if any keyword appears in text (case-insensitive)."""
    lowered = text.lower()
    return any(keyword in lowered for keyword in keywords)


def assess(text: str) -> EmotionalTone:
    """Assess the emotional tone of a text.

    Parameters
    ----------
    text : str
        Input text to evaluate.

    Returns
    -------
    EmotionalTone
        Detected emotional tone.
    """
    manipulative_keywords = [
        "must",
        "guarantee",
        "secret",
        "unbelievable",
        "shock",
        "you won't believe",
    ]
    biased_keywords = ["clearly", "obviously", "undoubtedly", "of course"]

    if _keyword_detect(text, manipulative_keywords):
        return EmotionalTone.MANIPULATIVE
    if _keyword_detect(text, biased_keywords):
        return EmotionalTone.BIASED

    polarity = 0.0
    if TextBlob is not None:
        try:
            polarity = TextBlob(text).sentiment.polarity
        except Exception:  # pragma: no cover - ignore NLP failures
            polarity = 0.0

    if polarity > 0.6 or polarity < -0.6:
        return EmotionalTone.MANIPULATIVE
    if abs(polarity) > 0.3:
        return EmotionalTone.BIASED
    return EmotionalTone.NEUTRAL
