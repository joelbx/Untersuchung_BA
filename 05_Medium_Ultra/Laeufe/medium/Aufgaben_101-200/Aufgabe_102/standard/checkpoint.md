# Checkpoint

Task: add Linux locally reachable IP ranges to network facts.
Status: implemented and verified.
Changes: `locally_reachable_ips` fact with IPv4/IPv6 lists from local host-scope routes; canonicalized, deduplicated, sorted. Missing command or failed route query yields empty lists with warning. Registered Linux collector fact ID and added unit coverage.
Verification: `python -m pytest -q test/units/module_utils/facts/network` (9 passed); `git diff --check` passed.
