"""Plugin-local registry for the active Linear Agent adapter.

A standalone plugin is loaded under one package identity per installation
mode, so it can keep runtime state locally instead of mutating Hermes' global
tool registry.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .adapter import LinearAgentAdapter

_active_adapter: LinearAgentAdapter | None = None


def set_active_adapter(adapter: LinearAgentAdapter | None) -> None:
    """Register or clear the currently connected Linear Agent adapter."""
    global _active_adapter
    _active_adapter = adapter


def get_active_adapter() -> LinearAgentAdapter:
    """Return the currently connected Linear Agent adapter."""
    if _active_adapter is None:
        raise RuntimeError(
            "linear_agent platform is not currently connected. "
            "Make sure the Linear Agent plugin is enabled and the gateway is running."
        )
    return _active_adapter
