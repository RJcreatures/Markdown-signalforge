#!/usr/bin/env python3
"""
****************************************************************************************
                           SIGNALFORGE / ATMOS 2026
                   STUDENT IMPLEMENTATION BOILERPLATE
****************************************************************************************
FILE: src/signalforge/config.py
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
import os
from pydantic import BaseModel, Field

############################ TASK CONSTANTS ############################
# ADD only domain-generic constants after reading docs and defining tests.
# Do not hard-code particular company findings or sample outputs.




class Settings(BaseModel):

    track: str = Field(default="C")
    search_provider: str

    request_timeout_seconds: int = Field(default=20, gt=5)
    download_timeout_seconds: int = Field(default=30, gt=5)
    max_download_bytes: int = Field(default=20 * 1024 * 1024, gt=5) # 20 MB
    max_sources_per_run: int = Field(default=10, gt=0)
    max_candidates: int = Field(default=3, gt=0)
    max_investigation_loops: int = Field(default=2, ge=0)


    allowed_source_classes: list[str] = Field(
        default_factory=lambda: [
            "issuer_report",
            "regulatory_filing",
            "official_announcement",
            "news_lead"        ]
    )


    require_source_url: bool = True
    require_document_hash: bool = True
    require_page_evidence: bool = True




############################ FUNCTION DEFINITIONS ############################

def load_settings() -> dict[str, Any]:
    """
    TASK: T02     OWNER: A     STUDY FIRST: A01

    DESCRIPTION:
        Load environment-backed settings and bounded per-run budgets

    HOW TO FILL THIS PLACEHOLDER:
        Define provider settings, public-source allowlist, request timeout, bytes cap and run budget; validate them; never store secrets in source control.

    EXPECTED RESULT / VALIDATION:
        A missing required setting returns a clear error before a network call.

    PROGRESSIVE HINTS (ask for help one level at a time):
        H1: Explain what success means before coding.
        H2: Split into inputs, decisions, side effects, and outputs.
        H3: Decide what can be checked deterministically.
        H4: Consult the written + video resources in LESSONS_AND_TASKS.md.
        H5: Follow the task-specific build/validation rules above.
        H6: For a precise algorithmic walkthrough without code, ask the mentor.
    """
    try:
            # prevents error
        settings_obj = Settings(
            track=os.getenv("TRACK", "C"),
            search_provider=os.getenv("SEARCH_PROVIDER", "brave").lower(),
            request_timeout_seconds=os.getenv("REQUEST_TIMEOUT_SECONDS", 20),
            download_timeout_seconds=os.getenv("DOWNLOAD_TIMEOUT_SECONDS", 30),
            max_download_bytes=os.getenv("MAX_DOWNLOAD_BYTES", 20 * 1024 * 1024),
            max_sources_per_run=os.getenv("MAX_SOURCES_PER_RUN", 10),
            max_candidates=os.getenv("MAX_CANDIDATES", 3),
            max_investigation_loops=os.getenv("MAX_INVESTIGATION_LOOPS", 2),
            allowed_source_classes=os.getenv("ALLOWED_SOURCE_CLASSES", "issuer_report,regulatory_filing,official_announcement,news_lead").split(",")
        )
    except Exception as e:
        raise ValueError(f"Configuration validation failed: {e}")

        # Handle LLM Provider and API key check
    llm_provider = os.getenv("LLM_PROVIDER", "openai").lower()
    api_key_env_var = f"{llm_provider.upper()}_API_KEY"
    api_key = os.getenv(api_key_env_var)

        # Dump Pydantic model to dictionary and append provider/key status
    config_dict = settings_obj.model_dump()
    config_dict["llm_provider"] = llm_provider
    config_dict["has_api_key"] = api_key is not None

    return config_dict



    # TODO T02: implement this function personally, then write/enable its tests.
    raise NotImplementedError("T02: load_settings has not been implemented")
    ####################################################################
