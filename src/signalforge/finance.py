#!/usr/bin/env python3
"""
****************************************************************************************
                           SIGNALFORGE / ATMOS 2026
                   STUDENT IMPLEMENTATION BOILERPLATE
****************************************************************************************
FILE: src/signalforge/finance.py
OWNERS: A  (A = you; B = your teammate)
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


def compute_comparable_growth(previous: dict[str, Any], current: dict[str, Any]) -> dict[str, Any]:
    """
    TASK: T26     OWNER: A     STUDY FIRST: A07

    DESCRIPTION:
        Calculate change for two financially comparable revenue observations

    HOW TO FILL THIS PLACEHOLDER:
        Guard same metric definition, scope, segment, currency and matching period duration; handle division by zero.

    EXPECTED RESULT / VALIDATION:
        An incompatible 15-month/12-month comparison is rejected.

    PROGRESSIVE HINTS (ask for help one level at a time):
        H1: Explain what success means before coding.
        H2: Split into inputs, decisions, side effects, and outputs.
        H3: Decide what can be checked deterministically.
        H4: Consult the written + video resources in LESSONS_AND_TASKS.md.
        H5: Follow the task-specific build/validation rules above.
        H6: For a precise algorithmic walkthrough without code, ask the mentor.
    """
    ######################## ADD YOUR CODE HERE ########################
    # TODO T26: implement this function personally, then write/enable its tests.
    raise NotImplementedError("T26: compute_comparable_growth has not been implemented")
    ####################################################################


def compute_receivable_days_proxy(receivables: dict[str, Any], revenue: dict[str, Any], period_days: int) -> dict[str, Any]:
    """
    TASK: T27     OWNER: A     STUDY FIRST: A07

    DESCRIPTION:
        Compute clearly labeled approximate receivables days when inputs support it

    HOW TO FILL THIS PLACEHOLDER:
        Check point-in-time balance versus flow period; prefer average receivables where available; label proxy absent credit sales.

    EXPECTED RESULT / VALIDATION:
        No constant 365 on half-year flow; no claim of exact DSO if proxy.

    PROGRESSIVE HINTS (ask for help one level at a time):
        H1: Explain what success means before coding.
        H2: Split into inputs, decisions, side effects, and outputs.
        H3: Decide what can be checked deterministically.
        H4: Consult the written + video resources in LESSONS_AND_TASKS.md.
        H5: Follow the task-specific build/validation rules above.
        H6: For a precise algorithmic walkthrough without code, ask the mentor.
    """
    ######################## ADD YOUR CODE HERE ########################
    # TODO T27: implement this function personally, then write/enable its tests.
    raise NotImplementedError("T27: compute_receivable_days_proxy has not been implemented")
    ####################################################################


def screen_financial_anomalies(observations: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    TASK: T28     OWNER: A     STUDY FIRST: A07

    DESCRIPTION:
        Identify candidate numerical shifts without asserting a cause

    HOW TO FILL THIS PLACEHOLDER:
        Check meaningful change, missing-data flags and materiality; record input evidence; avoid tiny-peer Z scores.

    EXPECTED RESULT / VALIDATION:
        An anomaly is research lead, not published accusation.

    PROGRESSIVE HINTS (ask for help one level at a time):
        H1: Explain what success means before coding.
        H2: Split into inputs, decisions, side effects, and outputs.
        H3: Decide what can be checked deterministically.
        H4: Consult the written + video resources in LESSONS_AND_TASKS.md.
        H5: Follow the task-specific build/validation rules above.
        H6: For a precise algorithmic walkthrough without code, ask the mentor.
    """
    ######################## ADD YOUR CODE HERE ########################
    # TODO T28: implement this function personally, then write/enable its tests.
    raise NotImplementedError("T28: screen_financial_anomalies has not been implemented")
    ####################################################################


def compare_peer_directions(target: dict[str, Any], peers: list[dict[str, Any]]) -> dict[str, Any]:
    """
    TASK: T42     OWNER: A     STUDY FIRST: A07

    DESCRIPTION:
        Assess compatible peer trends without unjustified statistical certainty

    HOW TO FILL THIS PLACEHOLDER:
        Validate metric definition and time period in each peer; show changes and alternative sector interpretation; mark unsupported comparisons.

    EXPECTED RESULT / VALIDATION:
        Missing or incomparable peers cannot falsely certify uniqueness.

    PROGRESSIVE HINTS (ask for help one level at a time):
        H1: Explain what success means before coding.
        H2: Split into inputs, decisions, side effects, and outputs.
        H3: Decide what can be checked deterministically.
        H4: Consult the written + video resources in LESSONS_AND_TASKS.md.
        H5: Follow the task-specific build/validation rules above.
        H6: For a precise algorithmic walkthrough without code, ask the mentor.
    """
    ######################## ADD YOUR CODE HERE ########################
    # TODO T42: implement this function personally, then write/enable its tests.
    raise NotImplementedError("T42: compare_peer_directions has not been implemented")
    ####################################################################
