# Checkpoint

Implemented Linux `locally_reachable_ips` fact in `lib/ansible/module_utils/facts/network/linux.py`. It queries IPv4 and IPv6 routes with `scope host` across all tables, skips non-delivering route types, normalizes and sorts IPs/prefixes, and warns with empty lists on query failure. Added unit tests in `test/units/module_utils/facts/network/test_linux.py`.

Checks: `pytest -q --disable-warnings test/units/module_utils/facts/network test/units/module_utils/facts/test_facts.py test/units/module_utils/facts/test_collectors.py` passed (153 passed, 7 skipped). `git diff --check` passed. `rg` is unavailable (`/bin/bash: rg: command not found`); used local alternatives. The `ip` binary is unavailable in this environment, so a live kernel route query was not run; behavior is covered by mocked route output tests.
