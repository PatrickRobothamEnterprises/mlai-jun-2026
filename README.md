# MLAI talk — "From Issue to PR: An Agent That Ships Code"

Materials for a ~35-minute talk (MLAI, June 2026) explaining what an AI *agent*
is, using one concrete example: an agent that **reads a GitHub issue and opens a
PR to fix it** — the official
[`anthropics/claude-code-action`](https://github.com/anthropics/claude-code-action).

This single repo does double duty: it holds the talk **and** is the live-demo
target the agent operates on.

## What's here

| Path | What it is |
|---|---|
| [`TALK.md`](TALK.md) | **The talk.** Present it straight from GitHub in the browser — scroll top to bottom, each `---` is a slide. Mermaid diagrams render natively. |
| [`SPEAKER_NOTES.md`](SPEAKER_NOTES.md) | Per-section talking points, timing, and the live-demo script. Keep on a second screen. |
| [`DEMO_SETUP.md`](DEMO_SETUP.md) | Step-by-step to arm the live demo (GitHub App, secret, seed issue, dry-run). |
| [`.github/workflows/claude.yml`](.github/workflows/claude.yml) | **The agent** — the Claude Code Action, triggered by `@claude` on an issue. |
| [`src/`](src/) · [`tests/`](tests/) | The demo target: a tiny stats lib with a seeded `median` bug + tests that catch it. |
| [`CLAUDE.md`](CLAUDE.md) | Conventions the agent reads before making changes. |
| [`SEED_ISSUE.md`](SEED_ISSUE.md) | The bug report to file as the demo issue. |
| [`fallback/`](fallback/) | Recorded run + screenshots — live-demo insurance. |

## Run the tests

```bash
python -m pytest -q
```

One test (`test_median_even_length`) fails until the agent's fix is merged —
that's the bug the demo fixes.

## Giving the talk

1. Open [`TALK.md`](TALK.md) on GitHub in your browser (full-screen the tab).
2. Have the demo repo, the seeded issue, and a merged example PR open in other tabs.
3. Follow [`SPEAKER_NOTES.md`](SPEAKER_NOTES.md); scroll `TALK.md` slide by slide.
4. At section 4, run the live demo (or play [`fallback/`](fallback/) if CI is slow).

## The demo in one line

Comment `@claude fix this` on an issue → the Claude Code Action reads the issue,
edits the code, runs the tests, and opens a PR. See [`DEMO_SETUP.md`](DEMO_SETUP.md).
