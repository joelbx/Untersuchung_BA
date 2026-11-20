# Checkpoint

Task: add ipset set-extension support to the Ansible iptables module.

Completed:
- Added `match_set` and `match_set_flags` arguments, documentation, and example.
- Required both arguments together, restricted flags to `src`, `dst`, `src,dst`, or `dst,src`, and rejected an empty set name.
- Generated one `-m set --match-set` clause for implicit or explicit set matching; the existing `!` prefix inverts the match.
- Added unit coverage for all flag choices, explicit and implicit matches, inversion, invalid combinations, and an empty name.

Verification:
- `pytest -q test/units/modules/test_iptables.py` — 27 passed.
- `git diff --check` — passed.
- Live iptables invocation was unavailable: `command -v iptables` produced no path (exit status 1). Command syntax was checked through module argument-list unit tests; live iptables parsing remains unverified.
