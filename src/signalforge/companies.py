#!/usr/bin/env python3
"""
****************************************************************************************
                           SIGNALFORGE / ATMOS 2026
                   STUDENT IMPLEMENTATION BOILERPLATE
****************************************************************************************
FILE: src/signalforge/companies.py
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


def resolve_company(query: str, sector: str) -> dict[str, Any]:
    """
    TASK: T06     OWNER: A     STUDY FIRST: A04

    DESCRIPTION:
        Resolve a judge-entered company or exchange symbol to its legal issuer

    HOW TO FILL THIS PLACEHOLDER:
        Normalize query; search current authoritative company/index registry; disambiguate names; check sector; record official identifier; never bake analysis results into company branches.

    EXPECTED RESULT / VALIDATION:
        Ambiguous inputs stop safely; unknown but listed issuers can be researched through a generic fallback.

    PROGRESSIVE HINTS (ask for help one level at a time):
        H1: Explain what success means before coding.
        H2: Split into inputs, decisions, side effects, and outputs.
        H3: Decide what can be checked deterministically.
        H4: Consult the written + video resources in LESSONS_AND_TASKS.md.
        H5: Follow the task-specific build/validation rules above.
        H6: For a precise algorithmic walkthrough without code, ask the mentor.
    """




    normalized_name = query.strip().lower()

    #print(f"Resolving company for query: '{query}' in sector: '{sector}'")












    ######################## ADD YOUR CODE HERE ########################
    #  T06: implement this function personally, then write/enable its tests.
    #raise NotImplementedError("T06: resolve_company has not been implemented")
    ####################################################################




name = "Reliance Industries Limited"
ctor = "Energy"

resolve_company(query=name, sector=ctor)