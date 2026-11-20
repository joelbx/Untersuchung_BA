Task: Add manual route-target management to nxos_vrf_af.
Status: Complete. Added route_targets argument with import/export/both directions,
present/absent per-entry state, exact scoped configuration matching, and
match_current_rt helper. Preserved address-family and EVPN auto behavior.
Verification: 9 nxos_vrf_af unit tests passed; git diff --check passed.
