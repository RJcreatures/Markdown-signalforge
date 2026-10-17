#!/usr/bin/env python3
"""
****************************************************************************************
                           SIGNALFORGE / ATMOS 2026
                   STUDENT IMPLEMENTATION BOILERPLATE
****************************************************************************************
FILE: src/signalforge/llm.py
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


def request_structured_reasoning(role: str, input_payload: dict[str, Any], settings: dict[str, Any]) -> dict[str, Any]:
    """
    TASK: T31     OWNER: B     STUDY FIRST: B07

    DESCRIPTION:
        Call exactly one configured LLM with bounded structured-output validation

    HOW TO FILL THIS PLACEHOLDER:
        Check model credentials at runtime; use role prompts from prompts/; bound calls/time; reject invalid or unsupported outputs.

    EXPECTED RESULT / VALIDATION:
        Malformed response or API refusal never turns into verified hypothesis.

    PROGRESSIVE HINTS (ask for help one level at a time):
        H1: Explain what success means before coding.
        H2: Split into inputs, decisions, side effects, and outputs.
        H3: Decide what can be checked deterministically.
        H4: Consult the written + video resources in LESSONS_AND_TASKS.md.
        H5: Follow the task-specific build/validation rules above.
        H6: For a precise algorithmic walkthrough without code, ask the mentor.
        H7: USE THESE EXACT TOOLS/METHODS: `llm.request_structured_reasoning()`, one chosen provider SDK with JSON/schema mode when supported, Pydantic `model_validate`/`model_validate_json`, capped tokens/timeouts; reject malformed replies. Provider unspecified—check actual SDK API.
        H8: GIVE UP — explicitly ask the mentor for complete reference code and tests for this function only. Review before adopting.
    """
    ######################## ADD YOUR CODE HERE ########################
    # TODO T31: implement this function personally, then write/enable its tests.
    raise NotImplementedError("T31: request_structured_reasoning has not been implemented")
    ####################################################################
