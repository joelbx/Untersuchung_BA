VERDICT: ACCEPT

The patch covers ipset rule construction, required parameter pairing, inversion, and use with other rule options. I found no correctness or regression issue.

- `python -m pytest -q test/units/modules/test_iptables.py` — 26 passed.
- `git diff --check` — passed.
- TEST_ENVIRONMENT_PROBLEM: none.

Review recorded in [checkpoint.md](/app/.codex-role-output/checkpoint.md).