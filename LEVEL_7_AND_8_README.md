# SignalForge hint upgrade: Levels 7 and 8

**Team A:** you. **Team B:** your partner. The existing 56 tasks and 50 placeholders retain their owners and prereqs.

## Level 7 — “Tell me exactly what to use”

Open `HINT_LADDER_56_TASKS.md` and find your task number. Level 7 provides concrete library/module/class/method names and technical guardrails tailored to that task. Each Python placeholder also repeats the relevant Level 7 under `PROGRESSIVE HINTS`. No code is supplied at this level.

## Level 8 — “I give up; show me the full solution”

Level 8 is an **explicit opt-in**. The boilerplate still contains `ADD YOUR CODE HERE`. If stuck after Level 7, ask your mentor:

> Level 8 — GIVE UP on task T10. Give me the full implementation of only `downloads.download_pdf` for our existing starter code, the required imports, test cases and an explanation. Keep all existing function signatures and avoid changing unrelated code.

Substitute the task ID and function name from the `TASK_SLOT_INDEX.json`. The solution is not preprinted for all 56 tasks: that would defeat the learn-by-coding purpose and produce a giant, untested app. If you use Level 8, each student must inspect the code, run meaningful tests and explain it. A generated answer is not automatically correct.

## Checking status

`python -m compileall -q src` checks syntax only. The existing pytest placeholders are **skipped**, not passing. The program is **not** a finished MVP.
