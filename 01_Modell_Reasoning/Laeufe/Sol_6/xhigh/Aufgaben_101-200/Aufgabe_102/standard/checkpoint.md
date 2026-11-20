# Checkpoint

- Task: add Linux scope-host locally reachable IP facts in `lib/ansible/module_utils/facts/network/linux.py`.
- Repository is clean at start; no `AGENTS.md` found. `rg` is unavailable, so use `find` and `grep`.
- Implemented `locally_reachable_ips` in Linux network facts and registered its gather subset; it queries IPv4 and IPv6 host-scoped routes, normalizes and sorts addresses/prefixes, and warns while returning empty lists when unavailable.
- Documented the new gather subset in `setup.py` and added unit coverage for parsing, ordering, failure isolation, IPv6 absence, and fact exposure.
- Verification: `python3 -m pytest -q test/units/module_utils/facts/network test/units/module_utils/facts/test_facts.py test/units/module_utils/facts/test_collector.py` passed (147 passed, 5 skipped); `git diff --check` passed.
