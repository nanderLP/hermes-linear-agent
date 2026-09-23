"""Profile-scoped environment lookup."""

from __future__ import annotations

import os

try:
    from agent.secret_scope import UnscopedSecretError, get_secret
except ImportError:  # pragma: no cover - Hermes releases before multiplexed profiles
    get_secret = None


def profile_env(name: str) -> str:
    """Read a ``LINEAR_AGENT_*`` setting from the active Hermes profile.

    A multiplexed gateway serves secondary profiles without copying their
    ``.env`` into ``os.environ``; ``get_secret`` resolves the profile scope
    Hermes installs around config loading, adapter startup and turns. An
    unscoped read under multiplexing returns "" instead of another profile's value.
    """
    if get_secret is None:
        return os.getenv(name, "").strip()
    try:
        return (get_secret(name) or "").strip()
    except UnscopedSecretError:
        return ""
