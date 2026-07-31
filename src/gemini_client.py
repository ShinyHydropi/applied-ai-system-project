"""
Shared Gemini API client and guardrail helpers for this project's genAI
features (src/explain.py, src/parse_preferences.py).
"""

from google import genai
from google.genai import types

TIMEOUT_MS = 10_000

_client = None

_TRUSTWORTHY_FINISH_REASONS = {types.FinishReason.STOP}


def get_client() -> genai.Client:
    global _client
    if _client is None:
        _client = genai.Client()  # reads GEMINI_API_KEY / GOOGLE_API_KEY
    return _client


def sanitize(value, max_len: int = 120) -> str:
    """Collapses whitespace/newlines and caps length on untrusted input.

    Keeps a crafted field (e.g. embedded newlines plus fake instructions)
    from restructuring a prompt built around it.
    """
    text = " ".join(str(value).split())
    if len(text) > max_len:
        text = text[:max_len].rstrip() + "..."
    return text


def response_is_trustworthy(response) -> bool:
    """Rejects responses Gemini blocked or cut off instead of completed cleanly."""
    feedback = getattr(response, "prompt_feedback", None)
    if feedback is not None and getattr(feedback, "block_reason", None):
        return False
    candidates = getattr(response, "candidates", None) or []
    if not candidates:
        return False
    finish_reason = getattr(candidates[0], "finish_reason", None)
    return finish_reason in _TRUSTWORTHY_FINISH_REASONS
