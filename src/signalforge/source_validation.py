#!/usr/bin/env python3
"""
****************************************************************************************
                           SIGNALFORGE / ATMOS 2026
                   STUDENT IMPLEMENTATION BOILERPLATE
****************************************************************************************
FILE: src/signalforge/source_validation.py
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


def verify_document_identity(artifact: dict[str, Any], company: dict[str, Any]) -> dict[str, Any]:
    """
    TASK: T12     OWNER: B     STUDY FIRST: B01

    DESCRIPTION:
        Verify the downloaded document belongs to the requested listed issuer

    HOW TO FILL THIS PLACEHOLDER:
        Inspect readable issuer name, official identifiers, document type and period; do not infer authenticity from PDF header/hash alone.

    EXPECTED RESULT / VALIDATION:
        Wrong-company filing cannot receive the requested issuer ID.

    PROGRESSIVE HINTS (ask for help one level at a time):
        H1: Explain what success means before coding.
        H2: Split into inputs, decisions, side effects, and outputs.
        H3: Decide what can be checked deterministically.
        H4: Consult the written + video resources in LESSONS_AND_TASKS.md.
        H5: Follow the task-specific build/validation rules above.
        H6: For a precise algorithmic walkthrough without code, ask the mentor.
        H7: USE THESE EXACT TOOLS/METHODS: `source_validation.verify_document_identity()`, verified issuer metadata, PDF cover/title and report-period extraction, domain/origin class; return `verified/ambiguous/rejected` and never rely only on filename.
        H8: GIVE UP — explicitly ask the mentor for complete reference code and tests for this function only. Review before adopting.
    """
    ######################## ADD YOUR CODE HERE ########################
    # TODO T12: implement this function personally, then write/enable its tests.
    raise NotImplementedError("T12: verify_document_identity has not been implemented")
    ####################################################################
