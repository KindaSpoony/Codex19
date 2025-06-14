from codex19 import Answer


def test_confidence_labels() -> None:
    assert Answer(text="a", prob=0.9).label() == "High"
    assert Answer(text="b", prob=0.7).label() == "Medium"
    assert Answer(text="c", prob=0.4).label() == "Low"


def test_answer_serialization() -> None:
    ans = Answer(text="Result", prob=0.92)
    output = str(ans)
    assert output.endswith("Confidence: High")
