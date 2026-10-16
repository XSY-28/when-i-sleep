# When I sleep 🌙

**Give your project a plan for the hours you're away.**

An agent skill for staged coding projects: **verify the current stage, repair failures, and advance when the evidence passes.** Leave a project and its stage prompts; return to completed work or a checkpoint that tells you exactly what remains.

[中文](README.zh-CN.md) · [Install](#install) · [Try the example](#try-it-on-a-small-project) · [How hosts differ](#choose-your-host)

```text
Stage prompt → Work → Acceptance checks → Pass → Next ready stage
                              ↓ Fail
                         Save repair prompt
                              ↓
                         Fix → Check again

Missing capability, exhausted budget, or low quota → Stage-results checkpoint
```

## Put it to work

In Codex, after installation:

```text
Use $when-i-sleep.
Project: /path/to/my-project
Stage prompts: docs/stages.md
Verify each stage, repair failures, and keep advancing. Don't ask me questions.
```

On another skill-capable host, invoke **When I sleep** using that host's skill syntax. A stage plan can also be pasted directly into the conversation.

The workflow is designed to:

- **Earn the next stage.** Run the acceptance checks against the current files, including uncommitted changes.
- **Turn failures into work.** Save a repair prompt with the actual error, edit scope and recheck command, then execute it.
- **Keep useful work moving.** Record a blocked stage and continue work that is explicitly independent.
- **Leave a clear handoff.** Save artifacts, verdicts, evidence, budgets and the exact recovery action before stopping.
- **Protect the final reserve.** In Codex, at **≤5% remaining quota**, checkpoint first. If an existing reset credit cannot be used, deliver the stage-results report and pause new development.

There are no questions during the run. Decisions outside the authorized scope become recorded blockers. The workflow preserves acceptance criteria and uses bounded repair attempts.

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

The skill is an instruction package. It does not install a background service or make a closed application continue running. Local unattended continuation needs a running host, accessible project files, suitable permissions, and a computer that stays awake. Codex's native continuation capability is described in the [official scheduled-task documentation](https://developers.openai.com/codex/app/automations).

## When Codex reaches 5%

The trigger is **any known relevant core five-hour or weekly window at or below 5% remaining**. An unknown value stays unknown.

1. Save the run state and a readable `checkpoint.md` before spending the reserve.
2. If the required tool and an explicit authorization for one redemption exist, try one existing reset credit.
3. If there is no usable credit, produce the stage-results report and pause new development. The report lists finished work, current changes, checks, blockers, active operations and the next action.
4. Resume after a verified reset or a known recovery time within the run deadline. Otherwise leave a resumable checkpoint.

To authorize one conditional redemption, append this to **that run's** request:

```text
For this run, when quota is at or below 5%, use one existing reset credit.
```

No credit purchase is performed. Each redemption follows the host's authorization rules; an example or a previous run cannot authorize a new one. An uncertain redemption keeps the same request key to avoid double consumption. See the [Codex adapter](skills/when-i-sleep/references/codex.md).

## Tune a night of work

| Setting | Default |
| --- | --- |
| Wake cadence, when supported | 15 minutes |
| Repair rounds | 3 per stage |
| Elapsed stage budget | 2 hours |
| Total run budget | 8 hours |

Override these in your request. Passing a stage advances immediately in the same turn; the cadence is for resumption, not a delay between stages. Counters persist across wakeups.

The run keeps a single authoritative `run.md`, original prompts, saved repair prompts, evidence logs, and a human-readable checkpoint when needed. It asks for no new input while you are away. Publishing, deploying, purchasing and external messages still require authorization already given for the run.

## Try it on a small project

The repository includes an [intentionally broken cart example](examples/cart/STAGES.md). Copy `examples/cart/` to a disposable working directory and ask the skill to run its `STAGES.md`. No live account, API key or package install is needed for the example itself; Python 3 is required.

Expected behavior: notice the incorrect subtotal, save and execute a repair, pass the fixed checks, then add a receipt function and verify it. This gives you a small project to inspect before leaving a larger one unattended.

## What has been checked

The package validator checks metadata, bundled references, local documentation links, private-path leakage and the boundary keeping account operations inside the Codex adapter. A reproducible example check confirms that the cart fixture rejects its broken implementation and accepts the expected behavior.

These checks do **not** establish overnight reliability, successful live reset redemption, crash recovery or compatibility with every host. See [validation and review cases](docs/validation.md) for the exact scope and commands.

## Contribute

Useful contributions include a host adapter backed by documented tools, an observed failure with a small reproduction, or a clearer acceptance/recovery rule. Keep platform-specific actions out of the shared workflow and preserve the checkpoint path when continuation is unavailable.

[MIT License](LICENSE).
