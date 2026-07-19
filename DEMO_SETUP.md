# Demo setup

This repo **is** the live demo — the agent (`.github/workflows/claude.yml`) runs
on it directly. Arm it once and do a full dry-run before the talk.

Repo: `PatrickRobothamEnterprises/mlai-jun-2026`

## Prerequisites
- You're an **admin** of this repo.
- An **Anthropic API key** (console.anthropic.com) with credit.
- [GitHub CLI](https://cli.github.com/) authenticated: `gh auth login`.

## 1 · Push this repo (if you haven't)

```bash
git remote add origin git@github.com:PatrickRobothamEnterprises/mlai-jun-2026.git
git push -u origin main
```

## 2 · Install the Claude GitHub App

Easiest — from inside Claude Code:

```
/install-github-app
```

Install it on `mlai-jun-2026` (grants Contents / Issues / Pull requests
read+write). Or install manually at <https://github.com/apps/claude>.

## 3 · Add the API key as a repo secret

```bash
gh secret set ANTHROPIC_API_KEY --repo PatrickRobothamEnterprises/mlai-jun-2026
# paste your key when prompted
```

(Or: repo **Settings → Secrets and variables → Actions → New repository secret**,
named exactly `ANTHROPIC_API_KEY`.)

## 4 · Create the seeded issue

Use the text in [`SEED_ISSUE.md`](SEED_ISSUE.md):

```bash
gh issue create --repo PatrickRobothamEnterprises/mlai-jun-2026 \
  --title "median() returns the wrong value for even-length lists" \
  --body-file SEED_ISSUE.md
```

## 5 · Dry-run the whole flow

1. On the issue, add a comment: `@claude fix this`.
2. Watch the **Actions** tab — the `Claude Code` workflow runs (~30s–3 min).
3. Confirm a **PR** is opened; its diff fixes `median()`, adds a test, CI is green.
4. **Close the PR without merging** (and re-open a fresh issue) so the bug is still
   present and the demo is repeatable live. *Or* merge it and `git revert` locally
   before the talk to reset.

## 6 · Record a fallback

Screen-record steps 1–3 into [`fallback/`](fallback/) so a slow or flaky CI run
can't derail the talk. Save a screenshot of the final PR + green checks too.

---

## Gotchas
- Runs consume **GitHub Actions minutes + Claude API tokens** (a fix like this is cents; keep `--max-turns` low).
- Runs take ~30s to a few minutes — use the "Under the hood" slides as filler while it works.
- **Issue text is untrusted input** (prompt injection) — that's a talking point, not just a warning.
- You must be a repo **admin** to install the GitHub App.
- Trigger phrase defaults to `@claude`; the workflow only runs when it's present, so normal issue/PR chatter won't fire it.

## Alternative: hands-off auto-run
To have the agent fire the moment an issue is opened (no `@claude` needed), swap
the workflow trigger to a labeled-issue gate:

```yaml
on:
  issues:
    types: [opened]
jobs:
  claude:
    if: contains(github.event.issue.labels.*.name, 'auto-fix')
    # ...same steps; add `prompt:` with the issue body...
```
