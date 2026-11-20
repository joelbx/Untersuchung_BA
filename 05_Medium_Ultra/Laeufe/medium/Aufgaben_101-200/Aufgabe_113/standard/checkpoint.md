Task: Add manual route-target management to nxos_vrf_af.
Status: Implemented route_targets with per-entry direction/state, exact configuration matching, and shared VRF/AF context. Added focused tests for mixed changes, scoping, context creation/removal, both directions, and EVPN auto idempotence. Focused pytest suite: 9 passed. git diff --check passed.
Constraints: local code/tests only; preserve git history, index baseline, and harness configuration.
