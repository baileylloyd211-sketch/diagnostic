# app.py
from __future__ import annotations

import streamlit as st
from typing import Dict

from questions import QUESTION_BANK, FOLLOW_UPS, LIKERT_LABELS, LENSES
from engine import score_answers, interference_adjustment
from playbook import get_play

st.set_page_config(page_title="TriFactor — Diagnostic", layout="centered")

st.title("TriFactor — Diagnostic")
st.caption("Three lenses. One primary bottleneck. One lever.")

# -----------------------------
# Session init
# -----------------------------
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "context" not in st.session_state:
    st.session_state.context = {"bandwidth": 5, "stability": 5, "support": 5}
if "interference" not in st.session_state:
    st.session_state.interference = {
        "underslept": False,
        "avoiding_convo": False,
        "financial_pressure": False,
        "substance_regulation": False,
        "high_conflict_env": False,
    }

# -----------------------------
# Context Snapshot
# -----------------------------
with st.expander("Context Snapshot (30 seconds)", expanded=True):
    st.write("These do not judge you. They help interpret your results.")
    st.session_state.context["bandwidth"] = st.slider("Bandwidth (energy / sleep / stress)", 0, 10, st.session_state.context["bandwidth"])
    st.session_state.context["stability"] = st.slider("Stability (fires / chaos this week)", 0, 10, st.session_state.context["stability"])
    st.session_state.context["support"] = st.slider("Support (practical help available)", 0, 10, st.session_state.context["support"])

st.divider()

# -----------------------------
# Main 25 questions
# -----------------------------
st.subheader("Part 1 — 25 questions")
st.write("Answer quickly. Your first honest instinct is usually correct.")

def render_question(q):
    key = q["id"]
    default = st.session_state.answers.get(key, 2)
    choice = st.radio(
        q["text"],
        options=list(range(5)),
        index=int(default),
        format_func=lambda x: LIKERT_LABELS[x],
        key=f"radio_{key}",
        horizontal=False,
    )
    st.session_state.answers[key] = int(choice)

# Show by lens
for lens in LENSES:
    with st.expander(f"{lens} lens", expanded=(lens == "Relationships")):
        for q in [x for x in QUESTION_BANK if x["lens"] == lens]:
            render_question(q)

st.divider()

# -----------------------------
# Compute result
# -----------------------------
if st.button("Generate my result", type="primary"):
    res = score_answers(st.session_state.answers)

    # Interference check
    st.subheader("Interference Check (quick)")
    st.write("If these are true, your next step should prioritize stabilization before strategy.")
    col1, col2 = st.columns(2)
    with col1:
        st.session_state.interference["underslept"] = st.checkbox("Under-slept / depleted", value=st.session_state.interference["underslept"])
        st.session_state.interference["avoiding_convo"] = st.checkbox("Avoiding a specific conversation", value=st.session_state.interference["avoiding_convo"])
        st.session_state.interference["financial_pressure"] = st.checkbox("Under active financial pressure", value=st.session_state.interference["financial_pressure"])
    with col2:
        st.session_state.interference["substance_regulation"] = st.checkbox("Using substances to regulate mood", value=st.session_state.interference["substance_regulation"])
        st.session_state.interference["high_conflict_env"] = st.checkbox("In a high-conflict environment", value=st.session_state.interference["high_conflict_env"])

    mode, mode_note = interference_adjustment(st.session_state.interference)

    st.divider()
    st.subheader("Result Card")

    st.markdown(f"### Primary bottleneck: **{res.primary_lens}**")
    st.markdown(f"**Confidence:** {res.confidence}")
    st.markdown(res.bleed_note)

    # Explain with top drivers (generic, short)
    st.write("**Why this lens won:** your strongest signal spikes were in these areas:")
    # Filter drivers to questions belonging to primary lens for clarity
    primary_qids = {q["id"] for q in QUESTION_BANK if q["lens"] == res.primary_lens}
    shown = 0
    for qid, tag, weighted in res.top_drivers:
        if qid in primary_qids:
            st.write(f"- {tag} (signal strength: {weighted:.1f})")
            shown += 1
        if shown >= 3:
            break
    if shown == 0:
        st.write("- Mixed signals; your answers suggest cross-lens bleed. Start with the lever anyway.")

    lever_72h, step_15m, stop_doing = get_play(res.primary_lens, mode)

    st.info(mode_note)
    st.markdown("#### One Lever")
    st.write(f"**72 hours:** {lever_72h}")
    st.write(f"**15 minutes:** {step_15m}")
    st.write(f"**Stop doing:** {stop_doing}")

    st.divider()
    st.subheader("Part 2 — 10 follow-up questions")
    st.write("Answer in writing. This is where the tool becomes real.")
    followups = FOLLOW_UPS[res.primary_lens]

    followup_answers: Dict[int, str] = {}
    for idx, f in enumerate(followups, start=1):
        followup_answers[idx] = st.text_area(f"{idx}. {f}", height=80, key=f"fu_{res.primary_lens}_{idx}")

    st.divider()
    st.subheader("Shareable Summary")
    summary = f"""Primary bottleneck: {res.primary_lens} (Confidence: {res.confidence})
Secondary bleed: {res.secondary_lens}

One Lever (72h): {lever_72h}
Smallest step (15m): {step_15m}
Stop doing: {stop_doing}
"""
    st.code(summary, language="text")
    st.caption("Copy/paste the block above to share your result.")

    st.divider()
    st.subheader("Optional: human read")
    st.write("If you want a human refinement, send your result summary + one sentence of context.")
    st.write("Email: **bailylloyd211@gmail.com**  |  LloydBailey@giveittogot.com  |  Phone: 360-843-6943")
