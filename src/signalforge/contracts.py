#!/usr/bin/env python3
"""
****************************************************************************************
                           SIGNALFORGE / ATMOS 2026
                   STUDENT IMPLEMENTATION BOILERPLATE
****************************************************************************************
FILE: src/signalforge/contracts.py
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


def define_company_and_document_contracts() -> dict[str, type]:
    """
    TASK: T03     OWNER: B     STUDY FIRST: B01

    DESCRIPTION:
        Declare typed Company, Document, Passage, SourceOrigin and RetrievalStatus records

    HOW TO FILL THIS PLACEHOLDER:
        Write Pydantic or dataclass models with issuer ID, URL, publisher, hash, publication versus retrieval time, reporting basis, passage offsets, and source group.

    EXPECTED RESULT / VALIDATION:
        Bad issuer identifiers, fake page numbers, and empty provenance fail validation.

    PROGRESSIVE HINTS (ask for help one level at a time):
        H1: Explain what success means before coding.
        H2: Split into inputs, decisions, side effects, and outputs.
        H3: Decide what can be checked deterministically.
        H4: Consult the written + video resources in LESSONS_AND_TASKS.md.
        H5: Follow the task-specific build/validation rules above.
        H6: For a precise algorithmic walkthrough without code, ask the mentor.
    """
    ######################## ADD YOUR CODE HERE ########################
    # TODO T03: implement this function personally, then write/enable its tests.
    raise NotImplementedError("T03: define_company_and_document_contracts has not been implemented")
    ####################################################################


def define_research_contracts() -> dict[str, type]:
    """
    TASK: T04     OWNER: B     STUDY FIRST: B01

    DESCRIPTION:
        Declare Observation, Metric, Claim, Hypothesis, Discovery, ResearchState models

    HOW TO FILL THIS PLACEHOLDER:
        Represent units, comparable period boundaries, accounting basis, evidence links, claim-to-evidence relations, hypothesis lifecycle, budgets, and all eight report fields.

    EXPECTED RESULT / VALIDATION:
        A validated numerical observation without period/basis/units is invalid.

    PROGRESSIVE HINTS (ask for help one level at a time):
        H1: Explain what success means before coding.
        H2: Split into inputs, decisions, side effects, and outputs.
        H3: Decide what can be checked deterministically.
        H4: Consult the written + video resources in LESSONS_AND_TASKS.md.
        H5: Follow the task-specific build/validation rules above.
        H6: For a precise algorithmic walkthrough without code, ask the mentor.
    """
    ######################## ADD YOUR CODE HERE ########################
    # TODO T04: implement this function personally, then write/enable its tests.
    raise NotImplementedError("T04: define_research_contracts has not been implemented")
    ####################################################################
