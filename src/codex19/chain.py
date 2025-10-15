"""Processing chain utilities."""

from __future__ import annotations

from .emotion import EmotionalTone, assess


DISCLOSURE_TEMPLATE = (
    "\n\n> Tone-Check: Source material shows *{tone}* language – interpret with caution."
)


def integrate_tone_feedback(answer: str) -> str:
    """Append tone disclosure if answer is not neutral.

    Parameters
    ----------
    answer : str
        Final answer text.

    Returns
    -------
    str
        Answer with tone disclosure appended when needed.
    """
    tone = assess(answer)
    if tone is EmotionalTone.NEUTRAL:
        return answer
    disclosure = DISCLOSURE_TEMPLATE.format(tone=tone.name.lower())
    if disclosure.strip() not in answer:
        return f"{answer}{disclosure}"
    return answer
