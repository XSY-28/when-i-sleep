# Execution and recovery

Read before starting any run. This skill is instructions, not a daemon, lock service, or hard watchdog. Host capabilities and permissions control what actually runs.

## One owner per project

Resolve the project's real path, including symlinks, and use a common ownership location under its permitted `when-i-sleep/` work root. Acquire project-scoped ownership **before** run discovery/creation, scheduler creation, or project edits. A separate lock per run id does not protect the project.

Use the host's mutex or an atomic ownership acquisition, such as creating a shared `.owner` directory. A read-then-write existence check is not atomic. Save a unique owner token, run id, conversation identity, start time, and operation identifiers. Replacing a record atomically does not provide execution mutual exclusion.

An existing owner requires read-only inspection. Resume the same run only when trusted host state confirms that its previous turn has ended and execution is serialized. An active or uncertain other owner means wait without another run or scheduler.

Reclaim or release ownership only under a common host mutex or an atomic operation that verifies the expected owner token. Proving an old process ended is necessary but does not make deleting its old lock race-free. If only a mkdir lock is available without safe conditional reclamation, leave a stale lock blocked; do not delete it on the basis of an earlier read, elapsed time, or a second read. Missing lock metadata is also ambiguous.

## Restore an operation

Before launching a long operation, persist its intent, timeout and cancellation mechanism; persist its session/job id as soon as available. Save cwd, command, process start time and logs. Restore the existing operation using the appropriate tool. Quiet logs or an old heartbeat do not prove death.

For a local PID, compare identity, start time, command and cwd to avoid PID reuse. After a crash, check whether child processes still write before takeover. If no reliable exit result exists, mark evidence unknown and revalidate only after exclusion is established. Never cancel another run's operation.

## Continuation contract

Use the selected host adapter's existing-conversation scheduler when available. The durable continuation prompt carries the skill, project path, run-record path, run id, original budget/deadline, and instructions to restore state, verify before advancing, repair failures, ask no questions, checkpoint on resource exhaustion, and stop on a terminal state. Replay does not refresh authority or budgets.

Reuse a matching scheduler instead of creating duplicates. Save its actual id, cadence and result. If creation is uncertain, inspect for the existing result before retrying. An unavailable scheduler must be reported, not replaced by an unsolicited cron service, hidden daemon, or unapproved cross-conversation loop.

## Deadlines and cleanup

At a stage deadline stop that stage's new work; at the run deadline stop all new development. Make a bounded cancellation attempt for operations this run demonstrably owns, using their session/job interface, then confirm exit/cancellation. An unavailable or failed cancellation leaves the operation unknown or active: preserve its identifiers and ownership, checkpoint, and do not start dependent work.

Release ownership only when owned operations cannot continue writing, using the safe token-checked protocol. Terminal ticks may inspect cleanup and retry stopping their bound scheduler. Distinguish stopping advancement, stopping scheduling, and ending background operations; none implies the others succeeded.

## Durable state

`run.md`'s current snapshot is the sole advancement authority. Update it after important actions and before yielding: overall/stage status, repair counts, deadlines, active operations, latest artifact fingerprint, and next action. Logs, auxiliary JSON and old summaries are evidence rather than competing state machines. A terminal report must not leave a `running` snapshot behind.

On context compaction or restart, restore from this snapshot and inspect actual files/processes. Related changes invalidate prior acceptance evidence. Final checkpoints link evidence and leave a concrete recovery entry point.
