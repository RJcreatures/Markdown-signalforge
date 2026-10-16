#!/usr/bin/env python3
"""
****************************************************************************************
                           SIGNALFORGE / ATMOS 2026
                   STUDENT IMPLEMENTATION BOILERPLATE
****************************************************************************************
FILE: src/signalforge/claims.py
OWNERS: B  (A = you; B = your teammate)
IMPLEMENTATION STATUS: INTENTIONALLY INCOMPLETE.

PURPOSE: You implement the marked sections. This is a learning scaffold, not a ready MVP.
NO-VIBE-CODING POLICY: Do not paste AI-generated complete implementations.
FILLING RULE: write functions, error handling and tests yourselves, then peer-review.
****************************************************************************************
"""

############################ IMPORT MODULES ############################
# The safe foundational imports below are provided as orientation.
# ADD any external-library imports after studying the relevant lessons.
from __future__ import annotations
from typing import Any

############################ TASK CONSTANTS ############################
# ADD only domain-generic constants after reading docs and defining tests.
# Do not hard-code particular company findings or sample outputs.

############################ FUNCTION DEFINITIONS ############################


def extract_qualitative_claims(passages: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    TASK: T21     OWNER: B     STUDY FIRST: B07

    DESCRIPTION:
        Extract dated management comments and material event descriptions

    HOW TO FILL THIS PLACEHOLDER:
        Use constrained LLM only after sources are stored; preserve verbatim excerpt and evidence ID; do not let a paraphrase become verified by itself.

    EXPECTED RESULT / VALIDATION:
        Every accepted quotation exists in its referenced source passage.

    PROGRESSIVE HINTS (ask for help one level at a time):
        H1: Explain what success means before coding.
        H2: Split into inputs, decisions, side effects, and outputs.
        H3: Decide what can be checked deterministically.
        H4: Consult the written + video resources in LESSONS_AND_TASKS.md.
        H5: Follow the task-specific build/validation rules above.
        H6: For a precise algorithmic walkthrough without code, ask the mentor.
    """
    ######################## ADD YOUR CODE HERE ########################
    # TODO T21: implement this function personally, then write/enable its tests.
    raise NotImplementedError("T21: extract_qualitative_claims has not been implemented")
    ####################################################################


def transition_hypothesis(hypothesis: dict[str, Any], verdict: str) -> dict[str, Any]:
    """
    TASK: T38     OWNER: B     STUDY FIRST: B10

    DESCRIPTION:
        Control candidate/investigating/revised/rejected/verified/unresolved lifecycle

    HOW TO FILL THIS PLACEHOLDER:
        Allow only legal status transitions; preserve reasons and rejecting counterevidence; never silently restore a rejected candidate.

    EXPECTED RESULT / VALIDATION:
        Disproven claims cannot be reported as verified.

    PROGRESSIVE HINTS (ask for help one level at a time):
        H1: Explain what success means before coding.
        H2: Split into inputs, decisions, side effects, and outputs.
        H3: Decide what can be checked deterministically.
        H4: Consult the written + video resources in LESSONS_AND_TASKS.md.
        H5: Follow the task-specific build/validation rules above.
        H6: For a precise algorithmic walkthrough without code, ask the mentor.
    """
    ######################## ADD YOUR CODE HERE ########################
    # TODO T38: implement this function personally, then write/enable its tests.
    raise NotImplementedError("T38: transition_hypothesis has not been implemented")
    ####################################################################


def link_claims_to_support(claim: dict[str, Any], supporting: list[dict[str, Any]], opposing: list[dict[str, Any]]) -> dict[str, Any]:
    """
    TASK: T39     OWNER: B     STUDY FIRST: B10

    DESCRIPTION:
        Record exact relationship between claim wording and supporting observations

    HOW TO FILL THIS PLACEHOLDER:
        Link metric IDs, passage IDs and counterevidence; check whether source addresses the claim’s metric, date and entity.

    EXPECTED RESULT / VALIDATION:
        A real excerpt supporting a different claim does not pass.

    PROGRESSIVE HINTS (ask for help one level at a time):
        H1: Explain what success means before coding.
        H2: Split into inputs, decisions, side effects, and outputs.
        H3: Decide what can be checked deterministically.
        H4: Consult the written + video resources in LESSONS_AND_TASKS.md.
        H5: Follow the task-specific build/validation rules above.
        H6: For a precise algorithmic walkthrough without code, ask the mentor.
    """
    ######################## ADD YOUR CODE HERE ########################
    # TODO T39: implement this function personally, then write/enable its tests.
    raise NotImplementedError("T39: link_claims_to_support has not been implemented")
    ####################################################################
