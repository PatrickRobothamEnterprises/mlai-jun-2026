# Speaker notes

Keep this on a second screen. Times are targets; total ≈ 40 min + Q&A.
Scroll [`TALK.md`](TALK.md) slide-by-slide as you go.

## Before you start
- Tabs open: `TALK.md` (fullscreen), the demo repo, the seeded issue, a
  **merged example PR** (for cold open + Q&A), the Actions tab.
- `fallback/` recording queued in case CI is slow.

---

### Cold open — "A machine read a bug report" (2 min)
Show the finished PR first. "Nobody typed the code in this diff. An agent read
an issue, found the bug, edited the file, ran the tests, and opened this PR.
By the end of this talk you'll know exactly how it works — and you'll see that
the hard part isn't the AI." Don't over-introduce yourself.

### The plan (30 sec)
Read the six items. Flag the shape: definition → history → **how-to** → demo →
advanced → "and it's probably you." One live demo in the middle.

---

### 1 · What is an agent? (5 min)
- **Classic definition first:** open on home turf for this crowd — sensors,
  actuators, policy π: percept → action. Half the room read Russell & Norvig;
  the RL folks know it as the agent–environment loop. Key line: "the
  definition hasn't changed — what fills the *policy box* has."
- **Single LLM call:** a forward pass they know. No sensors, no actuators —
  great at proposing, can't *do*.
- **The loop diagram:** say the modern definition out loud, twice —
  *agent = LLM + tools + a loop + an environment* — then point back:
  it's the same picture; the loop *is* the percept–action cycle.
- **Four pieces table:** read the classic-term column — LLM = policy,
  read-tools = sensors, write-tools = actuators. The loop lets the agent
  *verify its own work*.
- **Autonomy spectrum:** the review gate is a design choice you make. We'll
  place today's demo on the right end when we get there.

### 2 · How did LLMs change agents? (5 min)
- **Agents are old news:** callback to the definition from section 1 —
  thermostat, AlphaGo, RPA all fit it. Don't re-explain; the question is
  "so what changed?"
- **Old bottleneck table:** every pre-LLM agent was a one-off; nothing
  transferred.
- **What LLMs changed:** the policy became *general* and *speaks your
  language*. The pull-quote is the hinge of the whole talk — "the brain is an
  API call; the hard part is everything around it." Pause on it.
- **Why this talk exists:** 95% brain / 5% plumbing flipped. Sections 3–5 are
  the plumbing. This sets up everything that follows.

### 3 · How do you build an agent? (10 min) — the meat
- **3a Deployment:** same loop, four homes — terminal, CI, server, cron.
  Deployment decides latency, credentials, and *who's watching*. Headless ⇒
  tighter permissions + output lands somewhere reviewable. Punchline: today's
  entire deployment is ~5 lines of YAML, no framework.
- **3b Prompts:** you steer with *context*, not hard-coded steps. Show
  `CLAUDE.md`. Then the big one — **the definition of done is the most
  important prompt.** "Vague goals produce confident garbage; verifiable goals
  produce loops that self-correct." That line pays off in the demo when the
  agent re-runs tests.
- **3c Tools/MCP/Permissions:** tools = hands and eyes; a tool is just
  name + description + schema. MCP = USB-C for tools — write the server once,
  every agent can use it. Permissions: intern analogy, least privilege, issue
  text is *untrusted input* (read the SSH-key attack line — this crowd will
  feel it). "Worst case embarrassing, not catastrophic."
- **3d Skills:** prompts say what to do *now*; skills capture *how we do this
  here*. Show the release-checklist skill. Say explicitly: "writing a skill is
  writing an SOP — hold that thought," pointing at section 6.

---

### 4 · LIVE DEMO (10 min)  ← the centrepiece
**Script:**
1. Show `src/stats.py` and run `pixi run test` → 1 red test. "Here's the bug,
   and here's a test that catches it."
2. Show the open issue. Read it aloud — note it's a *good* issue (clear repro,
   expected vs actual). Good issues → reliable agents.
3. Comment `@claude fix this`.
4. Switch to the **Actions** tab; narrate the log as it runs. While CI works,
   walk the "What happened on the runner" and "trace" slides as filler.
5. Open the PR: walk the diff, the new test, Claude's summary comment.
6. Show CI green. Optionally merge.
7. Close on the recap table: point at each row — "deployment, prompt, tools,
   permissions, verification — everything from section 3, on one screen."

**If anything stalls → cut to `fallback/` immediately.** Don't fight live CI
on stage.

- **Trace slide:** demystify — one tool call at a time, reacting to
  observations. The red→edit→green cycle is the loop earning its keep.

### 5 · Next level (7 min)
- **5a Workflows:** one agent improvising 40 steps loses the thread; put
  control flow in *code*, keep agents small and checkable. Loops and retries
  are deterministic — "reliable, not vibes."
- **5b Logging/UUIDs:** "agents you can't observe, you can't trust." UUID per
  run/agent/tool-call; replay the trace instead of guessing; traces become
  evals. Frame it as the microservices discipline they already know.
- **5c Memory:** context window = working memory, wiped per session. Long-term
  memory = files the agent reads at start, writes at end. Key line: "curated,
  not accumulated — stale memory is worse than none."
- **5d Swarms:** fan-out, adversarial verification (skeptics try to *refute*),
  judge panels. "The unit of scaling isn't a bigger context — it's more,
  smaller, checkable agents."
- **One-liner slide:** read it, then the turn: "…which sounds less like ML
  engineering and more like *management*." Perfect segue to 6.

### 6 · Who can build agents? (4 min) — the send-off
- **The skill is specifying:** replay what we actually wrote today — a
  definition of done, a procedure, a scope of authority, an escalation path.
  Let the room realise before you say it.
- **Checklists/SOPs/runbooks table:** the reveal. "Most of the agent is
  already written — it's just in a binder."
- **Who owns the procedure:** ops person, accountant, support lead. The
  bottleneck is procedural clarity, not model access. "Teams that write things
  down win the agent era by default."

### Takeaways + Thank you (bal.)
Repeat the three: the definition (brain is rentable, you build the rest),
verification is the whole game, if you can write the SOP you can build the
agent. Then Q&A.

---

## Likely Q&A
- **Cost per run?** GitHub Actions minutes + Claude tokens; a fix like this is cents.
- **Large repos?** Context limits; scope the task, lean on grep/subagents/swarms, good `CLAUDE.md`.
- **Flaky tests?** The loop may thrash; you need a reliable signal — the
  definition-of-done lesson again.
- **vs Copilot/Cursor?** Autonomy spectrum — those suggest inline; this acts and opens a PR.
- **Isn't MCP just function calling?** Function calling is the model-side
  mechanism; MCP standardises the *server* side so tools are shared across agents.
- **How do you eval agents?** Traces + a checkable definition of done; replay
  failures as regression tests (section 5b).
- **Prompt injection defences?** Least privilege, human review gate, treat all
  input as hostile; there's no silver bullet — design for blast radius.
- **Self-hosted / other models?** The action also supports Bedrock / Vertex.
- **Does it merge itself?** No — least privilege by design; a human merges.
- **"I'm not a programmer — can I really do this?"** If you can write the
  runbook, yes — pair with an engineer for deployment/permissions the first time.
