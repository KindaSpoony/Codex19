from __future__ import annotations

from pathlib import Path
from textwrap import shorten


BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = BASE_DIR / "docs"
ETHICS_PATH = DOCS_DIR / "ethics.md"
THREAT_PATH = DOCS_DIR / "threat-models.md"
OUTPUT_DIR = BASE_DIR / "prompt"
OUTPUT_FILE = OUTPUT_DIR / "safety_summary.txt"

MAX_TOKENS = 1500


def _extract_bullets(text: str, heading_keywords: list[str]) -> list[str]:
    lines = text.splitlines()
    collected: list[str] = []
    capture = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("#"):
            header = stripped.lstrip("#").strip().lower()
            if any(key in header for key in heading_keywords):
                capture = True
                continue
            elif capture:
                break
        elif capture and stripped.startswith("-"):
            collected.append(stripped)
    return collected


def _tokenize(text: str) -> list[str]:
    return text.split()


def build_summary() -> str:
    ethics = ETHICS_PATH.read_text(encoding="utf-8")
    threat = THREAT_PATH.read_text(encoding="utf-8")

    refuse = _extract_bullets(ethics, ["must always refuse"])
    flag = _extract_bullets(ethics, ["must always flag"])
    escalate_ethics = _extract_bullets(ethics, ["must always escalate"])
    escalate_threat = _extract_bullets(threat, ["escalation thresholds"])

    rule_section = []
    if refuse:
        rule_section.append("## MUST REFUSE")
        rule_section.extend(refuse)
    if flag:
        rule_section.append("\n## MUST FLAG")
        rule_section.extend(flag)
    escalate = escalate_ethics + escalate_threat
    if escalate:
        rule_section.append("\n## ESCALATE")
        rule_section.extend(escalate)

    rules_text = "\n".join(rule_section)
    rules_tokens = _tokenize(rules_text)

    base_text_tokens = _tokenize(ethics + "\n" + threat)
    remaining = MAX_TOKENS - len(rules_tokens)
    truncated = " ".join(base_text_tokens[:max(0, remaining)])
    truncated = shorten(truncated, width=len(truncated), placeholder="")

    summary = truncated + "\n\n" + rules_text
    return summary.strip()


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    summary = build_summary()
    tokens = _tokenize(summary)
    if len(tokens) > MAX_TOKENS:
        summary = " ".join(tokens[:MAX_TOKENS])
    OUTPUT_FILE.write_text(summary, encoding="utf-8")
    print(str(OUTPUT_FILE))


if __name__ == "__main__":
    main()
