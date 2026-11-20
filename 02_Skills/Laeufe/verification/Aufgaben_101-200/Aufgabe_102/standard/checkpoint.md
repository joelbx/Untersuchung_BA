# Checkpoint

- Implemented `locally_reachable_ips` in Linux network facts as `{'ipv4': [...], 'ipv6': [...]}` from `ip -4/-6 route show table local`, accepting only local routes.
- Addresses and prefixes are normalized, deduplicated, and sorted; failed family queries return an empty list with a warning. Missing `ip` returns empty lists with a warning.
- Registered the fact in the Linux network collector, documented it, and added unit tests for normalization, ordering, failure, IPv6 absence, and collection integration.
- Verification: `python -m pytest -q test/units/module_utils/facts/network test/units/module_utils/facts/test_facts.py test/units/module_utils/facts/test_collector.py` exited 0: 146 passed, 5 skipped.
