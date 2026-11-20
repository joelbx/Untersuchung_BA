# Checkpoint

- Task: add manual route-target management to `nxos_vrf_af`.
- Initial inspection: module currently manages address-family presence and EVPN auto only.
- `rg` is unavailable in this environment (`/bin/bash: rg: command not found`); using `find` and `grep` for local discovery.
- Implemented `route_targets` with per-entry `rt`, `direction`, and `state`; `both` expands to import and export. Exact-line comparison is scoped to the selected VRF address-family block. EVPN auto and address-family state remain supported.
- Added focused unit coverage for context creation, mixed add/remove in one load, scope, idempotence, EVPN auto removal, absent behavior, required `rt`, and the public helper.
- Verification: `python -m pytest -q test/units/modules/network/nxos/test_nxos_vrf_af.py` exited 0 with 10 passed. `git diff --check` exited 0.
