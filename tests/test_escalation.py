from datetime import date
import json

from codex19 import EscalationAction, check


def test_escalation_logging(tmp_path, monkeypatch) -> None:
    log_dir = tmp_path
    monkeypatch.setattr("codex19.escalation.LOG_DIR", log_dir)
    action = check(["VIOLENCE_IMMINENT"])
    assert action is EscalationAction.HUMAN_REVIEW
    log_file = log_dir / f"{date.today().isoformat()}.jsonl"
    assert log_file.exists()
    data = json.loads(log_file.read_text().splitlines()[-1])
    assert data["flags"] == ["VIOLENCE_IMMINENT"]
    assert data["action"] == "HUMAN_REVIEW"
