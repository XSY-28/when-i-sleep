# When I sleep — run record

The current snapshot in this file is the single advancement authority. Update before yielding. Preserve original prompts and append historical events; auxiliary files hold evidence only.

## Current snapshot

- Run id / real project path / conversation:
- Host identity evidence / selected adapter / actually exposed integrations:
- User request and authority provenance:
- Start / deadline including timezone:
- Run status: `running | waiting | blocked | budget_exhausted | complete | stopped`
- Budgets: wake cadence / repairs per stage / elapsed time per stage / total:
- Scope / reversible assumptions:
- Actual scheduler id / creation result / cadence / stop result:
- Common ownership location / unique owner token / trusted owner / exclusion evidence:
- Active session/job ids / start times / cwd / logs / timeout / cancel mechanism:
- Latest relevant artifact fingerprint:
- Next safe action / wait condition / earliest recovery:
- Human-readable checkpoint path, if produced:

## Stage records

Repeat for each stage. Stage status: `pending | running | repairing | waiting | passed | blocked`.

- Id / original prompt or preserved prompt path / goal:
- Dependencies / independence evidence:
- Allowed modifications:
- Required acceptance and source, labeling inferred checks:
- Commands/observations / expected result / cwd:
- Current status / first start / elapsed time / cumulative repair rounds:
- Current artifact fingerprint including relevant uncommitted files:
- Acceptance evidence: times, command/method, result, fingerprint, log:
- Actual failure / root-cause hypothesis / repair prompt / repair result:
- Blocker and recovery condition:

## Events

Append timestamp → action → evidence → state change → next action. Keep failed checks and changes in user direction. Replayed wakeups do not reset counters.

## Final checkpoint

- Stage verdicts and evidence:
- Deliverables and actual changes:
- Unverified items / blockers / attempts:
- Bound continuation stop result:
- Owned operations: exit/cancel result, unknown or active work:
- Ownership release result:
- Elapsed budget / repair counts:
- Resume entry point and exact next action:

Append host-specific account fields only when the selected adapter requires them.
