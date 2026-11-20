Task: implement manual route-target management in nxos_vrf_af.
Status: implemented route_targets list with required rt, direction/state defaults and choices; exact AF-block comparison helper; one scoped command batch with EVPN auto behavior preserved. Added unit coverage for creation, mixed add/remove, default both, idempotency, scoped AF/VRF, AF removal, and auto removal.
Verification: python -m pytest -q test/units/modules/network/nxos/test_nxos_vrf_af.py (9 passed); git diff --check passed.
Delegation: none.
