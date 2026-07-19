# Project guide for Claude

This repo hosts an MLAI talk *and* doubles as the talk's live demo. The talk
materials are the `*.md` files; the demo is a tiny Python statistics library in
`src/` with a deliberate bug for the agent to fix.

When you're triggered from an issue, work on the **code in `src/` and `tests/`** —
ignore the talk markdown unless the issue asks about it.

## Conventions
- Python 3.10+, managed with **pixi** (`pixi.toml`). Manage dependencies with `pixi add`
  (conda-forge) or `pixi add --pypi` — do not use `pip`, `venv`, or `conda` directly.
- Public functions live in `src/stats.py` and have type hints and a short docstring.
- Every behavior change must be covered by a test in `tests/test_stats.py`.

## Definition of done
- `pixi run test` passes with zero failures before you open a PR.
- Keep the diff minimal and focused on the issue at hand.
- Explain the root cause and the fix in the PR description.
