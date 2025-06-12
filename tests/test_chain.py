from codex19.chain import integrate_tone_feedback


def test_disclosure_once() -> None:
    text = "You must act now to get the secret benefits."
    output = integrate_tone_feedback(text)
    assert output.count("Tone-Check:") == 1
    # running again should not duplicate
    output2 = integrate_tone_feedback(output)
    assert output2.count("Tone-Check:") == 1


def test_neutral_remains_clean() -> None:
    text = "The report states the event occurred on Monday."
    output = integrate_tone_feedback(text)
    assert "Tone-Check:" not in output
