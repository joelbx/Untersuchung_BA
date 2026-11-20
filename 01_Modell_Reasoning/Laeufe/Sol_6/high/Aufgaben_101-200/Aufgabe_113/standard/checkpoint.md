Task: add manual route-target management to nxos_vrf_af.
Status: implemented route_targets list with per-entry direction/state, exact-line comparison, and scoped address-family commands. Added focused unit coverage for mixed changes, idempotence, defaults, validation, absence, and scope.
Verification: 19 tests passed across nxos_vrf_af, nxos_vrf, and nxos_evpn_vni; git diff --check passed.
