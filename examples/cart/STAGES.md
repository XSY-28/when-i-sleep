# A small staged project

Copy this directory to a disposable working directory before running the skill.
Use Python 3 and run commands from that directory. No scheduler, account operation,
network access, package installation, Git mutation or external message is needed.

The user is away: make reversible choices and do not ask questions. Preserve
`acceptance.py`; repair the implementation instead of changing fixed checks.

## Stage 1 — correct the subtotal

`cart.subtotal(prices)` returns the total cost, with an empty list returning zero.
Scope: `cart.py`. Required acceptance: `python3 acceptance.py totals` exits 0.
This is the only initial stage; do not assume the starter code passes.

## Stage 2 — add a receipt

Depends on Stage 1 passing. Add `cart.receipt(prices)`, returning a dictionary
with `items` equal to the number of prices and `subtotal` equal to their total.
Scope: `cart.py`. Required acceptance: `python3 acceptance.py receipt` exits 0,
which also rechecks the first stage.

## Stage 3 — document use

Depends on Stage 2 passing. Write `USAGE.md` with a total and a receipt example.
Required acceptance: execute both examples against the current implementation
and confirm their documented outputs. Save commands and outputs as evidence.

Final acceptance: both fixed acceptance commands pass against the final artifact,
and both documented examples have been executed. Save the run record and any
repair prompts. If continuation is unavailable, say so; do not claim an overnight
run occurred.
