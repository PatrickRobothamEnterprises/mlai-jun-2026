# Seed issue for the live demo

Create this as a GitHub issue in the demo repo. Then, during the talk, add a
comment `@claude fix this` (or include `@claude` in the body when opening it) to
trigger the agent.

A *well-written* issue is part of the story: clear repro + expected vs. actual
is exactly what makes the agent reliable. Point this out on stage.

---

**Title:** `median()` returns the wrong value for even-length lists

**Body:**

`median()` gives the wrong answer when the list has an even number of elements.
It should average the two middle values, but instead it returns the lower one.

**Repro:**
```python
from src.stats import median
median([1, 2, 3, 4])
```

**Expected:** `2.5`  (the average of the two middle values, 2 and 3)
**Actual:** `2`

Odd-length lists are fine — only the even-length case is broken. Please fix
`median()` and add a test covering the even-length case.
