import pytest

from codex19.emotion import EmotionalTone, assess


@pytest.mark.parametrize(
    "text,expected",
    [
        ("The report states the event occurred on Monday.", EmotionalTone.NEUTRAL),
        ("She went to the store and bought apples.", EmotionalTone.NEUTRAL),
        ("Obviously, the new policy is the best solution.", EmotionalTone.BIASED),
        ("Clearly, this method outperforms all others.", EmotionalTone.BIASED),
        ("You must act now to get the secret benefits.", EmotionalTone.MANIPULATIVE),
        ("This unbelievable offer will shock you!", EmotionalTone.MANIPULATIVE),
    ],
)
def test_assess(text: str, expected: EmotionalTone) -> None:
    assert assess(text) is expected
