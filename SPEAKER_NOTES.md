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
By the end of this talk you'll know exactly how it works." Don't
over-introduce yourself.

### The plan (30 sec)
Read the seven items. Flag the shape: why → definition → history → how-to →
demo → getting started → further reading. One live demo in the middle.

---

### 1 · Why agents? (3 min) — the hook
- **Captured our imagination:** name the shared experience — everyone here
  has had the chat-window wow moment; no need to sell the models to this
  room. Then point at where the real work lives: repos, inboxes, queues,
  spreadsheets. Agents are how the model gets there.
- **Agents in the wild:** brisk — one breath per bullet, this is a montage,
  not a lecture. Land on "today's demo is one of these" so the room knows
  the cold-open PR wasn't a party trick.
- **The gap is smaller than it looks:** the promise slide — a loop, a
  handful of tools, a few pages of clear writing, all of it in this talk.
  This is the contract with the audience: by the end, you can build one.

### 2 · What is an agent? (5 min)
- **Textbook slide:** open on home turf for this crowd — sensors, actuators,
  policy π: percept → action. Half the room read Russell & Norvig; the RL
  folks know it as the agent–environment loop. Close on: "the definition
  held; what changed is what fills the boxes and what it costs to draw the
  arrows" — section 3 traces that change through the policy, the periphery,
  and the wiring between them.
- **Single LLM call:** a forward pass they know. It can describe the fix but
  can't open the file or run the tests — a promising policy with no sensors
  or actuators attached.
- **The loop diagram:** say the modern definition out loud, twice —
  *agent = LLM + tools + a loop + an environment* — then point back at the
  textbook diagram: same picture. Once the model can see the results of its
  own actions, it can catch its own mistakes.
- **Four pieces table:** read the classic-term column — LLM = policy,
  read-tools = sensors, write-tools = actuators.
- **Autonomy spectrum:** you choose where on the line your agent sits.
  Today's demo hands you a PR; the PR is the checkpoint where a human looks
  before anything permanent happens.

### 3 · How did LLMs change agents? (5 min)
- **Agents are old news:** callback to section 2 — thermostat, AlphaGo, RPA
  all fit the definition. Don't re-explain; pose the question: "if the
  definition is thirty years old, what changed?"
- **Old bottleneck table:** each era's policy only understood what its
  builders anticipated — and the sensors/actuators were hand-built around
  that narrow policy (state encodings, fixed action spaces). Every new task
  meant a new agent from scratch, hands and eyes included.
- **What changed — three things:** (1) Toolformer, 2023 — LLMs taught
  themselves to call APIs; chatbot novelty → coding agents and assistants.
  (2) Multimodal seq2seq ate traditional ML's lunch — zero/few-shot on
  unstructured text/image/video, no per-task dataset. (3) The arrows
  changed — the do-stuff layer (shells, APIs, permissions) is what it always
  was; the wiring used to be per-agent glue code and hand-designed
  encodings, now it's a description: an MCP entry, a SKILL.md. Bang for your
  buck: deployment, actions, context. Then land the pull-quote — "the brain
  is rented by the token, and the craft has moved into everything around
  it." Pause on
  it; it's the hinge of the talk.
- **Why this talk exists:** deployment, actions, context — that's the map
  for the rest of the talk. Point at each word in the diagram.

### 4 · How do you build an agent? (10 min) — the meat
- **4a Deployment:** same loop, four homes — terminal, CI, server, cron. What
  changes is feedback speed, credentials, and whether anyone's watching.
  Terminal = you're right there, generous permissions are fine. CI at 2am =
  tighter permissions, hard budgets, output lands somewhere reviewable.
  Punchline: today's entire deployment is ~5 lines of YAML, no framework.
- **4b Prompts:** the agent's program is mostly text it reads before acting.
  Show `CLAUDE.md`. Then the definition-of-done slide — walk the story:
  "fix the bug" lets the agent decide for itself when it's done; "tests must
  pass" gives the loop a finish line it can check, so a failed attempt leads
  to another attempt instead of a declared victory. Say the closing line:
  "most of the reliability you'll ever get out of an agent comes from this
  line." It pays off in the demo.
- **4c Tools/MCP/Permissions:** a tool is just name + description + schema;
  every result feeds the next decision — the sensor and actuator halves of
  the textbook diagram. MCP: write the server once, every agent can use it;
  the ecosystem compounds. Permissions: new-hire analogy; read the SSH-key
  attack line aloud — this crowd will feel it. The design goal: a fooled
  agent produces a weird PR somebody rejects, not a compromised system.
- **4d Skills:** the prompt says what to do now; a skill captures how your
  team does a job, reused across tasks. Say explicitly: "if that sounds like
  a standard operating procedure, that's exactly what it is — hold that
  thought," pointing at section 6.

---

### 5 · LIVE DEMO (10 min)  ← the centrepiece
**Script:**
1. Show `src/stats.py` and run `pixi run test` → 1 red test. "Here's the bug,
   and here's a test that catches it."
2. Show the open issue. Read it aloud — note it's a *good* issue (clear repro,
   expected vs actual). Good issues make for reliable agents.
3. Comment `@claude fix this`.
4. Switch to the **Actions** tab; narrate the log as it runs. While CI works,
   walk the "What happened on the runner" and "trace" slides as filler.
5. Open the PR: walk the diff, the new test, Claude's summary comment.
6. Show CI green. Optionally merge.
7. Close on the recap table: point at each row — "deployment, prompt, tools,
   permissions, verification — everything from section 4, on one screen."

**If anything stalls → cut to `fallback/` immediately.** Don't fight live CI
on stage.

- **Runner diagram:** point at the red arrow — the agent read the failing
  output and went back to editing. It caught its own mistake with nobody
  watching.
- **Trace slide:** demystify — one tool call at a time, reacting to whatever
  comes back. That's the entire mechanism.

### 6 · How do I get started? (4 min) — the payoff
- **What we actually wrote:** replay the list — a definition of done, a
  procedure, a scope of authority, an escalation path. Let the room realise
  where this is going before you say it: organisations have been writing
  these documents for a century.
- **Checklists/SOPs/runbooks table:** the reveal. "Most of the agent already
  exists. It's sitting in a binder, waiting for a loop to run it."
- **Start with the procedure you already own:** ops engineer, accountant,
  support lead. The scarce ingredient is a procedure written clearly enough
  for someone else — or something else — to follow. Close on the recipe:
  pick one document, give it a checkable finish line and tight permissions.

### 7 · Where do I learn more? (7 min) — the afterword
Frame it as further reading: headlines to go chase, not a tutorial. Move
briskly; this section flexes if time is short.
- **7a Workflows:** tell the story — one agent improvising forty steps loses
  the thread around step twenty, so move the control flow into a script. The
  script fans out, verifies, merges; each agent gets one small job with a
  clear check; retries live in ordinary code and behave the same every run.
- **7b Logging/UUIDs:** once nobody's watching, the trace is your only window
  into what happened. IDs on every run/agent/tool-call so you can correlate;
  replay the trace instead of guessing; saved traces become regression tests
  for prompt changes. Frame as the microservices observability discipline
  they already know.
- **7c Memory:** context window = working memory, gone at session end.
  Long-term memory = files read at start, updated at end. Spend a beat on
  curation: an accumulating memory fills with stale advice and the agent will
  faithfully follow it. "Prune it the way you'd prune a team wiki."
- **7d Swarms:** two motivating problems — jobs bigger than one context, and
  findings too important for a single pass — one answer: more agents, smaller
  jobs. Fan-out, adversarial verification (skeptics try to knock each finding
  down), judge panels.
- **The pattern slide:** read the four-part sentence, then the turn: it
  describes how a good lead hands work to a team — management skills, the
  same discipline as getting started in section 6, with more loops. Lands
  straight into the takeaways.

### Takeaways + Thank you (bal.)
Repeat the three: the definition (rented brain, plug-in periphery),
verification carries the system, if you can write the procedure you can
build the agent. Then Q&A.

---

## Likely Q&A
- **Cost per run?** GitHub Actions minutes + Claude tokens; a fix like this is cents.
- **Large repos?** Context limits; scope the task, lean on grep/subagents/swarms, good `CLAUDE.md`.
- **Flaky tests?** The loop may thrash; the finish line has to be a reliable
  signal — the definition-of-done lesson again.
- **vs Copilot/Cursor?** Autonomy spectrum — those suggest inline; this acts and opens a PR.
- **Isn't MCP just function calling?** Function calling is the model-side
  mechanism; MCP standardises the *server* side so tools are shared across agents.
- **How do you eval agents?** Traces + a checkable definition of done; replay
  failures as regression tests (section 7b).
- **Prompt injection defences?** Least privilege, human review gate, treat all
  input as hostile; there's no silver bullet — design for blast radius.
- **Self-hosted / other models?** The action also supports Bedrock / Vertex.
- **Does it merge itself?** No — a human merges, by design.
- **"I'm not a programmer — can I really do this?"** If you can write the
  runbook, yes — pair with an engineer for deployment/permissions the first time.
