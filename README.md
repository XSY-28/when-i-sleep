# When I sleep 🌙

**Go to sleep. Your project has a recovery plan.**

You split a project into stages, write the prompts, queue them up, and head to bed.

At 2 a.m., a test fails in stage two. The later prompts assume that stage worked. Someone needs to read the error, decide what to fix, rerun the checks, and work out whether it is safe to continue.

That someone is asleep.

**When I sleep gives your coding agent instructions for that decision.** It checks the current stage, writes and executes a repair prompt when a check fails, and advances dependent work only after acceptance passes. You supply the project and stage prompts; the agent handles the repair-and-recheck loop within the limits you set.

[中文](README.zh-CN.md) · [Install](#install) · [Use it tonight](#use-it-tonight) · [Try a small project](#try-it-on-a-small-project)

## What happens after you leave?

Suppose your plan is **database → API → interface**.

| What happens during the run | What the skill tells the agent to do |
| --- | --- |
| The database stage passes | Save its evidence and start the API stage. |
| An API test fails | Read the failure, save a specific repair prompt, apply the fix, and rerun the checks. |
| The repaired API passes | Start the interface stage against the verified result. |
| A required credential is missing | Record the blocker, leave dependent stages pending, and continue established independent work. |
| Codex has ≤5% quota left and no usable reset credit | Stop new development and deliver a report of the work completed so far. |

**You do not have to wake up to write the repair prompt or decide whether the next stage can start.** During the run, the agent makes reversible choices within your scope and records decisions it cannot make. Repair attempts and elapsed time are bounded, so a stubborn failure has a stopping point.

Continuation between turns requires your host's scheduler. For local unattended runs, keep the computer awake and the host application running; see [host support](#choose-your-host).

## What do you come back to?

Completed stages with acceptance evidence, plus a clear handoff for anything unfinished. A blocked run might leave a checkpoint like this **illustrative example**:

```text
Database: passed.
API: passed after repairing a failing request-validation check.
Interface: blocked; real-account sign-in needs staging credentials.

Saved: current changes, test logs, the API repair prompt, and run.md.
Next: once staging credentials are available, resume interface acceptance.
```

The checkpoint tells you what changed, what was actually checked, where work stopped, and how to resume. If a required check cannot run, it stays unverified; the agent preserves the failure and the remaining work.

## Use it tonight

After installation, give Codex the project and your stage prompts:

```text
Use $when-i-sleep.
Project: /path/to/my-project
Stage prompts: docs/stages.md
Verify each stage, repair failures, and advance when it passes.
Don't ask me questions while I'm away.
```

You can paste the stages directly instead of using a file. On another skill-capable host, invoke **When I sleep** using that host's syntax.

## Install

### Codex

Ask the built-in skill installer:

```text
$skill-installer Install the skill from
https://github.com/XSY-28/when-i-sleep/tree/main/skills/when-i-sleep
```

Codex detects installed skills automatically; restart it if the skill does not appear. See the [official skill documentation](https://learn.chatgpt.com/docs/build-skills).

### Other Agent Skills hosts

Download or clone this repository, then place the **entire** [`skills/when-i-sleep`](skills/when-i-sleep) directory in your host's configured skills location. Keep `references/` and `assets/` alongside `SKILL.md`. The OpenAI UI metadata in `agents/` is optional outside Codex.

Back up local customizations before replacing an existing installation. Host-specific paths and invocation syntax vary; follow your host's documentation.

## Choose your host

| Runtime | Stage verification and repair | Continuation while you're away | Account reset handling |
| --- | --- | --- | --- |
| Codex with the required desktop tools | Shared skill workflow | Existing-chat heartbeat when actually exposed | Existing credits only, with explicit per-use authorization |
| Codex without those tools | Shared skill workflow | Current active turn; checkpoint for later resumption | Disabled when the required tools are unavailable |
| Other hosts accepting `SKILL.md` | Portable instructions; host execution not yet verified here | Only the host's own supported scheduler | Not enabled |

**The host is detected from the actual runtime, not the model name.** Using an OpenAI model in another agent does not enable the Codex adapter. Other hosts never load the Codex account instructions.

The skill uses the host's actual continuation tools and permissions. Codex's native continuation capability is described in the [official scheduled-task documentation](https://developers.openai.com/codex/app/automations). Installing a skill alone does not create a background service.

## When Codex reaches 5%

The last few percent should be enough to leave a useful handoff. When a relevant core five-hour or weekly window reaches **≤5% remaining**, the Codex adapter saves `checkpoint.md` before attempting a reset.

With an available tool and a valid per-use authorization, it can try one existing reset credit. **If no credit can be used, it organizes the completed work, current changes, acceptance results, blockers and next step, then pauses new development.** It may resume after verified recovery within the original deadline.

To authorize one conditional redemption, append this to **that run's** request:

```text
For this run, when quota is at or below 5%, use one existing reset credit.
```

This is Codex-only behavior. Other hosts do not load account-reset instructions. Redemptions follow the host's authorization rules and use existing credits only; see the [Codex adapter](skills/when-i-sleep/references/codex.md) for recovery and duplicate-request handling.

## Tune a night of work

| Setting | Default |
| --- | --- |
| Wake cadence, when supported | 15 minutes |
| Repair rounds | 3 per stage |
| Elapsed stage budget | 2 hours |
| Total run budget | 8 hours |

Override these in your request. Passing a stage advances immediately in the same turn; the cadence is for resumption, not a delay between stages. Counters persist across wakeups.

Set different limits in the same request if your project needs them. Publishing, deploying, purchasing and external messages still require authorization already given for the run.

## Try it on a small project

The repository includes an [intentionally broken cart example](examples/cart/STAGES.md). Copy `examples/cart/` to a disposable working directory and ask the skill to run its `STAGES.md`. No live account, API key or package install is needed for the example itself; Python 3 is required.

Expected behavior: notice the incorrect subtotal, save and execute a repair, pass the fixed checks, then add a receipt function and verify it. This gives you a small project to inspect before leaving a larger one unattended.

## What has been checked

Package checks and the cart fixture are reproducible in [validation and review cases](docs/validation.md). They check packaging and fixed acceptance behavior. Real overnight reliability, live reset redemption, crash recovery and non-Codex host execution still need integration evidence.

## Contribute

Useful contributions include a host adapter backed by documented tools, an observed failure with a small reproduction, or a clearer acceptance/recovery rule. Keep platform-specific actions out of the shared workflow and preserve the checkpoint path when continuation is unavailable.

[MIT License](LICENSE).
