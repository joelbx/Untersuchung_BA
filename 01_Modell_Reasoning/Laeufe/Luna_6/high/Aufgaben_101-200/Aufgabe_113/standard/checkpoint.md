# Checkpoint

Implemented `route_targets` list support in `nxos_vrf_af`, including `rt`, `direction` (`both` by default), and per-entry `state` (`present` by default). The module now emits add/remove commands only for the selected VRF address-family, expands `both` to import and export, and includes the address-family context when applying changes to an existing context. `state=absent` continues to remove the address-family without processing route-target settings.

Added unit coverage for mixed add/remove operations, `both` idempotency, and the public `match_current_rt` helper.

Validation: `python -m pytest -q test/units/modules/network/nxos/test_nxos_vrf_af.py` passed (6 tests); `git diff --check` passed.
