# Checkpoint

Task: add manually configurable route-target entries to nxos_vrf_af.
Status: complete. Added the route_targets list interface, exact scoped comparison helper, command generation for import/export/both and present/absent, documentation, and unit coverage.
Checks:
- `python -m pytest -q test/units/modules/network/nxos/test_nxos_vrf_af.py` — 9 passed.
- `git diff --check` — passed.
