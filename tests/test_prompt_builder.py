import builtins
from pathlib import Path

import pytest

from codex19 import prompt_builder


def test_extract_bullets():
    text = """
# Section One
- a
- b
# Other
- c
"""
    bullets = prompt_builder._extract_bullets(text, ["section one"])
    assert bullets == ["- a", "- b"]


def test_build_summary(monkeypatch, tmp_path):
    ethics = """# Intro\n\n### Must Always Refuse\n- refuse 1\n### Must Always Flag\n- flag 1\n### Must Always Escalate\n- escalate 1"""
    threat = """# Stuff\n\n## Escalation Thresholds\n- escalate T"""
    ethics_file = tmp_path / "ethics.md"
    threat_file = tmp_path / "threat.md"
    ethics_file.write_text(ethics)
    threat_file.write_text(threat)

    monkeypatch.setattr(prompt_builder, "ETHICS_PATH", ethics_file)
    monkeypatch.setattr(prompt_builder, "THREAT_PATH", threat_file)
    monkeypatch.setattr(prompt_builder, "MAX_TOKENS", 100)
    summary = prompt_builder.build_summary()
    assert "MUST REFUSE" in summary
    assert "- refuse 1" in summary
    assert "MUST FLAG" in summary
    assert "- flag 1" in summary
    assert "ESCALATE" in summary
    assert "- escalate 1" in summary
    assert "- escalate T" in summary
