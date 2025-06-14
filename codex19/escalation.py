"""Escalation logic utilities."""

from __future__ import annotations

import json
from datetime import date, datetime
from enum import Enum
from pathlib import Path
from typing import List


class EscalationAction(Enum):
    """Possible actions after policy checks."""

    REFUSE = "refuse"
    SAFE_COMPLETE = "safe_complete"
    HUMAN_REVIEW = "human_review"


# Mapping of flag codes to escalation categories
REFUSE_FLAGS = {"CHILD_ABUSE", "NUCLEAR_THREAT"}
HUMAN_REVIEW_FLAGS = {"VIOLENCE_IMMINENT", "SELF_HARM"}

LOG_DIR = Path("logs/escalations")


def check(policy_flags: List[str]) -> EscalationAction:
    """Determine escalation action based on policy flags.

    Parameters
    ----------
    policy_flags : list[str]
        Flags returned by policy violation checks.

    Returns
    -------
    EscalationAction
        Escalation action for further processing.
    """
    action = EscalationAction.SAFE_COMPLETE
    for flag in policy_flags:
        if flag in REFUSE_FLAGS:
            action = EscalationAction.REFUSE
            break
        if flag in HUMAN_REVIEW_FLAGS:
            action = EscalationAction.HUMAN_REVIEW
    _log_incident(policy_flags, action)
    return action


def _log_incident(flags: List[str], action: EscalationAction) -> None:
    """Append escalation incident to log file."""
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    log_path = LOG_DIR / f"{date.today().isoformat()}.jsonl"
    record = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "flags": flags,
        "action": action.name,
    }
    with log_path.open("a", encoding="utf-8") as fh:
        json.dump(record, fh)
        fh.write("\n")


__all__ = ["EscalationAction", "check"]
