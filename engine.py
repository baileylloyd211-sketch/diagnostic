# engine.py
from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List, Tuple
from collections import defaultdict

from questions import QUESTION_BANK, LENSES

@dataclass
class ScoreResult:
    lens_scores: Dict[str, float]
    primary_lens: str
    secondary_lens: str
    confidence: str
    top_drivers: List[Tuple[str, str, float]]  # (qid, tag, weighted_value)
    bleed_note: str

def _confidence_from_gap(primary: float, secondary: float, answered_ratio: float) -> str:
    gap = primary - secondary
    if answered_ratio < 0.85:
        return "Low"
    if gap >= 6:
        return "High"
    if gap >= 3:
        return "Medium"
    return "Low"

def score_answers(answers: Dict[str, int]) -> ScoreResult:
    lens_scores = defaultdict(float)
    drivers = []  # (qid, tag, weighted_value)

    answered = 0
    total = len(QUESTION_BANK)

    for q in QUESTION_BANK:
        qid = q["id"]
        if qid not in answers:
            continue
        answered += 1
        val = int(answers[qid])
        weighted = val * float(q.get("weight", 1.0))
        lens_scores[q["lens"]] += weighted
        drivers.append((qid, q.get("tag", ""), weighted))

    # Ensure all lenses exist
    for L in LENSES:
        lens_scores[L] = float(lens_scores.get(L, 0.0))

    sorted_lenses = sorted(lens_scores.items(), key=lambda x: x[1], reverse=True)
    primary_lens, primary_score = sorted_lenses[0]
    secondary_lens, secondary_score = sorted_lenses[1]

    answered_ratio = answered / max(total, 1)
    confidence = _confidence_from_gap(primary_score, secondary_score, answered_ratio)

    # Top 4 highest weighted drivers overall, but we’ll explain only those belonging to primary lens later.
    drivers_sorted = sorted(drivers, key=lambda x: x[2], reverse=True)[:6]

    # Bleed note
    bleed_note = ""
    if secondary_score > 0 and (primary_score - secondary_score) < 3:
        bleed_note = f"Close secondary influence detected: **{secondary_lens}** is almost tied with **{primary_lens}**."
    else:
        bleed_note = f"Secondary bleed: **{secondary_lens}** (shows up as background friction)."

    return ScoreResult(
        lens_scores=dict(lens_scores),
        primary_lens=primary_lens,
        secondary_lens=secondary_lens,
        confidence=confidence,
        top_drivers=drivers_sorted,
        bleed_note=bleed_note,
    )

def interference_adjustment(interference: Dict[str, bool]) -> Tuple[str, str]:
    """
    Returns (mode, note)
    mode: "stabilize" if interference is high, else "execute"
    """
    hits = sum(1 for v in interference.values() if v)
    if hits >= 3:
        return ("stabilize", "High interference detected. Your next step should prioritize stabilization before strategy.")
    if hits == 2:
        return ("stabilize", "Moderate interference detected. Stabilize first, then execute the lever.")
    return ("execute", "Interference looks manageable. Execute the lever directly.")
