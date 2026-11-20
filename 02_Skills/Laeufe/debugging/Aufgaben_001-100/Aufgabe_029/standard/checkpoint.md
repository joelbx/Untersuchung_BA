# Checkpoint

Task: Add NIOS fixed address module and API support for IPv4/IPv6.
Status: Investigating existing modules, API patterns, and tests before edits.
Environment: `rg` unavailable; using local `find` and `grep`. No external research or downloads.

Root cause: no fixed address module or object constants exist. Existing `WapiModule.run()` derives lookup fields from `ib_req` and uses the same keys for payloads; a new module must map `ipaddr` to the family-specific WAPI key before calling it. The existing `get_object_ref()` generic branch can query a full identity, but explicit fixed-address handling makes MAC-based identity clear. The network module supplies the working DHCP option transform pattern. Focused pre-fix test fails during import because the module is absent.

Implementation: added `nios_fixed_address` with IPv4/IPv6 validation and mapping, MAC/address/network/view identity, DHCP option transform, metadata, required provider, state and check mode. Added API object constants and explicit MAC-based fixed-address lookup branch. Added focused unit coverage for mapping, validation, option defaults, lookup, idempotence, and check mode.

Verification: `PYTHONPATH=lib:test python -m pytest -q test/units/modules/net_tools/nios test/units/module_utils/net_tools/nios` passed (68 tests). `python -m py_compile lib/ansible/modules/net_tools/nios/nios_fixed_address.py lib/ansible/module_utils/net_tools/nios/api.py` passed. `git diff --check` passed. No live Infoblox server was available; WAPI integration behavior is covered by mocked unit tests only.
