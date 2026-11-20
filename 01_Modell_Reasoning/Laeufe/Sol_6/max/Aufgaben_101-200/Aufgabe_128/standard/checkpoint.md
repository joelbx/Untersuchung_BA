# Checkpoint

- Objective: add `match_set` and `match_set_flags` support to the Ansible `iptables` module, including validation, rule generation, and relevant tests.
- State: implemented ipset argument validation, automatic and explicit set match construction, inversion, documentation, example, changelog, and unit coverage.
- Verification: `PYTHONPATH=lib:test python3 -m pytest -q test/units/modules/test_iptables.py` (26 passed); `git diff --check` passed.
