# questions.py
from __future__ import annotations

LENSES = ["Relationships", "Finance", "Big Picture"]

# Each question is rated 0-4:
# 0 = Not at all / Never
# 1 = Rarely
# 2 = Sometimes
# 3 = Often
# 4 = Almost always
#
# "weight" lets you make certain questions count more.
# "tag" is used for explanations in the result.

QUESTION_BANK = [
    # -------------------------
    # Relationships (9)
    # -------------------------
    {"id": "rel_01", "lens": "Relationships", "text": "I delay addressing a known issue with someone for more than 7 days.", "weight": 1.1, "tag": "avoidance"},
    {"id": "rel_02", "lens": "Relationships", "text": "I rehearse conversations in my head but don’t actually have them.", "weight": 1.0, "tag": "avoidance"},
    {"id": "rel_03", "lens": "Relationships", "text": "I soften or dilute what I want to say to avoid discomfort.", "weight": 1.0, "tag": "conflict_avoidance"},
    {"id": "rel_04", "lens": "Relationships", "text": "I agree to things that cost me energy or time I don’t have.", "weight": 1.1, "tag": "boundaries"},
    {"id": "rel_05", "lens": "Relationships", "text": "I feel responsible for regulating other people’s emotions.", "weight": 1.0, "tag": "emotional_load"},
    {"id": "rel_06", "lens": "Relationships", "text": "I notice resentment building before I say anything.", "weight": 1.1, "tag": "resentment"},
    {"id": "rel_07", "lens": "Relationships", "text": "I tolerate behavior I would advise someone else not to tolerate.", "weight": 1.1, "tag": "self_violation"},
    {"id": "rel_08", "lens": "Relationships", "text": "I avoid setting limits because I fear escalation or withdrawal.", "weight": 1.0, "tag": "boundary_fear"},
    {"id": "rel_09", "lens": "Relationships", "text": "I replay interactions afterward wishing I had said something differently.", "weight": 1.0, "tag": "rumination"},
    {"id": "rel_10", "lens": "Relationships", "text": "I feel drained after interactions that are supposed to be supportive.", "weight": 1.1, "tag": "energy_drain"},
    {"id": "rel_11", "lens": "Relationships", "text": "I carry more relational responsibility than feels fair.", "weight": 1.0, "tag": "imbalance"},
    {"id": "rel_12", "lens": "Relationships", "text": "I avoid asking directly for what I need.", "weight": 1.0, "tag": "needs"},
    {"id": "rel_13", "lens": "Relationships", "text": "I stay in conversations after they stop being productive or respectful.", "weight": 1.0, "tag": "overexposure"},
    {"id": "rel_14", "lens": "Relationships", "text": "I feel unclear about where I stand with at least one important person.", "weight": 1.0, "tag": "ambiguity"},
    {"id": "rel_15", "lens": "Relationships", "text": "I prioritize keeping peace over being accurate.", "weight": 1.1, "tag": "appeasement"},
    {"id": "rel_16", "lens": "Relationships", "text": "I feel unseen in relationships that matter to me.", "weight": 1.0, "tag": "invisibility"},
    {"id": "rel_17", "lens": "Relationships", "text": "When conflict arises, it tends to linger unresolved.", "weight": 1.1, "tag": "repair_failure"},
    # -------------------------
    # Finance (8)
    # -------------------------
    {"id": "fin_01", "lens": "Finance", "text": "I avoid checking my account balances regularly.", "weight": 1.1, "tag": "avoidance"},
    {"id": "fin_02", "lens": "Finance", "text": "One unexpected expense would meaningfully destabilize me.", "weight": 1.1, "tag": "fragility"},
    {"id": "fin_03", "lens": "Finance", "text": "I delay paperwork, applications, or financial admin that I know matters.", "weight": 1.0, "tag": "admin_delay"},
    {"id": "fin_04", "lens": "Finance", "text": "I don’t have a simple, repeatable weekly money plan.", "weight": 1.0, "tag": "structure"},
    {"id": "fin_05", "lens": "Finance", "text": "My income feels unpredictable month to month.", "weight": 1.1, "tag": "volatility"},
    {"id": "fin_06", "lens": "Finance", "text": "I use spending to relieve stress, boredom, or emotional pressure.", "weight": 1.0, "tag": "emotional_spending"},
    {"id": "fin_07", "lens": "Finance", "text": "I make short-term money decisions that create longer-term stress.", "weight": 1.1, "tag": "short_termism"},
    {"id": "fin_08", "lens": "Finance", "text": "I feel behind on financial tasks even when nothing is actively on fire.", "weight": 1.0, "tag": "backlog"},
    {"id": "fin_09", "lens": "Finance", "text": "I postpone dealing with a known financial issue.", "weight": 1.1, "tag": "avoidance"},
    {"id": "fin_10", "lens": "Finance", "text": "I lack a clear picture of my fixed monthly obligations.", "weight": 1.0, "tag": "clarity"},
    {"id": "fin_11", "lens": "Finance", "text": "I avoid asking for financial help or clarity even when appropriate.", "weight": 1.0, "tag": "support_avoidance"},
    {"id": "fin_12", "lens": "Finance", "text": "I rely on 'it’ll work out' more than on a concrete plan.", "weight": 1.1, "tag": "wishful_thinking"},
    {"id": "fin_13", "lens": "Finance", "text": "I feel stuck between survival income and meaningful work.", "weight": 1.0, "tag": "income_split"},
    {"id": "fin_14", "lens": "Finance", "text": "I feel constant low-grade anxiety about money.", "weight": 1.0, "tag": "chronic_stress"},
    {"id": "fin_15", "lens": "Finance", "text": "I take on financial commitments without fully checking capacity.", "weight": 1.1, "tag": "overcommitment"},
    {"id": "fin_16", "lens": "Finance", "text": "I feel unclear about my fastest path to more stability.", "weight": 1.0, "tag": "path_unclear"},
    {"id": "fin_17", "lens": "Finance", "text": "Money issues regularly consume mental bandwidth.", "weight": 1.1, "tag": "cognitive_load"},
    # -------------------------
    # Big Picture (8)
    # -------------------------
    {"id": "big_01", "lens": "Big Picture", "text": "I have multiple active projects competing for my attention.", "weight": 1.0, "tag": "overcommitment"},
    {"id": "big_02", "lens": "Big Picture", "text": "I struggle to finish what I start.", "weight": 1.1, "tag": "completion"},
    {"id": "big_03", "lens": "Big Picture", "text": "I spend more time explaining ideas than demonstrating them.", "weight": 1.0, "tag": "overexplaining"},
    {"id": "big_04", "lens": "Big Picture", "text": "I can’t clearly state my next concrete step.", "weight": 1.0, "tag": "next_step"},
    {"id": "big_05", "lens": "Big Picture", "text": "I feel urgency that isn’t matched by visible progress.", "weight": 1.1, "tag": "urgency_gap"},
    {"id": "big_06", "lens": "Big Picture", "text": "I keep expanding scope instead of shipping something small.", "weight": 1.1, "tag": "scope_creep"},
    {"id": "big_07", "lens": "Big Picture", "text": "I delay sharing work until it feels fully formed.", "weight": 1.0, "tag": "perfectionism"},
    {"id": "big_08", "lens": "Big Picture", "text": "I feel under-resourced relative to what I’m trying to do.", "weight": 1.0, "tag": "runway"},
    {"id": "big_09", "lens": "Big Picture", "text": "I don’t have a single measurable win I’m pursuing right now.", "weight": 1.0, "tag": "metrics"},
    {"id": "big_10", "lens": "Big Picture", "text": "I jump between ideas when things get hard or slow.", "weight": 1.0, "tag": "idea_hopping"},
    {"id": "big_11", "lens": "Big Picture", "text": "I feel ahead conceptually but behind materially.", "weight": 1.1, "tag": "execution_gap"},
    {"id": "big_12", "lens": "Big Picture", "text": "I wait for permission, buy-in, or understanding before acting.", "weight": 1.0, "tag": "permission_waiting"},
    {"id": "big_13", "lens": "Big Picture", "text": "I don’t have a tight feedback loop for what I’m building.", "weight": 1.0, "tag": "feedback"},
    {"id": "big_14", "lens": "Big Picture", "text": "I spend time on things that don’t create traction.", "weight": 1.1, "tag": "low_leverage"},
    {"id": "big_15", "lens": "Big Picture", "text": "I feel disconnected from a clear 30-day objective.", "weight": 1.0, "tag": "short_horizon"},
    {"id": "big_16", "lens": "Big Picture", "text": "I know what matters most but act inconsistently with it.", "weight": 1.1, "tag": "misalignment"},

# The 10 follow-ups are chosen by the winning lens,
# but phrased to turn insight into commitment.
FOLLOW_UPS = {
    "Relationships": [
        "What conversation are you avoiding that would change everything if it happened calmly?",
        "What boundary do you keep failing to enforce because you fear the reaction?",
        "Where do you over-explain instead of making a clean request?",
        "What pattern repeats: escalation, withdrawal, or silent resentment?",
        "What do you keep tolerating that’s training others how to treat you?",
        "If nothing changes, what gets worse in 90 days?",
        "What is the smallest relationship repair you can attempt in 72 hours?",
        "Who drains you most, and what is the mechanism of that drain?",
        "What does 'respect' look like behaviorally in your closest relationship?",
        "What is one sentence you can say this week that you’ve been scared to say?",
    ],
    "Finance": [
        "What number are you avoiding looking at (cash, debt, bills, income)?",
        "What is your single biggest money leak (habit, subscription, impulse, helping others)?",
        "What is the simplest weekly money plan you could actually follow?",
        "What paperwork/admin task, if completed, would reduce stress fastest?",
        "What income action could you do in 72 hours that has the highest odds of paying off?",
        "What do you buy to regulate emotion, and what triggers it?",
        "Where are you choosing short-term relief that causes long-term pain?",
        "If nothing changes, what breaks first in 90 days?",
        "What is one rule you can adopt immediately (caps, no-spend window, auto-transfer)?",
        "Who could help (practically) if you asked clearly, and what exactly would you ask for?",
    ],
    "Big Picture": [
        "What are you trying to do that is too big for your current runway?",
        "What’s the smallest shippable proof you could build in 72 hours?",
        "What do you keep explaining that should be demonstrated instead?",
        "What would you finish if you only allowed one active project for 30 days?",
        "Where does your attention go that produces zero traction?",
        "What is your single most valuable constraint right now (money, time, energy, support)?",
        "If nothing changes, what gets worse in 90 days?",
        "What is the one lever that would reduce struggle this month?",
        "What is one thing you can publish that requires no permission and proves competence?",
        "What would you do if you stopped trying to convince anyone for 14 days?",
    ],
}

LIKERT_LABELS = [
    "0 — Not at all / Never",
    "1 — Rarely",
    "2 — Sometimes",
    "3 — Often",
    "4 — Almost always",
]
