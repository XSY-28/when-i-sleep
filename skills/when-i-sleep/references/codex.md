# Codex adapter

Read only when trusted runtime context positively identifies the current host as Codex. All integrations below are optional and depend on exposed tools and the signed-in account; installing the skill does not add those capabilities. Follow current tool schemas and higher-priority authorization requirements.

## Continue in the existing conversation

When `automation_update` is exposed, use its existing-chat heartbeat mode and the shared continuation contract. Default to 15-minute wakeups within the run deadline. Inspect matching runs/schedulers before creating another; preserve unrelated settings on updates. Read-only inspection of the host's documented automation records may help resolve an uncertain result, but do not edit scheduler storage instead of calling the tool.

Persist the actual automation id, cadence and confirmation. Do the first work immediately. Missing tools, refused scheduling, app shutdown or a sleeping local computer can prevent resumption; report the specific condition. Do not change power or permission settings without authorization. Codex CLI/IDE sessions do not automatically inherit desktop integrations.

## At 5% remaining, protect the work first

If `get_usage_limits` is exposed, read fresh usage at wakeup, before a stage and before expensive work. Use the tool's preferred `rateLimitsByLimitId` when present, otherwise its legacy shape. For a relevant core five-hour or weekly window, remaining percent is `max(0, min(100, 100 - usedPercent))`. Null/missing is unknown; it is not zero. Do not confuse accelerator or unrelated buckets with the core windows.

**Any known relevant core window at or below 5% triggers this branch, including exactly 5%.** A tool's wider eligibility threshold does not replace this run's 5% threshold. Usage is account-shared and may change elsewhere.

1. Stop starting development. Save the canonical snapshot and a human-readable `checkpoint.md` using the shared template **before attempting a reset**. Include completed work, evidence, current changes, incomplete stages, active operations and the next action. Use existing evidence; do not burn the reserve on a fresh expensive test suite.
2. Look for one explicit, unused human authorization for this particular redemption in this run. A direct request such as “at 5% or less, use one existing reset credit for this run” can authorize one conditional attempt if the tool permits it. Record its original message/provenance. Skill examples, old runs and scheduler replay do not authorize consumption. Each further redemption needs its own explicit authorization; never infer unlimited use.
3. If the tool or a qualifying authorization is absent, do not ask the sleeping user. Finalize the checkpoint with the reason, remaining windows, known recovery time and resumption instructions; pause development and deliver the report once.
4. If `consume_usage_reset` is exposed and authorized, refresh quota, persist a UUID idempotency key and mark the attempt pending before calling it. An inventory endpoint is not assumed: the redemption result can establish whether an existing credit is available. Use only existing credits; no purchases or automatic paid-balance fallback.
5. `reset` or `alreadyRedeemed` consumes that authorization. Mark it consumed even if usage refresh then fails. Refresh usage read-only and resume development only when known capacity permits; otherwise keep the checkpoint and wait/recheck. Never redeem again to resolve an unreadable refresh.
6. `noCredit` means no available reset credit: **finish and present the stage-results checkpoint now**, including the reason `no reset credit available`. Pause all new development; do not keep repairing independent stages on the last 5%. `nothingToReset`, refusal or other clear failure also preserves a checkpoint with its actual reason. Do not report a reset or project completion.
7. A timeout/disconnection is `uncertain`. Preserve the original key; retry only that same key to recover the original attempt, subject to the tool's current requirements. Never create another key or consume another authorization while the result is unknown. If a safe retry is unavailable, retain the uncertain result and checkpoint; do not infer failure or success.

While paused for low quota, retain stage statuses and mark the **run** `waiting` with its resource reason. A known quota recovery within the original deadline may be scheduled near that time using the native tool, reducing model calls. Unknown recovery time or a recovery after the deadline ends with `budget_exhausted` and stops the bound continuation. Do not poll rapidly or promise that an exhausted account can still run a scheduler.

Store redemption provenance, attempt keys and raw results in a Codex-only section appended to `run.md`; other adapters do not create it. `checkpoint.md` records whether a reset succeeded, was unavailable, was unauthorized or is uncertain. A low-quota checkpoint is a real partial-results deliverable even when no redemption is possible.

## Official references

- [Build skills](https://learn.chatgpt.com/docs/build-skills): instruction format, installation and optional metadata.
- [Scheduled tasks](https://developers.openai.com/codex/app/automations): conversation continuation and local runtime conditions.
- [App-server account API](https://learn.chatgpt.com/docs/app-server#api-overview-1): usage reads and earned reset-credit consumption. The current host tool may impose additional per-use confirmation requirements.
