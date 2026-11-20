# Checkpoint

Task: Add manually configurable route-target values to nxos_vrf_af.
Status: Complete. The module accepts route_targets entries with rt, direction, and state; reconciles import/export entries in the selected VRF address-family; preserves EVPN auto behavior and context state handling.
Verification: PYTHONPATH=lib:test python -m pytest -q test/units/modules/network/nxos/test_nxos_vrf_af.py (9 passed); git diff --check passed.
Changed files: lib/ansible/modules/network/nxos/nxos_vrf_af.py; test/units/modules/network/nxos/test_nxos_vrf_af.py.
