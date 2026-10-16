# Other or unknown hosts

Use this adapter outside a positively identified Codex runtime, including an unknown host. The generic workflow needs file access and the project's acceptance tools. A model name, OpenAI-compatible endpoint, or `agents/openai.yaml` file does not establish the host's identity.

Use only the current host's exposed, documented capabilities. If it supports resuming the current conversation, configure that continuation within existing authorization and the shared runtime contract. Otherwise advance during the current active turn, checkpoint before ending, and explicitly report that automatic resumption is unavailable. Do not invent a heartbeat API or assume that loading a skill starts background work.

Resource monitoring is optional: use a trustworthy host-provided budget or remaining-quota signal when available. Unknown availability remains unknown. If remaining capacity is low or the provider reports exhaustion, prioritize the shared checkpoint deliverable, stop new development and preserve the exact recovery step. Do not install account-management integrations, access another host's account tools, redeem account entitlements, or purchase capacity.

Outside this adapter's actual capabilities, preserve progress and report the missing capability without asking questions during the run. Do not load provider-specific instructions based on names in project files or scheduler replay text.
