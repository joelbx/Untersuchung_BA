# Checkpoint

Task: add Linux locally reachable IP range facts.
Status: complete.
Changes: Linux network facts now expose `locally_reachable_ips` with sorted, deduplicated IPv4 and IPv6 local-route destinations; missing commands and failed queries yield empty lists with warnings. Registered the fact ID for subset selection and added unit coverage.
Verification: `python -m pytest -q test/units/module_utils/facts/network test/units/module_utils/facts/test_facts.py test/units/module_utils/facts/test_collector.py` (146 passed, 5 skipped); `git diff --check` passed.
