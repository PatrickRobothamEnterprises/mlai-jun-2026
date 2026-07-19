---
name: pixi-python
description: >-
  Use pixi (pixi.toml) for ALL Python environment and dependency management —
  never pip, venv, virtualenv, conda, or poetry directly. Trigger whenever
  setting up a Python project, installing/adding/removing packages, creating or
  activating an environment, running Python scripts or tests, or when you see
  pip install, python -m venv, requirements.txt, environment.yml, poetry, or a
  pixi.toml / pixi.lock.
---

# pixi for Python

**Golden rule:** manage Python environments and dependencies with `pixi`. Do **not** run
`pip install`, `python -m venv`, `virtualenv`, `conda`, or `poetry` directly.

## Command mapping
| Instead of | Use |
|---|---|
| `pip install X` (available on conda-forge) | `pixi add X` |
| `pip install X` (PyPI-only, not on conda-forge) | `pixi add --pypi X` |
| `python script.py` | `pixi run python script.py` |
| `pytest` | `pixi run test` (define the task once) or `pixi run pytest` |
| `python -m venv .venv && source …` | `pixi install` (env lives in `.pixi/`) |
| one-off tool (ruff, httpie, …) | `pixi exec ruff …` |

`pixi run` auto-updates `pixi.lock` and installs the environment first, so you rarely need to call
`pixi install` by hand. Prefer `pixi run <cmd>` over activating a shell.

## New Python project (no manifest yet)
1. `pixi init` → creates `pixi.toml` (or `pixi init --format pyproject` to keep everything in
   `pyproject.toml` under `[tool.pixi.*]`).
2. Set `platforms` to what you actually need, e.g. `["osx-arm64", "linux-64"]`.
3. Add dependencies: `pixi add python pytest` (conda), `pixi add --pypi <pkg>` (PyPI-only).
4. Define tasks: `pixi task add test "pytest"` → run with `pixi run test`.

## Existing pip / venv / conda project (pixi everywhere)
Offer to adopt pixi rather than silently converting:
- Import existing specs: `pixi init --import environment.yml`, or translate a `requirements.txt`
  into `pixi add --pypi …` entries.
- Commit `pixi.toml` **and** `pixi.lock`; add `.pixi/` to `.gitignore`.
- Leave the old `requirements.txt` / `environment.yml` in place only if the project still needs them
  for non-pixi consumers; otherwise remove them once migrated.

## Manifest shape (`pixi.toml`)
```toml
[workspace]
name = "my-project"
channels = ["conda-forge"]
platforms = ["osx-arm64", "linux-64"]

[dependencies]          # conda packages
python = ">=3.10"
pytest = "*"

[pypi-dependencies]     # PyPI-only packages
# some-pkg = "*"

[tasks]
test = "pytest -q"

# Optional multi-environment setup:
# [feature.docs.dependencies]
# mkdocs = "*"
# [environments]
# docs = ["docs"]
```

`pyproject.toml` works too — same tables prefixed with `[tool.pixi.*]` (e.g. `[tool.pixi.workspace]`).

## Everyday commands
- `pixi add <pkg>` / `pixi add --pypi <pkg>` — add a dependency.
- `pixi remove <pkg>` — remove one.
- `pixi run <task|cmd>` — run in the env (installs + updates the lock as needed).
- `pixi install` — sync the env from the lockfile.
- `pixi update` — bump locked versions.
- `pixi list` / `pixi tree` — inspect installed packages.
