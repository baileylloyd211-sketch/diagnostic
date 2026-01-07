# playbook.py
from __future__ import annotations
from typing import Dict, Tuple

# One-lever recommendations by lens + mode.
# Keep these concrete and 72-hour executable.

ONE_LEVER: Dict[str, Dict[str, Dict[str, str]]] = {
    "Relationships": {
        "execute": {
            "lever_72h": "Schedule one calm, bounded conversation (20 minutes) about ONE issue you keep avoiding.",
            "step_15m": "Write 3 bullet points: (1) what I observe, (2) what I need, (3) what I’m asking for.",
            "stop_doing": "Stop hinting. Stop hoping they’ll infer what you mean.",
        },
        "stabilize": {
            "lever_72h": "Reduce exposure: create one boundary that protects your energy this week.",
            "step_15m": "Decide one limit (time, topic, access) and write the exact sentence you’ll use.",
            "stop_doing": "Stop staying in conversations that become disrespectful or circular.",
        },
    },
    "Finance": {
        "execute": {
            "lever_72h": "Do a 15-minute money reality check and pick one immediate income action.",
            "step_15m": "Open accounts/bills and write down: cash on hand, next 2 bills, one income target.",
            "stop_doing": "Stop avoiding the numbers. Avoidance is a fee.",
        },
        "stabilize": {
            "lever_72h": "Cut one leak and create one buffer rule for the next 7 days.",
            "step_15m": "Cancel/pause one expense OR set a strict daily cap for 7 days.",
            "stop_doing": "Stop using spending as mood regulation (especially late-night).",
        },
    },
    "Big Picture": {
        "execute": {
            "lever_72h": "Ship one proof artifact that demonstrates value in under 60 seconds.",
            "step_15m": "Define the artifact’s format: one page, one screenshot, one demo link, one result card.",
            "stop_doing": "Stop explaining the full vision to uncommitted people.",
        },
        "stabilize": {
            "lever_72h": "Freeze scope: pick ONE active project for 7 days and ignore the rest.",
            "step_15m": "Write the single deliverable you will finish, and the single metric that proves done.",
            "stop_doing": "Stop starting new threads when you’re under-resourced.",
        },
    },
}

def get_play(lens: str, mode: str) -> Tuple[str, str, str]:
    pack = ONE_LEVER.get(lens, {}).get(mode, {})
    return (
        pack.get("lever_72h", "Pick one lever you can execute in 72 hours."),
        pack.get("step_15m", "Pick a 15-minute first step."),
        pack.get("stop_doing", "Stop doing the thing that keeps the loop alive."),
    )
