Task: add manually configurable route targets to nxos_vrf_af.
Status: implemented route_targets with per-entry direction and state, idempotent comparison, and AF-scoped commands. Added mixed/scoping and absent-AF tests. Verification: 5 nxos_vrf_af unit tests passed.
