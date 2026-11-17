"""Groq cloud engine (OpenAI-compatible, no local GPU needed — ideal for phones).

Set your key with ``export GROQ_API_KEY=gsk_...`` (get one free at
https://console.groq.com/keys) or pass ``api_key=`` explicitly.
"""

from __future__ import annotations

import os
from typing import List

from openjarvis.core.registry import EngineRegistry
from openjarvis.engine._openai_compat import _OpenAICompatibleEngine

GROQ_DEFAULT_MODEL = "llama-3.3-70b-versatile"
GROQ_MODELS = [
    "llama-3.3-70b-versatile",
    "llama-3.1-8b-instant",
    "openai/gpt-oss-20b",
    "openai/gpt-oss-120b",
]


@EngineRegistry.register("groq")
class GroqEngine(_OpenAICompatibleEngine):
    """Groq's OpenAI-compatible endpoint: https://api.groq.com/openai/v1."""

    engine_id = "groq"
    is_cloud = True
    _default_host = "https://api.groq.com/openai"
    _api_prefix = "/v1"

    def __init__(self, host: str | None = None, *, api_key: str | None = None,
                 timeout: float = 60.0) -> None:
        key = api_key or os.environ.get("GROQ_API_KEY")
        super().__init__(host, api_key=key, timeout=timeout)

    def health(self) -> bool:
        # Only "healthy" when a key is configured; avoids useless network calls.
        if not self._api_key:
            return False
        try:
            return self._client.get("/v1/models", timeout=5.0).status_code == 200
        except Exception:
            return False

    def list_models(self) -> List[str]:
        try:
            return super().list_models() or list(GROQ_MODELS)
        except Exception:
            return list(GROQ_MODELS)
