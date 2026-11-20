# ICX logging checkpoint

Issue: implement missing ICX logging module. Following assigned systematic-debugging phases. Initial inspection confirms no `icx_logging.py`; neighboring ICX modules and IOS logging module exist. `rg` is unavailable (`/bin/bash: rg: command not found`), so local searches use `find`/`grep`. No fix attempted yet.

Root cause: repository contains no ICX logging module. Reproduction test `PYTHONPATH=lib:test python -m pytest -q test/units/modules/network/icx/test_icx_logging.py` fails during collection with `ImportError: cannot import name 'icx_logging'`. Existing ICX system module supplies the connection and environment fallback pattern; IOS/VyOS logging modules supply aggregate argument patterns but do not handle ICX syntax. Hypothesis: adding an ICX-specific parser and command diff resolves the missing behavior.

Implementation: added ICX logging module with aggregate normalization, conditional validation, IPv6-aware host parsing and commands, facility clearing, buffered level diffs, console/global/persistence/RFC5424 handling, and check mode. Added focused unit tests. A second reproduction exposed malformed IPv6-style names being accepted; validation now rejects them.

Verification: `PYTHONPATH=lib:test python -m pytest -q test/units/modules/network/icx` passed: 103 tests. No external tooling or downloads used.
