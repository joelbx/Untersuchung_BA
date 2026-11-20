# Checkpoint

Investigating nxos_vrf_af route-target support. Repository search tool `rg` is unavailable (`/bin/bash: rg: command not found`); using local file inspection. No changes to module yet.

## Root cause and hypothesis
`main()` only declares `route_target_both_auto_evpn` and compares that single line within the AF block. No argument schema or command generation exists for manual route-target values. `NetworkConfig.get_block_config(path)` returns the requested AF block, so exact line comparison within that block can preserve VRF/AF scope. Existing `nxos_evpn_vni` code shows device CLI uses `route-target import/export VALUE` and `no` forms.

Hypothesis: adding a nested `route_targets` argument plus exact per-direction line comparison against the scoped AF block will support mixed operations and idempotence without touching unrelated contexts.

## Implementation and verification
Added nested `route_targets` options (`rt`, `direction`, `state`), documented them, and added `match_current_rt` to compare exact import/export lines in the selected AF block. `main()` now emits one AF context prefix for auto EVPN and manual route-target changes. AF removal continues to ignore route-target options.

Before implementation: `python -m pytest -q test/units/modules/network/nxos/test_nxos_vrf_af.py` exited 1; the three new route-target tests failed with `Unsupported parameters ... route_targets` (3 existing tests passed).

After implementation: `python -m pytest -q test/units/modules/network/nxos/test_nxos_vrf_af.py` exited 0 (7 passed). `git diff --check` exited 0. Integration test requires an NX-OS device and was not run locally.
