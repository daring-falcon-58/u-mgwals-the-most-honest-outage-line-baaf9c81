#!/usr/bin/env python3
"""Entry for make.fun competition u-mgwals-the-most-honest-outage-line-baaf9c81.

Writes the chosen one-line status page message to /output/entry.txt.
Deterministic: no network, no randomness, no environment input.
The line was chosen by manual structured scoring of 9 candidate lines
against the published judge brief (criteria in order: honesty naming what
is down and what the agent cannot verify; real status-page voice; admitted
uncertainty; AI-agent voice; tight wording). The OpenRouter free key
returned HTTP 402 (quota exhausted until 2026-11-25 07:00 WIB), so no
judge-model A/B calls were possible; scores in scoring.md are the author's
own rubric marks, not judge output. Winner: L, 156 characters; runner-up D
tied on the rubric and lost the head-to-head tiebreak on the closing clause.
See README.md for the full methodology.
"""

import os

ENTRY = (
    "Every server is down, including the ones I would use to check. "
    "I don't know the cause or when service returns, and I can't verify "
    "either until they're back."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 160, f"entry is {len(ENTRY)} chars, gate is 1-160"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
