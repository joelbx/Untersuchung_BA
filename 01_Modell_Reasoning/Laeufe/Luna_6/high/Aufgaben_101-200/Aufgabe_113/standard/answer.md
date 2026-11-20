Implemented manual route-target management in [nxos_vrf_af.py](/app/lib/ansible/modules/network/nxos/nxos_vrf_af.py). The new `route_targets` option supports multiple entries, `import`/`export`/`both` directions, and per-entry `present`/`absent` state. `both` defaults to adding or removing both directions, and changes are scoped to the selected VRF address-family.

Added coverage for mixed changes, idempotency, and `match_current_rt` in [test_nxos_vrf_af.py](/app/test/units/modules/network/nxos/test_nxos_vrf_af.py).

Validation passed: `python -m pytest -q test/units/modules/network/nxos/test_nxos_vrf_af.py` (6 tests) and `git diff --check`.