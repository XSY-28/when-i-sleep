# Validation scope

## Reproducible local checks

From the repository root, with Python 3.10+:

```bash
python -m pip install -r requirements-dev.txt
python scripts/check_package.py
python scripts/check_example.py
```

Or use an isolated temporary dependency environment with uv installed:

```bash
uv run --no-project --with PyYAML==6.0.3 python scripts/check_package.py
python3 scripts/check_example.py
```

The package check verifies seven bundled runtime files, skill frontmatter and
OpenAI UI metadata, local links, lack of personal absolute paths, and a static
boundary preventing account-reset operations from leaking into shared resources
or the other-host adapter. It does not simulate the reasoning of a live agent.

The example check copies the cart fixture to a temporary directory and supplies
controlled implementations. Four cases establish that fixed checks reject the
initial bug, accept the corrected subtotal, reject a missing receipt, and accept
the receipt with subtotal regression checks. It does not claim that an agent
performed those edits or successfully executed the documentation stage.

GitHub Actions runs these checks on Python 3.10 and 3.13. A committed workflow
is not evidence of a successful run; inspect the actual Actions result.

## Behavioral review cases

These are review cases for the instructions, not automated live integration
tests. They define what to inspect when exercising an actual host adapter.

| Situation | Required decision |
| --- | --- |
| A model is served by OpenAI, but its host is not Codex | Select the other-host adapter; no Codex account instructions |
| Source changed after a prior passing report | Revalidate affected stages before advancing |
| A real integration criterion lacks credentials | Keep it blocked; proceed only with established independent work |
| Core remaining quota is exactly 5%, no usable credit | Write and present the stage-results checkpoint; pause development |
| Five-hour remaining is 6%, weekly remaining is 4% | Codex low-quota branch applies |
| A reset attempt timed out | Preserve the same request key and uncertain result; no second redemption |
| Reset says already redeemed but refresh fails | Mark authorization consumed; no new redemption |
| No scheduler is exposed | Work in the active turn, checkpoint and disclose that resumption is unavailable |
| A stale owner cannot be safely reclaimed | Wait without deleting the lock or starting another writer |
| One stage times out but independent work remains | Stop that stage; continue only within the total deadline |
| Stopping continuation fails | Keep terminal state; future ticks only inspect cleanup and retry stop |
| A final report says blocked | The authoritative snapshot must also say blocked |

## Integration evidence still needed

Live overnight continuation, actual reset redemption, account exhaustion during
scheduling, crash recovery, concurrent ownership stress, Windows execution and
each non-Codex host require their own observed validation. The skill currently
ships an execution protocol, not a background service or mandatory isolation
mechanism. Higher-priority host permissions remain in force.
