#!/usr/bin/env python3
"""
****************************************************************************************
                           SIGNALFORGE / ATMOS 2026
                   STUDENT IMPLEMENTATION BOILERPLATE
****************************************************************************************
FILE: src/signalforge/investigation.py
OWNERS: A / B  (A = you; B = your teammate)
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


def search_supporting_evidence(hypothesis: dict[str, Any], budget: dict[str, Any]) -> list[dict[str, Any]]:
    """
    TASK: T34     OWNER: A     STUDY FIRST: A08

    DESCRIPTION:
        Retrieve corroborating passages and identify missing required observations

    HOW TO FILL THIS PLACEHOLDER:
        Use local retrieval first, approved public search if needed, preserve query log; no invented citation.

    EXPECTED RESULT / VALIDATION:
        Supports each evidence link with stored document, page and excerpt.

    PROGRESSIVE HINTS (ask for help one level at a time):
        H1: Explain what success means before coding.
        H2: Split into inputs, decisions, side effects, and outputs.
        H3: Decide what can be checked deterministically.
        H4: Consult the written + video resources in LESSONS_AND_TASKS.md.
        H5: Follow the task-specific build/validation rules above.
        H6: For a precise algorithmic walkthrough without code, ask the mentor.
        H7: USE THESE EXACT TOOLS/METHODS: `investigation.search_supporting_evidence()`, `retrieval.retrieve_evidence()`, accounting synonym bank, follow-up FTS5 queries and dated source filters; log no-result searches.
        H8: GIVE UP — explicitly ask the mentor for complete reference code and tests for this function only. Review before adopting.
    """
    ######################## ADD YOUR CODE HERE ########################
    # TODO T34: implement this function personally, then write/enable its tests.
    raise NotImplementedError("T34: search_supporting_evidence has not been implemented")
    ####################################################################


def search_opposing_evidence(hypothesis: dict[str, Any], budget: dict[str, Any]) -> list[dict[str, Any]]:
    """
    TASK: T35     OWNER: B     STUDY FIRST: B10

    DESCRIPTION:
        Search for counterarguments, alternatives, and factual contradictions

    HOW TO FILL THIS PLACEHOLDER:
        Investigate acquisition, sector-wide trends, seasonality, changed definitions, restatements and contrary management text.

    EXPECTED RESULT / VALIDATION:
        A credible contrary source weakens or rejects the original interpretation.

    PROGRESSIVE HINTS (ask for help one level at a time):
        H1: Explain what success means before coding.
        H2: Split into inputs, decisions, side effects, and outputs.
        H3: Decide what can be checked deterministically.
        H4: Consult the written + video resources in LESSONS_AND_TASKS.md.
        H5: Follow the task-specific build/validation rules above.
        H6: For a precise algorithmic walkthrough without code, ask the mentor.
        H7: USE THESE EXACT TOOLS/METHODS: `investigation.search_opposing_evidence()`, FTS5 queries for restatement/acquisition/seasonality/peer trends, structured counterevidence IDs, recorded search coverage; require substantive contradictions rather than model self-critique.
        H8: GIVE UP — explicitly ask the mentor for complete reference code and tests for this function only. Review before adopting.
    """
    ######################## ADD YOUR CODE HERE ########################
    # TODO T35: implement this function personally, then write/enable its tests.
    raise NotImplementedError("T35: search_opposing_evidence has not been implemented")
    ####################################################################


def check_corporate_event_confounders(company: dict[str, Any], period: dict[str, Any]) -> list[dict[str, Any]]:
    """
    TASK: T41     OWNER: A     STUDY FIRST: A08

    DESCRIPTION:
        Check whether major corporate events distort financial comparisons

    HOW TO FILL THIS PLACEHOLDER:
        Search evidenced acquisition, demerger, discontinued operations, accounting changes; record unresolved checks.

    EXPECTED RESULT / VALIDATION:
        Growth claim is not asserted organic if an acquisition may explain it.

    PROGRESSIVE HINTS (ask for help one level at a time):
        H1: Explain what success means before coding.
        H2: Split into inputs, decisions, side effects, and outputs.
        H3: Decide what can be checked deterministically.
        H4: Consult the written + video resources in LESSONS_AND_TASKS.md.
        H5: Follow the task-specific build/validation rules above.
        H6: For a precise algorithmic walkthrough without code, ask the mentor.
        H7: USE THESE EXACT TOOLS/METHODS: `investigation.check_corporate_event_confounders()`, stored source passages + FTS5 searches for `acquisition`, `demerger`, `restatement`, `scheme of arrangement`, timeline validation; unresolved material events restrict conclusions.
        H8: GIVE UP — explicitly ask the mentor for complete reference code and tests for this function only. Review before adopting.
    """
    ######################## ADD YOUR CODE HERE ########################
    # TODO T41: implement this function personally, then write/enable its tests.
    raise NotImplementedError("T41: check_corporate_event_confounders has not been implemented")
    ####################################################################
