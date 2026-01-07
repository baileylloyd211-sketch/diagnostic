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
    {"id": "rel_01", "lens": "Relationships", "text": "I avoid important conversations until they explode.", "weight": 1.2, "tag": "avoidance"},
    {"id": "rel_02", "lens": "Relationships", "text": "I feel misunderstood more often than understood.", "weight": 1.1, "tag": "misattunement"},
    {"id": "rel_03", "lens": "Relationships", "text": "I say 'yes' when I mean 'no' to keep peace.", "weight": 1.2, "tag": "boundaries"},
    {"id": "rel_04", "lens": "Relationships", "text": "Small issues turn into big fights or cold distance.", "weight": 1.1, "tag": "escalation"},
    {"id": "rel_05", "lens": "Relationships", "text": "I feel like I carry the emotional load for others.", "weight": 1.0, "tag": "imbalance"},
    {"id": "rel_06", "lens": "Relationships", "text": "Trust feels thin (I second-guess motives / intentions).", "weight": 1.1, "tag": "trust"},
    {"id": "rel_07", "lens": "Relationships", "text": "I struggle to ask clearly for what I need.", "weight": 1.0, "tag": "needs"},
    {"id": "rel_08", "lens": "Relationships", "text": "I feel isolated even when I'm around people.", "weight": 1.0, "tag": "isolation"},
    {"id": "rel_09", "lens": "Relationships", "text": "My relationships drain more energy than they give back.", "weight": 1.2, "tag": "drain"},

    # -------------------------
    # Finance (8)
    # -------------------------
    {"id": "fin_01", "lens": "Finance", "text": "I avoid looking at my money situation directly.", "weight": 1.3, "tag": "avoidance"},
    {"id": "fin_02", "lens": "Finance", "text": "A single unexpected expense destabilizes me.", "weight": 1.2, "tag": "fragility"},
    {"id": "fin_03", "lens": "Finance", "text": "I don't have a simple weekly plan for income and bills.", "weight": 1.1, "tag": "structure"},
    {"id": "fin_04", "lens": "Finance", "text": "I overspend when I'm stressed, bored, or emotional.", "weight": 1.1, "tag": "impulse"},
    {"id": "fin_05", "lens": "Finance", "text": "My income feels unpredictable or too dependent on luck.", "weight": 1.2, "tag": "volatility"},
    {"id": "fin_06", "lens": "Finance", "text": "I procrastinate paperwork, applications, or admin tasks.", "weight": 1.0, "tag": "admin"},
    {"id": "fin_07", "lens": "Finance", "text": "I take on short-term fixes that create long-term stress.", "weight": 1.1, "tag": "tradeoffs"},
    {"id": "fin_08", "lens": "Finance", "text": "I feel stuck between survival work and meaningful work.", "weight": 1.1, "tag": "split"},

    # -------------------------
    # Big Picture (8)
    # -------------------------
    {"id": "big_01", "lens": "Big Picture", "text": "I have a lot of ideas but no clean next step.", "weight": 1.1, "tag": "diffusion"},
    {"id": "big_02", "lens": "Big Picture", "text": "I struggle to finish what I start.", "weight": 1.2, "tag": "completion"},
    {"id": "big_03", "lens": "Big Picture", "text": "I can’t get people to stay engaged long enough to understand.", "weight": 1.2, "tag": "attention"},
    {"id": "big_04", "lens": "Big Picture", "text": "I feel like I’m ahead of the curve but under-resourced.", "weight": 1.2, "tag": "runway"},
    {"id": "big_05", "lens": "Big Picture", "text": "The world feels unserious; accountability feels gone.", "weight": 1.0, "tag": "unserious"},
    {"id": "big_06", "lens": "Big Picture", "text": "I feel urgency, but progress doesn’t match the urgency.", "weight": 1.2, "tag": "speed"},
    {"id": "big_07", "lens": "Big Picture", "text": "I don’t trust institutions or narratives anymore.", "weight": 1.0, "tag": "trust"},
    {"id": "big_08", "lens": "Big Picture", "text": "I want traction more than I want validation.", "weight": 1.1, "tag": "traction"},
]

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
