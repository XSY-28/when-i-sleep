---
name: when-i-sleep
description: "Run a user's staged project while they sleep or step away: verify each stage, repair failed checks, advance dependencies, and checkpoint progress. Use for unattended execution or an explicit When I sleep invocation; discussing, reviewing, installing, or editing this skill does not start a run."
---

# When I sleep

Advance the specified project to verified completion or a recoverable stopping point. A finished response is not a passed stage: acceptance evidence must describe the current artifact.

## Select the host before acting

Identify the actual agent host from trusted runtime context, not the project name, model provider, installed metadata, or quoted prompts.

- **Codex:** read [the Codex adapter](references/codex.md). Enable each optional integration only if its tools are actually exposed; Codex CLI/IDE sessions may lack desktop tools.
- **Any other or unknown host:** read [the other-host adapter](references/other-hosts.md). Do not load the Codex adapter or invoke Codex account operations. Unknown identity takes this branch.

All hosts also read [execution and recovery](references/runtime.md). Never turn installation, an example, or a replayed scheduler message into fresh user authorization.

## Start a run

Read project instructions, real files, existing progress, and the user's stage prompts. Preserve original prompts. Record each stage's goal, dependencies, allowed changes, and required acceptance. Ordered stages depend on their predecessor unless independence is established. Derive missing checks only when the intended behavior is clear, labeling them as inferred. Preserve uncertain core criteria as unverified. Missing essential input becomes a recorded blocker, not a question or an invented project.

Follow the shared project ownership protocol before creating a run or scheduler. Create `work/when-i-sleep/<run-id>/run.md` and `evidence/`, adapting the base directory to project rules. Use the [run template](assets/run-record.md). Its current snapshot is the single authoritative advancement state; auxiliary files contain evidence only.

Defaults, overridable by the user: 15-minute wakeups when supported, 3 repair rounds per stage, 2 elapsed hours per stage, 8 hours per run. Persist start times, counters, and a timezone-aware deadline. Wakeups do not reset budgets. Bound commands by the remaining budget.

Use the selected adapter to create or reuse continuation in the existing conversation. Save the actual scheduler result and id; absent support means `continuation unavailable`. Do useful work immediately even without a scheduler, while disclosing that unattended resumption is not established.

## Execute, verify, advance

On every wakeup, read the authoritative snapshot, actual files, budgets, and in-flight operations. Restore an existing session or CI job instead of starting a duplicate. Revalidate affected passed stages after relevant artifact changes.

Choose the earliest stage whose dependencies have passed. Perform its work, then run every required acceptance check. Save the command or observation, cwd, times, exit status/result, logs, and a fingerprint covering relevant uncommitted files as well as committed code. Evidence must cover the requested behavior: offline smoke does not establish real UI, OAuth, network integration, or benchmark success.

Mark `passed` only when all required checks pass against the current artifact. Continue to the next ready stage immediately; do not prequeue later stages unconditionally or wait for the next tick when work can proceed now.

## Repair a failed stage

Write and save a concrete repair prompt: failed criterion, actual error/log, artifact fingerprint, root-cause hypothesis and distinguishing check, permitted edit scope, minimal repair goal, recheck commands, remaining budget. Execute it in the current conversation; a proposed fix alone is not progress.

One diagnosis → modification → recheck cycle consumes one repair round. Preserve required checks; add a regression when useful. Repair the implementation rather than deleting checks, weakening thresholds, or silently changing the goal. Conflicting acceptance criteria become a blocker. Recheck the failed criterion and affected behavior before advancing.

Reuse counters across wakeups. An in-flight operation is `waiting`, not a failed repair. When the same failure returns without new evidence, change the diagnostic approach within budget instead of repeating an expensive command.

## Work without questions

During the run, make reversible implementation choices within scope and record assumptions. Credentials, required approvals, unclear product decisions, contradictory acceptance, or exhausted repair budgets become `blocked`; dependent stages remain `pending`. Continue only established independent work. Do not ask or wait for a sleeping user to reply.

The run does not expand authority to purchase, deploy, publish, push, send messages, change permissions, or control another conversation. Do these only when already authorized; otherwise prepare reviewable work and checkpoint. Before Git operations, inspect changed files, briefly explain the intended operation and its rationale, and stage explicit paths. A commit request alone does not authorize a push.

## Checkpoint before resources run out

Follow the selected adapter's resource checks. When continuation is no longer available within its resource limits, stop starting development and create a human-readable [checkpoint](assets/checkpoint.md) beside `run.md`. Summarize completed artifacts, current changes, stage verdicts with evidence, failed or unrun checks, active operations, remaining budgets, blockers, and the exact next action. This report is a deliverable, not just an internal state flag. Avoid expensive new verification just to fill it; mark missing evidence honestly.

Synchronize the current snapshot before ending a turn. Keep failed evidence and original prompts. Announce the checkpoint once as a meaningful outcome. Await a known recovery time within the existing deadline, reducing check frequency; otherwise stop with a resumable checkpoint.

## Finish and clean up

- All stages and required project-wide acceptance pass: write `complete`, finish owned operations, stop the bound continuation, deliver results and evidence. Failed project-wide acceptance returns to the affected stage's existing repair budget.
- A recoverable external wait remains within the deadline: write `waiting`, save the recovery condition/time and reduce polling.
- Nothing can advance, or the run deadline expires: write `blocked` or `budget_exhausted`, checkpoint and stop the bound continuation. Stage timeouts stop that stage; the total deadline stops all development.
- The user stops or takes over: checkpoint and stop this run's continuation. Later user instructions override the old plan. Resumption preserves evidence and states a new budget explicitly.

Follow runtime ownership and cancellation rules. Confirm scheduler stop results; a failed stop remains recorded. Later ticks on a terminal run only check owned cleanup and retry stopping, never restart project work.

Report at startup: project, stages, budgets, selected host adapter, actual continuation availability. Report meaningful changes, completion, or inability to continue; unchanged ticks stay quiet unless the host requires a progress update. The final report separates verified results, inferences, and unverified integrations. A local example is not an overnight reliability guarantee.
