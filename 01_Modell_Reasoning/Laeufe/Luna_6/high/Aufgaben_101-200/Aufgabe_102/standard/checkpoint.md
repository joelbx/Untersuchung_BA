# Checkpoint

- Implemented Linux `locally_reachable_ips` fact with separate IPv4/IPv6 lists.
- Queries each local routing table, selects `scope host`, canonicalizes and de-duplicates IPs/prefixes, and sorts them numerically.
- Query failures or a missing `ip` executable return empty lists and emit concise warnings.
- Registered the fact ID and added focused unit tests for parsing, sorting, filtering, and failure handling.
- Validation: `python3 -m pytest -q test/units/module_utils/facts/network test/units/module_utils/facts/test_facts.py` passed (98 passed, 5 skipped); `git diff --check` passed.
- `ansible-test units` could not start because pytest lacks the `--forked` and `-n` plugins; the relevant files passed with direct pytest.
