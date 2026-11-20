# Checkpoint

Implemented `nios_fixed_address` for IPv4 and IPv6 with required name, IP, MAC, network, and provider; optional network view, DHCP options, extensible attributes, and comment; present/absent and check mode through WapiModule. Added address validation and WAPI field remapping. Added fixed address API constants and MAC-based lookup support, plus handling for multiple IPv6 references.

Verification:
- `python -m pytest -q test/units/module_utils/net_tools/nios test/units/modules/net_tools/nios` — 71 passed, exit 0.
- `git diff --check` — exit 0.
- Initial search used `rg`, unavailable with `/bin/bash: rg: command not found`; local `find` and `grep` were used instead.

One intermediate test run failed because a new test expected the unit test harness exception without installing its exit hook. The test was corrected and the full NIOS suite was rerun successfully.
