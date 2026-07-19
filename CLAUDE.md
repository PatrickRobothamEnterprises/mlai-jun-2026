# Project guide for Claude

This repo hosts an MLAI talk *and* doubles as the talk's live demo. The talk
materials are the `*.md` files; the demo is a tiny Python statistics library in
`src/` with a deliberate bug for the agent to fix.

When you're triggered from an issue, work on the **code in `src/` and `tests/`** —
ignore the talk markdown unless the issue asks about it.

## Conventions
- Python 3.10+. Standard library only — do not add dependencies.
- Public functions live in `src/stats.py` and have type hints and a short docstring.
- Every behavior change must be covered by a test in `tests/test_stats.py`.

## Definition of done
- `python -m pytest` passes with zero failures before you open a PR.
- Keep the diff minimal and focused on the issue at hand.
- Explain the root cause and the fix in the PR description.
