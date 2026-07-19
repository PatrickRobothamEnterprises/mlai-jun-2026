# Speaker notes

Keep this on a second screen. Times are targets; total ≈ 35 min + Q&A.
Scroll [`TALK.md`](TALK.md) slide-by-slide as you go.

## Before you start
- Tabs open: `TALK.md` (fullscreen), the demo repo, the seeded issue, a
  **merged example PR** (for cold open + Q&A), the Actions tab.
- `fallback/` recording queued in case CI is slow.

---

### Cold open — "A machine read a bug report" (2 min)
Show the finished PR first. "Nobody typed the code in this diff. An agent read
an issue, found the bug, edited the file, ran the tests, and opened this PR.
For the next half hour I'll show you exactly what that is — and why it's not
magic." Don't over-introduce yourself.

### The plan (30 sec)
Just read the six items. Set expectation: one live demo in the middle.

---

### 1 · What is an agent? (6 min)
- **Single LLM call:** anchor the ML crowd — this is a forward pass they know.
  Great at proposing, can't *do*.
- **An agent (diagram):** say the definition out loud, twice —
  *agent = LLM + tools + a loop + an environment.* This is the spine of the talk.
- **Four pieces table:** the loop is the novel part — it's what lets the agent
  *verify its own work*.
- **Autonomy spectrum:** locate our example on the right. The PR is the review gate.

### 2 · Why issue → PR? (3 min)
- **Human workflow diagram:** trace each arrow. Emphasise the fail→plan loop.
- **Capability table:** each human step maps to one agent capability. Land it as
  "a complete agent task you can hold in your head."

### 3 · Anatomy (7 min)
- **Tools:** hands and eyes; without them the LLM can only talk.
- **Context:** you steer with context (`CLAUDE.md`), not hard-coded steps. Point
  out the "pytest must pass" line — that's *why* it runs tests at all.
- **Loop & budget:** tie back to the "Done?" node; budget = safety net.
- **Safety/permissions:** least privilege — can open a PR, can't merge.
- **The whole agent in one file:** the punchline — no framework, the loop is
  inside the action.

---

### 4 · LIVE DEMO (10 min)  ← the centrepiece
**Script:**
1. Show `src/stats.py` and run `pytest` → 1 red test. "Here's the bug, and here's
   a test that catches it."
2. Show the open issue. Read it aloud — note it's a *good* issue (clear repro,
   expected vs actual). Good issues → reliable agents.
3. Comment `@claude fix this`.
4. Switch to the **Actions** tab; narrate the log as it runs. If it's slow, jump
   ahead to the "Under the hood" slides and come back.
5. Open the PR: walk the diff, the new test, Claude's summary comment.
6. Show CI green. Optionally merge.

**If anything stalls → cut to `fallback/` immediately.** Don't fight live CI on stage.

---

### 5 · Under the hood (4 min)
- **Runner diagram:** the red→edit→green cycle is the loop earning its keep — it
  caught its own mistake with no human.
- **Trace slide:** it's just tool calls, one at a time, reacting to observations.
  Demystify: no hidden magic.

### 6 · Where it breaks (4 min)
- **Failure modes:** the common thread — a tight feedback signal (tests/types/CI)
  is what makes it work *and* what fixes most failures.
- **Prompt injection:** the sharp one for this crowd. Issue text is untrusted;
  "agent-era SQL injection." Read the attacker example.
- **Human in the loop:** agent opens, human merges; review, don't rubber-stamp;
  it moves the human *up a level*.

### Takeaways + Thank you (bal.)
Repeat the three: definition, verification, human-on-merge. Then Q&A.

---

## Likely Q&A
- **Cost per run?** GitHub Actions minutes + Claude tokens; a fix like this is cents.
- **Large repos?** Context limits; scope the task, lean on grep/subagents, good `CLAUDE.md`.
- **Flaky tests?** The loop may thrash; you want a reliable signal — same lesson.
- **vs Copilot/Cursor?** Autonomy spectrum — those suggest inline; this acts and opens a PR.
- **Self-hosted / other models?** Action also supports Bedrock / Vertex.
- **Does it merge itself?** No — least privilege by design; a human merges.
