# Checkpoint

Task: Add manual route-target management to `nxos_vrf_af` for IPv4 and IPv6 VRF address families.

Initial inspection: module currently manages address-family presence and EVPN auto only; unit tests cover the basic cases. Working tree was clean.

Completed: added `route_targets` nested options, a scoped route-target comparison helper, and command generation for mixed add/remove operations. Updated module examples and unit tests for IPv4/IPv6, both directions, scoped changes, idempotence, EVPN auto interaction, address-family removal, and validation.

Verification: `PYTHONPATH=lib:test/units python -m pytest -q test/units/modules/network/nxos/test_nxos_vrf_af.py` (10 passed); `git diff --check` passed.
