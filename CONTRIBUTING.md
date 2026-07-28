# Contributing

1. Install Hermes from source in editable mode, following the upstream development guide.
2. Install this repository in the same environment with `python -m pip install -e ".[dev]" --no-deps`.
3. Run `pytest`, `ruff check hermes_linear_agent tests scripts __init__.py`, and `ruff format --check hermes_linear_agent tests scripts __init__.py`.
4. Keep Linear mutations fail-closed and add regression coverage for every behavioral change.
5. Do not add Linear-specific changes to Hermes core or import underscore-prefixed Hermes APIs.
6. Never commit credentials, webhook payloads containing private data, or OAuth state files.
