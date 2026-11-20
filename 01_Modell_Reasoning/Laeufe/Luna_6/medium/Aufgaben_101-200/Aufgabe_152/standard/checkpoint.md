# ICX logging module checkpoint

- Objective completed: added `icx_logging` for ICX 7000 logging destinations, aggregate requests, present/absent state, and running configuration reconciliation.
- Implementation: `lib/ansible/modules/network/icx/icx_logging.py` includes the requested mapping, parsing, comparison, validation, command generation, module entry point, check mode, and environment fallback.
- Command support includes IPv4/IPv6 host syntax and ports, console, buffered levels, persistence, RFC5424, facility changes/clearing, and global logging on/off.
- Verification: `python -m py_compile lib/ansible/modules/network/icx/icx_logging.py` succeeded; existing ICX unit suite passed (92 tests).
