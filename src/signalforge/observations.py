#!/usr/bin/env python3
"""
****************************************************************************************
                           SIGNALFORGE / ATMOS 2026
                   STUDENT IMPLEMENTATION BOILERPLATE
****************************************************************************************
FILE: src/signalforge/observations.py
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


def extract_numeric_observation(passages: list[dict[str, Any]], metric_definition: dict[str, Any]) -> dict[str, Any]:
    """
    TASK: T18     OWNER: A     STUDY FIRST: A06

    DESCRIPTION:
        Extract one labeled financial value from an official document

    HOW TO FILL THIS PLACEHOLDER:
        Identify row label, column heading, value, original units, period, segment, accounting basis and exact passage.

    EXPECTED RESULT / VALIDATION:
        Right number in wrong row/column is rejected.

    PROGRESSIVE HINTS (ask for help one level at a time):
        H1: Explain what success means before coding.
        H2: Split into inputs, decisions, side effects, and outputs.
        H3: Decide what can be checked deterministically.
        H4: Consult the written + video resources in LESSONS_AND_TASKS.md.
        H5: Follow the task-specific build/validation rules above.
        H6: For a precise algorithmic walkthrough without code, ask the mentor.
    """
    ######################## ADD YOUR CODE HERE ########################
    # TODO T18: implement this function personally, then write/enable its tests.
    raise NotImplementedError("T18: extract_numeric_observation has not been implemented")
    ####################################################################


def normalize_observation(observation: dict[str, Any]) -> dict[str, Any]:
    """
    TASK: T20     OWNER: A     STUDY FIRST: A06

    DESCRIPTION:
        Convert units and prepare comparable time labels without inventing data

    HOW TO FILL THIS PLACEHOLDER:
        Normalize INR lakh/million/crore with explicit scale; preserve original; distinguish period length and balance versus flow.

    EXPECTED RESULT / VALIDATION:
        Wrong-scale/15-month-mismatch evidence cannot become a validated growth input.

    PROGRESSIVE HINTS (ask for help one level at a time):
        H1: Explain what success means before coding.
        H2: Split into inputs, decisions, side effects, and outputs.
        H3: Decide what can be checked deterministically.
        H4: Consult the written + video resources in LESSONS_AND_TASKS.md.
        H5: Follow the task-specific build/validation rules above.
        H6: For a precise algorithmic walkthrough without code, ask the mentor.
    """
    ######################## ADD YOUR CODE HERE ########################
    # TODO T20: implement this function personally, then write/enable its tests.
    raise NotImplementedError("T20: normalize_observation has not been implemented")
    ####################################################################
