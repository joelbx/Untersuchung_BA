Updated [nxos_vrf_af.py](/app/lib/ansible/modules/network/nxos/nxos_vrf_af.py) to manage multiple import and export route-targets per VRF address family, including mixed additions and removals. It also exposes `match_current_rt` and documents the new option.

Verification: the focused unit suite passed (10 tests), and `git diff --check` passed.